from PyPDF2 import PdfFileMerger
# "py -m pip install PyPDF2" you need the python module "PyPDF2" for this to work
pdfs = ['1.pdf', '2.pdf', '3.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf,)

merger.write("result.pdf")
merger.close()