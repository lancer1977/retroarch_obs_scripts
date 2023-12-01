from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




class FileMonitor(FileSystemEventHandler):
    observer: Observer = None
    
    folder:str
    filepath:str
    action = print("test")
    
    def on_modified(self, event):
        if event.is_directory:
            return
        # Execute your method here
        if(self.filepath == event.src_path):
            self.action()        

    def startMonitor(self): 
        if(self.observer != None):
            self.observer.stop()
        self.observer = Observer()
        self.observer.schedule(self, self.folder, recursive=True)
        try:
            self.observer.start()
        except Exception as e:
            print("Error: unable to start monitor for ", e)


    def stopMonitor(self):
        self.observer.stop()