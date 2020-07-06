# Merge two PDFs
from PyPDF2 import PdfFileReader, PdfFileWriter

import os, glob

def add_page(source_path, source_file):
	os.makedirs('./converted/'+source_path,exist_ok=True)
	output = PdfFileWriter()
	sourcePdf = PdfFileReader(source_path +"/"+ source_file, "rb") #source file
	blankPdf = PdfFileReader("blank.pdf", "rb") #blank page

	output.addPage(sourcePdf.getPage(0))
	output.addPage(blankPdf.getPage(0))

	pageCount = sourcePdf.getNumPages()

	for x in range(0,pageCount):
		if x == 0:
			continue
		output.addPage(sourcePdf.getPage(x))

	outputStream = open("./converted/"+source_path+"/"+source_file, "wb")
	output.write(outputStream)
	outputStream.close()


os.makedirs('converted',exist_ok=True)
rootDir = 'files'

for root, dirs, files in os.walk(rootDir):
	print("Files --------------------------")
	for file in files:
		print(os.path.join(root, file))
		if file.endswith('.pdf'):
			if file.startswith('blank') == False:
				add_page(root, file)
	#	print('\t%s' % fname)

#for file in os.listdir('.'):
#	if file.endswith('.pdf'):
#		if file.startswith('blank') == False:
#			add_page(file)

