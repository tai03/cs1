import time
localtime = time.asctime( time.localtime(time.time()) )
TIme = tuple(localtime)
print(TIme)