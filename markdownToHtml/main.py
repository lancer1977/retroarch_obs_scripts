# Use with https://obsproject.com/forum/resources/xobsbrowserautorefresh-timed-automatic-browser-source-refreshing.1677/
 
import time 
from markdown_observer import MarkdownObserver
from settings import CurrentSettings

if __name__ == "__main__":
    monitor = MarkdownObserver()  
    CurrentSettings.updateExternalChange = monitor.startMonitor
    CurrentSettings.startMonitor()
    monitor.startMonitor()
    try:
        while True:
            time.sleep(CurrentSettings.sleep_seconds)
    except KeyboardInterrupt:
        monitor.stopMonitor()
        CurrentSettings.stopMonitor()
 
