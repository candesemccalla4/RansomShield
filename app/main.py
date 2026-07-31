"""
RansomShield Main Controller

Launches:
1. Security Assessment GUI
2. Watchdog File Monitoring System
"""


import threading

from gui import start_gui

from detection.file_monitor import start_monitor



# Folder monitored by Watchdog

MONITOR_FOLDER = "../test_environment/test_files"



def start_watchdog():

    """
    Starts ransomware file monitoring
    """

    start_monitor(MONITOR_FOLDER)



def main():

    print(
        """
=================================

        RansomShield

 Ransomware Defense Framework

=================================
        """
    )


    # Start Watchdog in background

    monitoring_thread = threading.Thread(
        target=start_watchdog
    )


    monitoring_thread.daemon = True

    monitoring_thread.start()



    print(
        "[+] File monitoring activated"
    )


    print(
        "[+] Launching security assessment dashboard"
    )


    # Start GUI

    start_gui()



if __name__ == "__main__":

    main()
