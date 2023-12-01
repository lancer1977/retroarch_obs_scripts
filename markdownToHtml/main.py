# Use with https://obsproject.com/forum/resources/xobsbrowserautorefresh-timed-automatic-browser-source-refreshing.1677/
 
import time 
import file_monitor
from settings import CurrentSettings

if __name__ == "__main__":
    CurrentSettings.startMonitor() 
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        file_monitor.observer.stop()

    file_monitor.join()
