# 2020/2/10
# VictorGanro 编写
# 用于解析视频。下载视频
# 第三方环境 JAVA browsermobproxy
## 必须需要JAVA环境
##
#  GANRO更新 2020/4/30
#  1.对爱奇艺数据下载的修复
#  2.最aira2下载的支持
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import os
from HTML_GET import htmlget
from download import downlaod
def url_return(GET_URL):
    file_path = os.getcwd()
    print(file_path+"\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    server = Server(file_path+"\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    server.start()
    proxy = server.create_proxy()
 
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
#要访问的地址
    #GE_URL = input("输入你想要解析的URL:") #输入解析的URL
    base_url = "http://jx.du2.cc/?url="+GET_URL
    proxy.new_har("ht_list2", options={ 'captureContent': True})
 
    driver.get(base_url)
#此处最好暂停几秒等待页面加载完成，不然会拿不到结果
    time.sleep(15)
    result = proxy.har
    FLAGE = ""
    MOVE_URL = []
    for entry in result['log']['entries']:
        _url = entry['request']['url']
        print(_url)
        if _url.find("mp4")>=0:
            MOVE_URL.append(_url)
            FLAGE = "MP4"
            print("MP4")
        if _url.find(".m3u8")>=0:
            print("ts")
            MOVE_URL.append(_url)
            FLAGE = "TS"
    #else:
        #if _url.find(".ts")>=0:
            #MAIN_URL = re.findall("(.*?/hls/).*?",_url)[0] #TS 主URL的标头
    # # 根据URL找到数据接口,这里要找的是 http://git.liuyanlin.cn/get_ht_list 这个接口
    # if "http://git.liuyanlin.cn/get_ht_list" in _url:
    #     _response = entry['response']
    #     _content = _response['content']
    #     # 获取接口返回内容
    #     print(_response)
#去重
    MOVE_URL = list(set(MOVE_URL))
    print(MOVE_URL)
    server.stop()
    driver.quit()
    def get_ts_urls(m3u8_path,base_url): #筛选TS列表
        urls = []
        with open(m3u8_path,"r",encoding="UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.find(".ts")>0:
                    if base_url == None:
                        urls.append(line.strip("\n"))
                    else:
                        urls.append(base_url+line.strip("\n"))
        return urls
    if FLAGE == "TS":
        CODE = htmlget(MOVE_URL[0],"UTF-8","NO","") #请求M3U8数据
        print(CODE)
        f = open("MAP.M3GANRO","w",encoding="UTF-8")
        f.write(CODE)
        f.close()
    #下载URLS中的 TS视频
        #print("开始下载")
        LIST_URL = get_ts_urls("MAP.M3GANRO",None) #解析TS数据条 储存在LIST_URL
        print(LIST_URL)
        return LIST_URL
    #print(LIST_URL)
    #print(LIST_URL[0])
    # for i in range(len(URLS)):
    #     downlaod(URLS[i],os.getcwd()+"\\chace\\"+chace_file_name,str(i)+".ts")
    #     print("当前进度:"+str(int((i+1)/len(URLS)*100)))
        #print("ENDING------------->>>>>>>>>>>>>>>>>")
    #print(CODE)
    if FLAGE == "MP4":
        #print("开始下载")
        return ["mp4",MOVE_URL[0]]
        #file_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+".mp4"
        #downlaod(MOVE_URL[0],os.getcwd()+"\\MOVES\\",file_name)
        #print("ENDING ----------->>>>>>>>>>>>>>>>")
    #直接下载
    else:
        return False
