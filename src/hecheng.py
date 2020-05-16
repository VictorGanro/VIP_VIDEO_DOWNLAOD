import os
def combine(ts_path, combine_path, file_name):
    file_list = os.listdir(ts_path)
    for i in range(len(file_list)):
        file_list[i] = ts_path+"\\"+file_list[i]
    file_path = combine_path +"\\"+ file_name + '.ts'
    with open(file_path, 'wb+') as fw:
        for i in range(len(file_list)): 
            fw.write(open(file_list[i], 'rb').read())
def GET_TO_MP4(TS_file_path,file_name_for_mp4):
    code = "ffmpeg.exe -i "+TS_file_path +" -c copy "+file_name_for_mp4
    os.system(code)
