import sys
import urllib.request
from urllib.error import HTTPError
from socket import timeout

BASE_URL = 'http://dx.doi.org/'
bibs = []
dois = []
doisnotfound = []
count = 1

#read input
if len(sys.argv) < 3:
	print("Please enter the names of the input and output files, respectively.")	
	sys.exit(-1)

#read file
with open(sys.argv[1]) as input_file:
	doi = input_file.readlines()

#get BibTex
for d in doi:
    url = BASE_URL + d
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    
    try:
        print("bib " + str(count) + " of " + str(len(doi)))
        with urllib.request.urlopen(req, timeout=30) as f:  
            bibtex = f.read().decode()
        bibs.append(bibtex)
        print("DOI successfully converted: " + d +"\n")

    except HTTPError as e:
        if e.code == 404:
            print('DOI not found: ' + d + "\n")
            doisnotfound.append(d)
			
        else:
            print('Service unavailable: ' + d)
            doisnotfound.append(d)
    except timeout:
        print('Connection timed out: ', d)
        notfound.append(d)
    count +=1

#write bibs file
for b in bibs:
    file = open(sys.argv[2], "a") 
    file.write(b) 
print("BibText file successfully saved")
file.close()

#write DOI not found file
for nf in doisnotfound:
    file = open("DOInotfound.txt", "a") 
    file.write(nf)
print("DOIS report not found saved successfully")
file.close() 
              