import os
import time
from pyaria2 import Aria2RPC
def downlaod(link, file_name,save_file):
    jsonrpc = Aria2RPC()
    set_dir = save_file
    options = {"dir": set_dir, "out": file_name, }
    res = jsonrpc.addUri([link], options = options)
    return res #返回MD5代码