import time, threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CanaryHandler(FileSystemEventHandler):
    def __init__(self, threshold, alert_func):
        self.events = []
        self.threshold = threshold
        self.alert_func = alert_func
        self.lock = threading.Lock()

    def record_event(self, event):
        with self.lock:
            self.events.append((event.event_type, event.src_path, time.time()))
            now = time.time()
            self.events = [e for e in self.events if now - e[2] < 5]
            if len(self.events) >= self.threshold:
                self.alert_func(self.events)
                self.events = []

    def on_created(self, event):
        self.record_event(event)
    def on_deleted(self, event):
        self.record_event(event)
    def on_modified(self, event):
        self.record_event(event)
    def on_moved(self, event):
        self.record_event(event)

def watch_canaries(paths, threshold, alert_func):
    observer = Observer()
    handler = CanaryHandler(threshold, alert_func)
    for p in paths:
        observer.schedule(handler, p, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
