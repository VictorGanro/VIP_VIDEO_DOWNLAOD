import urllib.request
import ssl
import random
import os 
from fake_useragent import UserAgent
import requests
ssl._create_default_https_context = ssl._create_unverified_context
def htmlget(url,bianma,POST_OR_NOT,POST_data):  
    #POST_DATA IS DICTIONARY TYPE {"NAME":"123"}
    try:
        location = os.getcwd() + '\\data.json'
        ua = UserAgent(path=location)
        head = ua.random
        #print(head)
        headersl = {"User-Agent":head}
        if POST_OR_NOT == "YES":
            get_url = requests.post(url = url,data=POST_data,headers=headersl,timeout=5)
        else:
            get_url = requests.get(url,headers=headersl,timeout=5)
        get_url.encoding = bianma
        print("[+]LOG: GET SUCCESS")
        return get_url.text
    except:
        print("[-]LOG: GET ERROR")
        #print("链接目标网站超时，更换随机header重试")
        while True:
            fla = 0
            try:
                head = ua.random
                #print(head)
                headersl = {"User-Agent":head}
                if POST_OR_NOT == "YES":
                    get_url = requests.post(url = url,data=POST_data,headers=headersl,timeout=5)
                else:
                    get_url = requests.get(url,headers=headersl,timeout=5)
                get_url.encoding = bianma
                print("[+]LOG: GET SUCCESS")
                return get_url.text
            except:
                fla = fla +1
                if fla ==4:
                    break
                    return None
                #print("链接目标网站超时，继续更换")

