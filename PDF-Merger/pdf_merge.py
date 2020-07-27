import PyPDF2
import sys

pdfs = sys.argv[1:]


def pdf_merg(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged_pdf.pdf')


if __name__ == '__main__':
    pdf_merg(pdfs)
