from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf,)

merger.write("result.pdf")
merger.close()