import PyPDF2
import sys

argv = sys.argv[1:]

temp = PyPDF2.PdfFileReader(open(argv[0], 'rb'))
wtrmark = PyPDF2.PdfFileReader(open(argv[1], 'rb'))


def watermark(template, watermark):
    writer = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        writer.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            writer.write(file)


if __name__ == '__main__':
    watermark(temp, wtrmark)
