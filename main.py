import boto3
import pathlib
import os
import json
import urllib.request, json
import requests as r
import pandas as pd
import csv

file = 'test.json'

file2 = 'test'


response = r.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20220201&end=%2020221012&sort=exchangedate&order=desc&json')
json_object = json.dumps(response.json())

with open(file, "w") as outfile:
    outfile.write(json_object)


s3_client = boto3.client('s3')
file_name = 'C:\\Users\\Vlad\\Desktop\\laba2\\test.json'
bucket_name = 'mynewlabdata'
object_name = 'sample1.json'
response = s3_client.upload_file(file_name, bucket_name, object_name)





