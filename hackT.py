import random
import os
import time
import threading
import sys
import pickle
import subprocess
from datetime import datetime

from var import *
from other import *
from function import *
from missions import *

def run_hostile_mode():
    """
    Runs the hostile/hacker terminal in isolation.
    Loads game state from pickle, runs Hostile_terminal, and saves state back.
    """
    # Load ALL variables from temporary file passed from main.py
    TEMP_FILE = os.path.join(os.path.dirname(__file__), "temp_tracked_computer.pkl")

    if os.path.exists(TEMP_FILE):
        with open(TEMP_FILE, "rb") as f:
            (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
             Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
             Number_OF_MALWARES, Money, Honor, MAX_Integrity) = pickle.load(f)
    else:
        print("Error: No tracked computer found. Please track a computer in the main game first.")
        sys.exit(1)

    # Call the hostile terminal and unpack all returned values
    (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity) = Hostile_terminal(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity)

    # Save ALL modified variables back to the file for main.py to read
    data_to_save = (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                    Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                    Number_OF_MALWARES, Money, Honor, MAX_Integrity)

    with open(TEMP_FILE, "wb") as f:
        pickle.dump(data_to_save, f)

    print("\nLogging out of hostile terminal...")
    print(f"\nGoodbye, {tracked_computer.UserName}.")
    time.sleep(1)


def run_hacker_terminal():
    """
    Opens a new CMD window to run the hostile terminal in isolation.
    Passes the "hostile" argument to main.py to trigger hostile mode.
    """
    # For PyInstaller exe support: Get the executable path
    executable_path = sys.executable
    
    # Call main.py/exe with "hostile" argument in a new console window
    subprocess.call(
        [executable_path, "hostile"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


# If this script is run directly with "hostile" argument, run hostile mode
if __name__ == "__main__":
    if "hostile" in sys.argv or len(sys.argv) > 1:
        run_hostile_mode()
    else:
        # If called directly without hostile arg, show error
        print("Error: This script should be called from the main game with 'hostile' argument.")
        sys.exit(1)