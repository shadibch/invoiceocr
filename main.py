import ocr
import json
import sys
invoice = ocr.invoice(sys.argv[1])
with open("data_file.json", "w") as write_file:
    json.dump(invoice, write_file,indent=4)


