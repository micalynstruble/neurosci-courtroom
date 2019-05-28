!pip install PyPDF2

import PyPDF2 
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#reading a pdf file
pdfFileObj = open('401 F.3d 574.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#getting page number and extracting text
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

#getting number of pages
num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()
res = text.translate(str.maketrans('', '', string.punctuation))

#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

  #The word_tokenize() function will break our text phrases into #individual words
tokens = word_tokenize(text)