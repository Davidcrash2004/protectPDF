from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

file = input('introduce el nombre exacto de tu archivo: ')
password = input('introduce una contraseña para el archivo: ')

def secure_pdf(file, password):
	parser = PdfFileWriter()
	pdf = PdfFileReader(file)

	for page in range(pdf.numPages):
		
		parser.addPage(pdf.getPage(page))
	parser.encrypt(password)
	with open(f"encrypted_{file}", "wb") as f:
		parser.write(f)
	print(f"encrypted_{file} Creado...")


if __name__ == "__main__":
	secure_pdf(file, password)
