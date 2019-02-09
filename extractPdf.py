import sys

def extractPDF(path):
    result = []
    pdf = open(path, "rb").read()
    startmark = b"\xff\xd8"   
    startfix = 0  
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find("stream".encode(), i)

        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream+20)
        print(istart)
        if istart < 0:
            i = istream+20
            continue
        iend = pdf.find("endstream".encode(), istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend-20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")
        istart += startfix
        iend += endfix
        print ("JPG %d from %d to %d" % (njpg, istart, iend))
        jpg = pdf[istart:iend]
        jpgfile = open("jpg%d.jpg" % njpg, "wb")
        jpgfile.write(jpg)
        jpgfile.close()
        result.append("jpg%d.jpg" % njpg)    
        njpg += 1
        i = iend
    return result
      
