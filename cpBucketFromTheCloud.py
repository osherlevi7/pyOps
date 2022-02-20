#!/usr/bin/env python3
import os
list = ["7f9d568d-c273-4d44-96c4-09252d780f07",
"f0a030ee-981c-4c8a-b0a4-21e53dd8c131",
"7cd62e09-69d9-45fe-a3a7-429a66d1989f"]


for i in list:
   print("Scan - ", i, "download seccessfully")
   os.system("gsutil -m cp -r gs://bucketName/objName/distFolder/" + i + " .")
   print ('Succesfully download all the bucket from the list') 