from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("guide_to_dddm.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)