import requests
import pandas as pd
from datetime import datetime
from selenium import webdriver
import random
import os


proxies = []
file_path = os.path.join(os.getcwd(), "heroku/http_proxies.txt")
with open(file_path) as f:
    proxies = f.read().splitlines()
    print(proxies)


proxies = random.sample(proxies, 2)



while len(proxies) > 0:
    proxy = proxies.pop(0)
    print(f"Testing proxy: {proxy}")

try:
# Call IP and add new row/df
    response = requests.get("https://httpbin.org/anything", proxies={"http": proxy, "https": proxy}, timeout=60)
    if response.status_code == 200:
        print(f"Working proxy found: {proxy}")
        response = response.json()
        print(response)
        ip = response["origin"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # current time as a string


    # create new document
        new_ip = {
        'ip' : f'{ip}',
        'current_time' : f'{current_time}'
        }
        # records.insert_one(new_ip)
        print(new_ip)



    # find one specific document (always finds the first one)
    # document = records.find_one({'ip' : f'{ip}' })
    # print(document)



        # after successful run, take proxy out
        if proxy in proxies:
            proxies.remove(proxy)



except Exception as e:
    print(f"Error with proxy {proxy}: {e}")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # current time as a string
# create new document
    new_ip = {
    'ip' : f'{proxy}',
    'current_time' : f'{current_time}',
    'error' : f'ERROR : {e}'
    }
    # records.insert_one(new_ip)
    print(new_ip)
    if len(proxies) == 0:
        print("No working proxies found.")