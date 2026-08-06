"""
RansomShield Main Controller

Launches:
1. Security Assessment GUI
2. Watchdog File Monitoring System
"""

import sys
import os
import threading


# Add project folder to Python path

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from gui import start_gui
from detection.file_monitor import start_monitor



MONITOR_FOLDER = os.path.join(
    PROJECT_ROOT,
    "test_environment",
    "test_files"
)



def start_watchdog():

    start_monitor(
        MONITOR_FOLDER
    )



def main():

    print(
        """
=================================

        RansomShield

 Ransomware Defense Framework

=================================
        """
    )


    monitoring_thread = threading.Thread(
        target=start_watchdog
    )


    monitoring_thread.daemon = True

    monitoring_thread.start()


    print(
        "[+] File monitoring activated"
    )


    print(
        "[+] Launching security dashboard"
    )


    start_gui()



if __name__ == "__main__":

    main()
