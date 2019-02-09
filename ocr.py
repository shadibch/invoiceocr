from PIL import Image
import pytesseract
import argparse
import cv2
import os
import sys
import extractPdf
import re

regex = re.compile('[-+]?([1-9]+,)?[0-9]*\.[0-9]+$')
ap = argparse.ArgumentParser()

def invoice(imagePath):
    invoice = ocr(imagePath)
    return parseInvoice(invoice)
def ocr(imagePath):
    if imagePath.endswith(".pdf"):
        im = extractPdf.extractPDF(imagePath)
        str = ""
        for i in im:
            str += pytesseract.image_to_string(Image.open(i))
        return str
    return pytesseract.image_to_string(Image.open(imagePath))
item = {}
def parseInvoice(str):
    invoice = {}
    lines = str.splitlines()
    items = False
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        if not items:
            if line.startswith("T. R No "):            
                start = len("T. R No ") +3
                invoice['inno'] = line[start:].strip()
            if line .startswith("M/s."):
                start = len("M/s.") +2
                index = line.index("No.")
                invoice['to']=line[start:index].strip()
                invoice['no']=line[index + 3 :].strip()
            if line.startswith("Kind Attn"):
                start = line.index(":")
                end = line.index("Date")
                invoice['attention'] = line[start + 1:end].strip()
                invoice['date'] = line[end + 6 :].strip()
            if line.startswith("Project"):
                start = line.index(":") + 1
                end = line.index("Qtn")
                invoice["project"] = line[start:end]
                qtn = line[end + 7:]
                invoice["qtn"] = qtn.strip()
            if line.startswith("S.No."):
                items = True
                invoice["items"] = []
        else:
            idx = line.find(".")
            print(idx)
            if  idx > -1 and idx < 4:
                item = {}
                item["items"] = []
                sn = line[:idx ].strip()
                item["sn"] = sn
                invoice["items"].append(item)
                index = regex.search(line)
                if index != None:
                    value = line[index.start():]
                    description = line[idx:index.start()]
                    item["items"].append({"description":description,"value":value})
                else:
                    description = line[idx:]
                    item["items"].append({"description":description})
            else: 
                if line.startswith("Total"):
                     invoice["items"][-1]["total"] = line[6:].strip()
                elif line.startswith("Vat@5%"):
                     invoice["items"][-1]["vat"] = line[7:].strip()
                elif line.startswith("Grand Total"):
                     invoice["grandTotal"]={}
                     lines_ = line.split(" ")
                     invoice["grandTotal"]["value"] = lines_[-1]
                     invoice["grandTotal"]["currency"]= lines_[-2]
                else:              	
                    index = regex.search(line)
                    if index != None:
                        value = line[index.start():]
                        description = line[:index.start()]
                        item["items"].append({"description":description,"value":value})                                   
                    else:
                        description = line
                        print(invoice["items"])
                        invoice["items"][-1]["items"].append({"description":description})
                
    return invoice



