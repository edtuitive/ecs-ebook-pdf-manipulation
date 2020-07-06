# Remove page 3
from PyPDF2 import PdfFileReader, PdfFileWriter

import os, glob

def remove_page(source_file):
	print(source_file)
	output = PdfFileWriter()
	sourcePdf = PdfFileReader(source_file, "rb") #source file

	pageCount = sourcePdf.getNumPages()

	for x in range(0,pageCount):
		if x == 2:
			continue
		output.addPage(sourcePdf.getPage(x))

	outputStream = open("./converted/"+source_file, "wb")
	output.write(outputStream)
	outputStream.close()

os.makedirs('converted')

for file in os.listdir('.'):
	if file.endswith('.pdf'):
		if file.startswith('blank') == False:
			remove_page(file)


