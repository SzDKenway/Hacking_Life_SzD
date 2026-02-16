import random
import os
import time

import threading
import sys

from datetime import datetime

from var import *
from other import *
from function import *
from missions import *

# Check if this instance is running in hostile/hacker terminal mode
if "hostile" in sys.argv:
    # Import and run hostile terminal mode, then exit
    from hackT import run_hostile_mode
    run_hostile_mode()
    sys.exit(0)

# Normal game mode continues below
Username = ""
Command = ""
Command_Amount = 0
previus_command = ""
tracked_computer = None
paidRent = False
Current_TComp = None

print("EXE path:", sys.executable)
print("SAVE_DIR:", SAVE_DIR)
print("\n\nWelcome to the hacking simulator!")
Username = input("\nEnter your username:\n").strip().lower()
file_path = os.path.join(SAVE_DIR, f"{Username}_save.txt")
if os.path.exists(file_path):
    (Username, Money, Honor, Integrity, MAX_Integrity, survived_days,
     Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses,
     NUMBER_OF_DDoS, Number_OF_Decoders, ranges_of_computers,
     Downloaded_Files, Hostile_EASY_additional_integrity,
     Hostile_MEDIUM_additional_integrity,
     Hostile_HARD_additional_integrity, Savings) = Load_game(Username)
    print("Save file found.")
    for i in range(3):
        print("Loading savings" + "." * (i + 1))
        time.sleep(0.5)
        clear_console()
else:
    print("No save file found.")
    time.sleep(2)

    print("\nStarting a new game...")
    time.sleep(2)

    Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings = new_game(
        Money, Honor, Integrity, MAX_Integrity, survived_days,
        Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses,
        NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files,
        ranges_of_computers,
        Hostile_EASY_additional_integrity,
        Hostile_MEDIUM_additional_integrity,
        Hostile_HARD_additional_integrity,
        Savings
    )

    Save_game(Username, Money, Honor, Integrity, MAX_Integrity, survived_days,
              Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses,
              NUMBER_OF_DDoS, Number_OF_Decoders, ranges_of_computers,
              Downloaded_Files, Hostile_EASY_additional_integrity,
              Hostile_MEDIUM_additional_integrity,
              Hostile_HARD_additional_integrity, Savings)
computers = pre_work(ranges_of_computers)
print("For suggestions type '"+ blue("info") + "'. For update info: '"+ blue("update") + "'.")
print("Be aware, the game saves ONLY when you have to pay rent (after each week in game).\nYou may receive bonus money if your hacking remains unnoticed.(You don't make a mistake or do certain things: expose files, DDOS attack...etc.)\nIf you manage to get the target killed, you can avoid them noticing your hacking.")
while Command != "exit":
    if Money <= 0:
        if Savings > 0:
            clear_console()
            Money = Savings
            Savings = 0
            print(f"{time_tag()} " + yellow("EMERGENCY money transfer due the the lack of money."))
        else:
            clear_console()
            print("You have run out of money! Game over.")
            time.sleep(6)
            clear_console()
            Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings = new_game(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings)
            print("New game started!\n\nSaving RECCOMENDED.")
            break
    elif Integrity <= 500:
        clear_console()
        print(f"{time_tag()} " + yellow("CRITICAL integrity level!"))
    elif Integrity <= 0:
        clear_console()
        print("Your Integrity has reached 0! Game over.")
        time.sleep(6)
        clear_console()
        Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings = new_game(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings)
        print("New game started!\n\nSaving RECCOMENDED.")
        break
    Money = round(Money)
    print("\n--------------------------------------------\n" + yellow(f"Survived Days: {survived_days}\n"))
    if tracked_computer != None:
        print("CURRENTLY TRACKED PC:\n- " + blue(tracked_computer.UserName)+ "/" +blue(tracked_computer.contract_Type)+ "/" + yellow(tracked_computer.Comp_Integrity)+ "/" + green(f"{tracked_computer.payment}$"))
        print("(name/mission/integrity/money)\n\n")
    elif tracked_computer == None:
        print(f"CURRENTLY TRACKED PC:\n- " + blue("NONE"))
        print("(name/mission/integrity/money)\n\n")
    if Command in ["buy", "work", "nmap", "hack", "malware", "fix", "savings", "profile"]:
        Savings = Savings_Holder(Savings)
    print(blue(f"{Username.upper()}'s PC")+"\n\nOwn integrity: "+blue(Integrity)+"\nBank Account: "+blue(Money)+"$\n--------------------------------------------")
    Command = input("\nCommand: ").strip().lower()
    if Command in ["shop", "buy", "work", "nmap", "hack", "malware", "fix", "savings", "tracks", "profile"]: 
        Command_Amount += 1
    if Command_Amount > 1 and Command_Amount % 10 == 0:
        survived_days += 1
        paidRent = False
        (Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity) = add_Hostile_integrity(Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, survived_days)
    if Command == "new game":
        Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings = new_game(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings)
        print("New game started!\n\nSaving RECCOMENDED.")
    elif Command == "profile":
        tracked_computer = Profile(tracked_computer)
    elif Command == "stats":
        Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Savings = stats(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Savings)
    elif Command == "savings":
        (Money, Savings) = Transfer_Savings_Money(Money, Savings)
    elif Command == "shop":
        shop(Money, Integrity, Cost_MALWARES, Cost_BBRUTEF, Cost_viruses, Cost_DDoS, Cost_Decoders, Cost_little_integrity, Cost_big_integrity, Cost_Range)
    elif Command == "buy":
        (Money, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Integrity, MAX_Integrity, ranges_of_computers) = buy(Money, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Integrity, MAX_Integrity, ranges_of_computers, Cost_MALWARES, Cost_BBRUTEF, Cost_viruses, Cost_DDoS, Cost_Decoders, Cost_little_integrity, Cost_big_integrity, Cost_Range)
    elif Command == "work":
        (computers, Money) = Work(ranges_of_computers, Money)
    elif Command == "tracks":
        computers = ShowPCs(computers)
    elif Command == "clear":
        clear_console()
    elif Command == "update":
        updateInfo()
    elif Command == "pro mode":
        Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings = pro_game_MOD(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings)
    elif Command == "save":
        Save_game(Username,Money,Honor,Integrity,MAX_Integrity,survived_days,Number_OF_MALWARES,NUMBER_OF_BBRUTEF,NUMBER_OF_viruses,NUMBER_OF_DDoS,Number_OF_Decoders,ranges_of_computers,Downloaded_Files,Hostile_EASY_additional_integrity,Hostile_MEDIUM_additional_integrity,Hostile_HARD_additional_integrity, Savings)
    elif Command == "fix":
        (Money, Integrity, survived_days) = fix(Money, Integrity, MAX_Integrity, survived_days)
    elif survived_days % 7 == 0 and survived_days != 0 and paidRent == False:
        Money = rent_payment(Money, survived_days, ranges_of_computers)
        paidRent = True
        Save_game(Username,Money,Honor,Integrity,MAX_Integrity,survived_days,Number_OF_MALWARES,NUMBER_OF_BBRUTEF,NUMBER_OF_viruses,NUMBER_OF_DDoS,Number_OF_Decoders,ranges_of_computers,Downloaded_Files,Hostile_EASY_additional_integrity,Hostile_MEDIUM_additional_integrity,Hostile_HARD_additional_integrity, Savings)
    elif Honor <= 0 and survived_days % 2 == 0 and Command not in ["info", "save", "stats", "clear", "exit"]:
       (Money, Honor, Integrity) = hack_attack(Money, Honor, Integrity, survived_days)
    elif Command == "nmap":
        tracked_computer = track(computers)
        Current_TComp = tracked_computer
    elif Command in ["hack", "malware"]:
        if tracked_computer is not None:
            if tracked_computer.Comp_Integrity <= 0:
                print("This computer has already been destroyed. Please track a new computer.")
                continue
            if Command == "hack":
                (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity) = hack(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity)
            elif Command == "malware":
                (tracked_computer, Number_OF_MALWARES, Integrity) = send_malware(tracked_computer, Number_OF_MALWARES, Integrity)
            for i, pc in enumerate(computers):
                if pc.IP == tracked_computer.IP:
                    computers[i] = tracked_computer
                    break
            (tracked_computer, Money) = Money_Drain(tracked_computer, Money)
            (tracked_computer, Money) = Assassination(tracked_computer, Money)
        else:
            print(yellow("You need to track a computer first!"))
    elif Command == "exit":
        clear_console()
        print(f"Exiting the game. Goodbye {Username}!")
        print(blue("\nGame developed by SzDKenway."))
    elif Command == "info":
        info()
    else:
        print(red("Unknown command. Please try again."))
    previus_command= Command

    if tracked_computer is None and Current_TComp is not None:
        tracked_computer = Current_TComp
    (tracked_computer, Money, Integrity) = Profile_Mission(tracked_computer, Money, Integrity)
    (tracked_computer, Money, Downloaded_Files) = Data_Theft(tracked_computer, Money, Downloaded_Files)
    (tracked_computer, Honor, Money, Downloaded_Files) = Expose_Confidential_Information(tracked_computer, Honor, Money, Downloaded_Files)
    (tracked_computer, Money) = Sneaky_Bonus(tracked_computer, Money)
