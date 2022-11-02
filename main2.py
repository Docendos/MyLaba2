import boto3
import pathlib
import os
import json
import urllib.request, json
import requests as r
import pandas as pd
import csv

bucket_name = 'mynewlabdata'
file_to_download = 'sample1.json'
path = 'C:\\Users\\Vlad\\Desktop\\laba2\\new1_json.json'

s3 = boto3.client('s3')
s3.download_file(bucket_name, file_to_download, path)

temp = pd.read_json('C:\\Users\\Vlad\\Desktop\\laba2\\new1_json.json')
csvData = temp.to_csv(index=False)

file_csv = 'new_csv.csv'

with open(file_csv, 'w', encoding='utf8') as file:
    file.write(csvData)


file_name = 'C:\\Users\\Vlad\\Desktop\\laba2\\new_csv.csv'
bucket_name = 'mynewlabdata'
object_name = 'sample_csv.csv'
response = s3.upload_file(file_name, bucket_name, object_name)