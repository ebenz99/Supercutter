import logging
import threading
import time
import queue
from libs.downloader import *
from libs.transcriber import *
from libs.cutter import *
from libs.stitcher import *

my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
    my_queue.put(f(*args))
  return wrapper

@storeInQueue
def my_transcribe(keyword):
	return transcribe(keyword)

#url = input()
url = "https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9"

keyword = input("What's your keyword?\n")
#keyword = "facebook"



dlar(url)
dlvr(url)
result_dic = transcribe(keyword)
cut(result_dic)
stitch()
clean()

'''
#for threading
t2 = threading.Thread(target=dlvr,args=(url,))
t2.start()
dlar(url)

t3 = threading.Thread(target=my_transcribe,args=(keyword,))
t3.start()
t2.join()
t3.join()

cut(my_queue.get())
'''



