import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        # Execute your method here
        print(f'File {event.src_path} has been modified.')

if __name__ == "__main__":
    path = "D:\\code\\retro_obs\\markdownToHtml\\"
    event_handler = MyHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
