import requests
import math
import unittest
import sys
sys.path.append("..")
from utils import  *
from time import sleep
import re
#typical way to get the download file name from requests' response
#fileNames = re.findall("filename=(.+)", r.headers['content-disposition'])

class TestCase01(unittest.TestCase):
    def test_progressbar(self):
        url = "https://releases.hashicorp.com/consul/1.4.3/consul_1.4.3_windows_amd64.zip"
        # Streaming, so we can iterate over the response.
        r = requests.get(url, stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0)); 
        block_size = 1024*1024
        writtenBytes = 0 

        with open('output.bin', 'wb') as f:
            for data in r.iter_content(block_size):
                writtenBytes = writtenBytes  + len(data)
                printProgressBar(writtenBytes, total_size, prefix = 'Progress:', suffix = 'Complete', length = 50)
                f.write(data)
        if total_size != 0 and writtenBytes != total_size:
            print("ERROR, something went wrong") 


if __name__ == '__main__':
     unittest.main()