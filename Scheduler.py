import schedule
import time 
from ScannerDeteccion import getter
getter=getter()
schedule.every(2).minutes.do(getter)
#Revisiones 
while True:
    schedule.run_pending()
    time.sleep(1)