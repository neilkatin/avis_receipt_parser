#! /usr/bin/env python3
import pymupdf4llm
md = pymupdf4llm.to_text("eReceipt903311032.pdf")
print(md)
