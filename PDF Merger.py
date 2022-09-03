# combining dummy.pdf and twopage.pdf
import PyPDF2


def pdf_combiner(*pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")  # to write file


pdf_combiner("dummy.pdf", "twopage.pdf")
