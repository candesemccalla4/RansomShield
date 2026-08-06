"""
RansomShield File Monitoring Module

Uses Watchdog to monitor file system activity.
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class RansomShieldHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:

            print(
                "[+] New file detected:",
                event.src_path
            )


    def on_modified(self, event):

        if not event.is_directory:

            print(
                "[+] File modified:",
                event.src_path
            )


    def on_deleted(self, event):

        if not event.is_directory:

            print(
                "[-] File deleted:",
                event.src_path
            )


    def on_moved(self, event):

        if not event.is_directory:

            print(
                "[!] File renamed:",
                event.src_path,
                "to",
                event.dest_path
            )



def start_monitor(folder):

    print(
        "RansomShield monitoring started..."
    )

    print(
        "Watching:",
        folder
    )


    event_handler = RansomShieldHandler()


    observer = Observer()


    observer.schedule(
        event_handler,
        folder,
        recursive=True
    )


    observer.start()


    try:

        while True:

            time.sleep(1)


    except KeyboardInterrupt:

        observer.stop()


    observer.join()
