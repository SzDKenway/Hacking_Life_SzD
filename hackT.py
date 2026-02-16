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
from missions import *


def run_hacker_terminal(tracked_computer, Integrity, NUMBER_OF_viruses,
                        NUMBER_OF_DDoS, Number_OF_Decoders,
                        Downloaded_Files, NUMBER_OF_BBRUTEF,
                        Number_OF_MALWARES, Money, Honor, MAX_Integrity):

    print("Opening hostile terminal in new window...")
    time.sleep(1)

    with open("hostile_save.pkl", "wb") as f:
        pickle.dump((
            tracked_computer,
            Integrity,
            NUMBER_OF_viruses,
            NUMBER_OF_DDoS,
            Number_OF_Decoders,
            Downloaded_Files,
            NUMBER_OF_BBRUTEF,
            Number_OF_MALWARES,
            Money,
            Honor,
            MAX_Integrity
        ), f)

    process = subprocess.Popen(
        [sys.executable, "hostile"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    process.wait()

    with open("hostile_save.pkl", "rb") as f:
        result = pickle.load(f)

    os.remove("hostile_save.pkl")

    print("\nLogging out of hostile terminal...")
    print(f"\nGoodbye, {result[0].UserName}.")
    time.sleep(1)

    return result


def run_hostile_mode():
    with open("hostile_save.pkl", "rb") as f:
        (tracked_computer,
         Integrity,
         NUMBER_OF_viruses,
         NUMBER_OF_DDoS,
         Number_OF_Decoders,
         Downloaded_Files,
         NUMBER_OF_BBRUTEF,
         Number_OF_MALWARES,
         Money,
         Honor,
         MAX_Integrity) = pickle.load(f)

    from function import Hostile_terminal

    result = Hostile_terminal(
        tracked_computer,
        Integrity,
        NUMBER_OF_viruses,
        NUMBER_OF_DDoS,
        Number_OF_Decoders,
        Downloaded_Files,
        NUMBER_OF_BBRUTEF,
        Number_OF_MALWARES,
        Money,
        Honor,
        MAX_Integrity
    )

    with open("hostile_save.pkl", "wb") as f:
        pickle.dump(result, f)

    sys.exit()
