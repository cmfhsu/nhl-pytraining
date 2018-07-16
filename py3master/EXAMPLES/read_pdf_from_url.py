#!/usr/bin/env python
import sys
import os
from urllib.request import urlopen
from urllib.error import HTTPError

# url to download a PDF file of Hamlet (by Wm. Shakespeare)

url = 'http://www.gutenberg.org/files/1524/old/2ws2610.pdf'
saved_pdf_file = '../TEMP/hamlet.pdf'

try:
    URL = urlopen(url)
except HTTPError as e:
    print("Unable to open URL:", e)
sys.exit(1)

pdf_contents = URL.read()
URL.close()

with open(saved_pdf_file, 'wb') as HAM:
    HAM.write(pdf_contents)

if sys.platform == 'win32':
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    cmd = 'open ' + saved_pdf_file
else:
    cmd = 'acroread ' + saved_pdf_file

os.system(cmd)
