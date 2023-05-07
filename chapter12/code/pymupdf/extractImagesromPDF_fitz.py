#!usr/bin/env python3

import fitz

pdf_document = fitz.open("pdf/XMPSpecificationPart3.pdf")  
for current_page in range(len(pdf_document)):  
    for image in pdf_document.get_page_images(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)
        pix.save("page%s-%s.png" % (current_page, xref))
        print("Extracted image page%s-%s.png" % (current_page, xref))
