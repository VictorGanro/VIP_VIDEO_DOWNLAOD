import sys
from Main import url_return
from download import downlaod
import time
import os
import asyncio
from hecheng import combine
from hecheng import GET_TO_MP4
def aira_run(): #启动aria2
    #aira_file = os.getcwd()+"\\aria2\\RUN_DOWNLOAD.exe"
    K = open("start.bat","w",encoding="UTF-8")
    K.write("cd "+os.getcwd()+"\\aria2\\" +"\n")
    K.write("start RUN_DOWNLOAD.exe")
    K.close()
    os.system("start.bat")
    time.sleep(5)
    #print("code :"+"start "+aira_file)
if sys.argv[1] ==None: #读取参数 如果没参数报错
    print("ERROR")
else:
    url = sys.argv[1]
    video_list = url_return(url)#解析出的URL数据
    if video_list == False:
        print("解析失败!")
    else:
        print("开始下载!")
        aira_run()
        if video_list[0] == "mp4": #MP4下载
            mp4_file = os.getcwd()+"\\MOVES"
            try:
                RES = downlaod(video_list[1],time.strftime("%Y%m%d%H%M%S", time.localtime())+".mp4",mp4_file)
                print("看下载窗口，百分百就可以了哦--------->>>>>>>>>")
                print("MD5---------->>>"+RES)
            except:
                print("下载失败--------->>>>>>>>")
        else: #TS下载
            chace_file = os.getcwd()+"\\chace\\"+time.strftime("%Y%m%d%H%M%S", time.localtime()) #缓存目录
            os.system("mkdir "+chace_file)
            print("缓存目录创建成功")
            async def download_a(url,file_name,save_path):
                try:
                    md5 = downlaod(url,file_name,save_path)
                    print("MD5数据为--------->>>>>>>>>>"+md5)
                except:
                    print("下载失败------->>>>>>")
            loop = asyncio.get_event_loop()
            task = []
            for i in range(len(video_list)):
                task.append(download_a(video_list[i],str(i)+".ts",chace_file))
            loop.run_until_complete(asyncio.wait(task))
            print("开始合成......")
            file_name_S = time.strftime("%Y%m%d%H%M%S", time.localtime())
            combine(chace_file,chace_file,file_name_S)
            save_mp4_path = os.getcwd()+"\\MOVES\\"
            GET_TO_MP4(chace_file+"\\"+file_name_S+".ts",save_mp4_path+file_name_S+".mp4")




