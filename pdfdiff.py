#!/usr/bin/env python

"""
  http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library  
"""
import os
import sys

from icdiff import diff
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def start():
    if len(sys.argv) <3:
         raise Exception('USAGE: pdfdiff a.pdf b.df')
    file_1 = sys.argv[-2]
    file_2 = sys.argv[-1]
    if not os.path.isfile(file_1) or not os.path.isfile(file_2): 
        raise Exception('Input file cant be located')
    file_1_split = os.path.splitext(file_1)
    file_2_split = os.path.splitext(file_2)
    if file_1_split[-1].lower() != '.pdf' and file_2_split[-1].lower() != '.pdf':
        raise Exception('file is not a pdf type')
    file_1_txt = file_1_split[0] + '.txt'
    file_2_txt = file_2_split[0] + '.txt'
    with open(file_1_txt, 'w') as fd1:
        fd1.write(convert_pdf_to_txt(file_1)) 
    with open(file_2_txt, 'w') as fd2:
        fd2.write(convert_pdf_to_txt(file_2)) 
    diff(file_1_txt, file_2_txt)
    os.remove(file_1_txt)
    os.remove(file_2_txt)

if __name__ == '__main__':
    start()
