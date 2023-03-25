from PyPDF2 import PdfFileReader
pdf = PdfFileReader(open('pdf/XMPSpecificationPart3.pdf','rb'))
print(str(pdf.getNumPages()))

from subprocess import check_output
def get_num_pages(pdf_path):
	output = check_output(["pdfinfo", pdf_path]).decode()
	pages_line = [line for line in output.splitlines() if "Pages:" in line][0]
	num_pages = int(pages_line.split(":")[1])
	return num_pages
    
print(get_num_pages('pdf/XMPSpecificationPart3.pdf'))
