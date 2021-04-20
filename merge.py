# Needs "pip install PyPDF2"
# Optional: "pip install pyinstaller"
# Optional: PyInstaller -F ./Sourcefile.py


from PyPDF2 import PdfFileMerger
pdfs = ['1.pdf', '2.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf,)

merger.write("result.pdf")
merger.close()