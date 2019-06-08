import logging
import threading
import time
from downloader import *
from transcriber import *


#url = input()
url = "https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9"

#keyword = input()
keyword = "nine"

t1 = threading.Thread(target=dlar,args=(url,))
t2 = threading.Thread(target=dlvr,args=(url,))
t1.start()
t2.start()
t1.join()

t3 = threading.Thread(target=transcribe,args=(keyword,))
t3.start()
t2.join()
t3.join()




