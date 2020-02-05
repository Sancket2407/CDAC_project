#@Author:Shreya
#Date:
import boto3
import sys
import glob
import errno
import os

from bs4 import BeautifulSoup
import requests
from bs4.dammit import EncodingDetector
import re

requ_object = requests.get("https://en.wikipedia.org/wiki/India")
http_encode = requ_object.encoding if 'charset' in requ_object.headers.get('content-type', '').lower() else None
html_encode = EncodingDetector.find_declared_encoding(requ_object.content, is_html=True)
encoding = html_encode or http_encode
soup = BeautifulSoup(requ_object.content, from_encoding=encoding)

image =[]

#@Author:Shreya&Rohit
#Date:
def get_image():
    j=0
    for i in soup.find_all('img', {'src':re.compile('.jpg')}):
        image.append(i['src'])
    image1 = image[1:]
    for i in image1:
        print(i)
        extention = os.path.splitext(i)[-1]
        page = requests.get('https:'+i)
        f_name = 'img'+str(j)+'{}'.format(extention)
        j+=1
        with open('images/'+f_name, 'wb') as f:
            f.write(page.content)

get_image()

#@Author:Rohit
#Date:

s3_resource = boto3.resource('s3')

def upload_objects():
      try:
              bucket_name = "group-1-bucket"
              root_path = '/home/hadoop/images'
              my_bucket = s3_resource.Bucket(bucket_name)
              for path, subdirs, files in os.walk(root_path):
                      path = path.replace("\\","/")
                      directory_name = "Raw_zone/unstructure_image/"
                      for file in files:
                              my_bucket.upload_file(os.path.join(path, file), directory_name+'/'+file)
      except Exception as err:
              print(err)

upload_objects()



