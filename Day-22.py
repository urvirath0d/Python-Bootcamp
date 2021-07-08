# importing PIL
from PIL import Image

# Read image
img = Image.open(r"D:\check.jpeg")

# Output Images
img.show()

# prints format of image
print(img.format)

# prints mode of image
print(img.mode)
import PyPDF2
# import webbrowser

# Open the files that have to be merged one by one
pdf1File = open(r'D:\VGEC-00266.pdf', 'rb')
pdf2File = open(r'D:\VGEC-00266.pdf', 'rb')

# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

# Load pagenumbers for the first document
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Load pagenumbers for the second document
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# write document file
pdfOutputFile = open('MergedFiles.pdf', 'wb')
# path = 'MergedFiles.pdf'
# webbrowser.open_new(path)
pdfWriter.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()