# Needs "pip install PyPDF2"
# Optional: "pip install pyinstaller"
# Optional: PyInstaller -F ./Sourcefile.py

from PyPDF2 import PdfMerger

pdfs = ['1.PDF', '2.PDF', '3.PDF', '4.PDF', '5.PDF', '6.PDF']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
