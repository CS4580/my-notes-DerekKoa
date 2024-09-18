"""Download data from our serber
"""
import urllib
import requests
import zipfile
import shutil
import sys, os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


SERVER_URL = 'https://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def download_file(url, file_name):
    #TODO: download to pwd

    dest_path = os.path.join(os.getcmd(), os.path.basename(url))
    req = request.get(url, stream=True)

    if response.status_code == 200:
        with open(dest_path, 'wb') as out file:
          shutil.copyfileeob()
    try:
        resonse = urlopen(req)  
    except HTTPError as e:
        print('ERROR CODE:', e.code)
    except URLError as e:
        print('ERROR CODE', e.code)
    else:
        print('Success')

    
    #TODO: check extension if zip call unzip file f(x)
    pass

def unzip_file(file_name):
    #TODO: uzip file
    extract_path = os.getcwd()

    with zipfile.ZipFile(zip_path, 'r') as zip_ref
    pass

def main():
    """Driven Function
    """
    data = 'pandas01data.zip'
    download_file(SERVER_URL, data)
    unzip_file(data)



if __name__ == '__main__':
    main()