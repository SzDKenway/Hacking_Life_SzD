import random
import os
import time

import threading  # Ez a modul lehetővé teszi több szál (thread) indítását, párhuzamosan futó feladatokhoz
import sys

from datetime import datetime


#---------------------------------------------------------------------
from var import *
from other import *
from missions import *
import subprocess

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def hack(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
         Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
         Number_OF_MALWARES, Money, Honor, MAX_Integrity):

    Chose = ""
    success = False

    choice = input("\nAre you sure you want to hack this computer? (y/n): ").strip().lower()
    while choice not in ['y', 'n']:
        choice = input(red("Invalid input. Please enter 'y' or 'n': ")).strip().lower()

    if choice == 'y':
        clear_console()

        for i in range(6):
            if i == 1:
                print(f"{time_tag()} Attempting to hack {tracked_computer.UserName}'s computer...")
                time.sleep(1)
            elif i == 2:
                print(f"\nTarget PC: {tracked_computer.IP}\n")
                time.sleep(1)
            elif i == 3:
                print(f"{time_tag()} Initiating remote connection...")
            elif i == 4:
                print(f"\n{time_tag()} Bypassing firewall...")
                time.sleep(2)

        if Integrity * 1.2 > tracked_computer.Comp_Integrity:
            while Chose not in ["y", "n", "back"]:
                Chose = input(
                    f"\nDo you want to crack the password MANUALLY?\n"
                    f" - 'y' = manual cracking\n"
                    f" - 'n' = use BruteForce (Current amount: {NUMBER_OF_BBRUTEF})\n"
                    f" - 'back' = Cancel\n\nCONFIRM: "
                ).strip().lower()

                # ===== MANUAL CRACK =====
                if Chose == "y":
                    if PassWord(tracked_computer, Integrity):
                        success = True
                        clear_console()

                        print(green("Password CRACKED."))
                        print(green("Firewall Penetrated."))
                        print(green("Remote access GRANTED."))
                        time.sleep(1)

                        print("\nOpening HACKER terminal...\n")

                        from hackT import run_hacker_terminal

                        (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                         Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                         Number_OF_MALWARES, Money, Honor, MAX_Integrity) = run_hacker_terminal(
                            tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                            Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                            Number_OF_MALWARES, Money, Honor, MAX_Integrity
                        )

                        clear_console()
                        print("Exiting HACKER terminal...")
                        time.sleep(1.5)

                        return (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                                Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                                Number_OF_MALWARES, Money, Honor, MAX_Integrity)

                    else:
                        print(yellow("You FAILED to crack the password"))
                        print(yellow("Access DENIED"))

                # ===== BRUTEFORCE =====
                elif Chose == "n":
                    if NUMBER_OF_BBRUTEF <= 0:
                        print(yellow("You don't have any BruteForce programs left."))
                        time.sleep(1)
                        continue

                    NUMBER_OF_BBRUTEF -= 1
                    success = True
                    clear_console()

                    print(f"Target IP: {tracked_computer.IP}")
                    print(f"{time_tag()} Running bruteforce.exe...")
                    time.sleep(2)

                    if tracked_computer.Comp_Integrity * 1.5 <= Integrity:
                        print(green("Password CRACKED."))
                        print(green("Firewall Penetrated."))
                        print(green("Remote access GRANTED."))
                        time.sleep(1)

                        print("\nOpening HACKER terminal...\n")

                        from hackT import run_hacker_terminal

                        (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                         Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                         Number_OF_MALWARES, Money, Honor, MAX_Integrity) = run_hacker_terminal(
                            tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                            Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                            Number_OF_MALWARES, Money, Honor, MAX_Integrity
                        )

                        clear_console()
                        print("Exiting HACKER terminal...")
                        time.sleep(1.5)

                    else:
                        tracked_computer.NoticeHacking = True
                        Integrity -= random.randint(1, 5) * 100
                        print(yellow("BRUTEFORCE failed"))
                        print(yellow("Intrusion DETECTED!"))

                    return (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
                            Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
                            Number_OF_MALWARES, Money, Honor, MAX_Integrity)

                elif Chose == "back":
                    print("Password cracking was cancelled.")
                    break

        else:
            print(yellow("Hacking failed. Target PC integrity too high."))
            tracked_computer.NoticeHacking = True

    else:
        print("HACKING was cancelled.")

    return (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS,
            Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF,
            Number_OF_MALWARES, Money, Honor, MAX_Integrity)


def chance(percent: float) -> bool:
   return random.random() < (percent / 100)

def time_tag():
    return datetime.now().strftime("[%H:%M:%S]")
#---------------------------------------------------------------------

def Transfer_Savings_Money(Money, Savings):
    clear_console()
    choice = ""
    Amount = 0
    while choice != "back":
        print(f"Money: {Money}$\nSavings: {Savings}$")
        choice = input("Would you like to transfer to ('t', Money => Savings) or withdraw ('w', Savings => Money) Savings? (or 'back' if you finished)\n\nANSWER: ").strip().lower()
        if choice == "t":
            while True:
                try:
                    Amount = int(input("Enter the Amount: "))
                    Money -= Amount
                    Savings += Amount
                    print(f"You have TRANSFERRED {Amount}$ to your Savings.")
                    time.sleep(2)
                    clear_console()
                    break
                except ValueError:
                    print(red("Please enter a valid number."))
                    continue
        elif choice == "w":
            while True:
                try:
                    Amount = int(input("Enter the Amount: "))
                    Savings -= Amount
                    Money += Amount
                    print(f"You have WITHDRAWED {Amount}$ from your Savings.")
                    time.sleep(2)
                    clear_console()
                    break
                except ValueError:
                    print(red("Please enter a valid number."))
                    continue
        elif choice == "back":
            print("Exiting Saving management...")
            clear_console()
        else:
            print(red("Invalid command.\n"))
    return Money, Savings

def info():
    print("Every 10 command equals to 1 day. By every 2 day others computers' Integrity have a low chance to get better but by every 5 day they have a higher chance to be upgraded.\nIf your Integrity/Money and savings reaches 0 you lose the game.\nYou have to pay rent after each week and that's when the game saves automatically.\nIf your Honor reaches below 0 you will have problems.\nYou can earn money by completing contracts from hacked computers. Every contract can be completed once you quitted the hostile terminal.\nYou can buy tools from the dark web to help you hack computers.\nIf you kill the tracked target your hacking less likely to be noticed.\n\nMISSION TYPES: \n- Data Theft: Download and send important file(s) from the target computer and SEND them.\n- 'Identity Theft' - Change the username of the target without hacking them.\n- Expose Confidential Information: Download and expose important files from the target computer.\n- Virus Installation - you need to install the desired amount of viruses\n- Drain Money: Hack into the target's bank account and steal money.\n- Assassination: Locate the target user and send their coordinates to an assassin (costs Honor).\n- 'CyberPunking' - (Expose all important files, Install virus)\n- 'Cyber Attack' - (Integrity need to decrease to 0, send all important files)\n- 'Zero Day Protocol' - (Drain Money, Assassination)\n- 'Delete ALL files' - You must delete ALL files from the Target's PC.\n\nCOMMANDS:\n- 'new game' - start a new game\n- 'stats' - check your stats\n- 'shop' - view items available for purchase on the dark web\n- 'buy' - buy items from the dark web\n- 'work' - find new computer(s) to hack or the refresh the list.\n- 'profile' - Change the name of the tracked target.\n- 'tracks' - show the already found computer(s)\n- 'nmap' - track a specific computer by its IP address\n- 'hack' - attempt to hack a tracked computer\n- 'malware' - install malware on a tracked computer\n- 'fix' - repair your own computer's integrity\n- 'clear' - clear the console screen\n- 'pro mode' - activate pro mode for advanced gameplay features\n- 'exit' - exit the game,\n- 'save' - save game\n- 'savings' - manage savings (betting system randomly)")

def info2():
    print("COMMANDS: \n- 'install' - install virus\n- 'stats' - Own stats\n- 'scan' - check current pc's stats\n- 'bank' - drains bank account\n- 'files' - download a file\n- 'locate' - Track & reveal position to the assassin\n- 'quit' - exit the terminal\n- 'cook' - start a DDoS attack\n\nAFTER downloading files:\n- 'expose' - Expose a file\n- 'send' - Send a file\n- 'sell' - Sell downloaded files\n")

def updateInfo():
    print("new commands: (own terminal commands) 'nmap' and 'tracks'.Money also appears in currenctly tracked line.")

def stats(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Savings):
    clear_console()
    rent = 10000*(survived_days/7)
    taxes = Money*random.randint(1,25)*0.01
    bonus = ranges_of_computers*5000
    full = rent + taxes + bonus
    full = round(full)
    print(f"Honor: {Honor}\nYour Current Integrity: {Integrity} (MAX: {MAX_Integrity})\nNumber of MALWARES: {Number_OF_MALWARES}\nNumber of BRUTEFORCE programs: {NUMBER_OF_BBRUTEF}\nNumber of viruses: {NUMBER_OF_viruses}\nNumber of DDoS programs: {NUMBER_OF_DDoS}\nNumber of Decoders: {Number_OF_Decoders}\nFiles: {[file.name for file in Downloaded_Files]}\nRanges of computers: {ranges_of_computers}\nCurrent savings: {Savings}\n\n" +yellow(f"Estimated rent: {full}$"))
    return Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Savings

def stats2(Money, Honor, Integrity, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders):
    print(f"\nMoney: {Money}\nHonor: {Honor}\nIntegrity: {Integrity}\nNumber_OF_MALWARES: {Number_OF_MALWARES}\nNUMBER_OF_BBRUTEF: {NUMBER_OF_BBRUTEF}\nNUMBER_OF_viruses: {NUMBER_OF_viruses}\nNUMBER_OF_DDoS: {NUMBER_OF_DDoS}\nNumber_OF_Decoders: {Number_OF_Decoders}\n\n")
    return Money, Honor, Integrity, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders

# Commands-----------------------------------------------------------------------------------------------------

def fix(Money, Integrity, MAX_Integrity, survived_days):
    clear_console()
    choice= ""
    damage = False
    damage_amount = 0
    days_gone = 0
    cost= 0
    for i in range(3):
        clear_console()
        print(f"Scanning own system for errors" + "."*i)
        time.sleep(1)
    if MAX_Integrity > Integrity:
        damage = True
        damage_amount = MAX_Integrity-Integrity
        cost = damage_amount*10
        days_gone = damage_amount // 200
        print(yellow("Damage(s) FOUND.\n"))
        print(f"Damage: {damage_amount}\nCost to fix it: {cost}\nAmount of time needed: {days_gone}")
        while choice not in ["y", "n"]:
            choice = input("Do you want to start to fix the system? (y/n)\nConfirm: ")
            if choice == "y":
                if Money < cost:
                    print("You don't have enough money for fixing")
                    return Money, Integrity, survived_days
                Money -= cost
                survived_days += days_gone
                clear_console()
                for y in range(4):
                    clear_console()
                    print(f" Fixing in progress" + "."*y)
                    if y == 1:
                        print(f"\n{time_tag()} Searching for damage in the system...")
                    if y == 2:
                        print(f"\n{time_tag()} Repairing damaged files...")
                    if y == 3:
                        print(f"\n{time_tag()} " + green(f"Fixing finished."))
                        time.sleep(1)
                    time.sleep(1.2)
                Integrity = MAX_Integrity
                damage = False
            elif choice == "n":
                print("Fixing has been cancelled.")
            else:
                print(red("Invalid answer.\n"))
    else:
        print(green("\nNo Damage in the system."))
    return Money, Integrity, survived_days

def shop(Money, Integrity, Cost_MALWARES, Cost_BBRUTEF, Cost_viruses, Cost_DDoS, Cost_Decoders, Cost_little_integrity, Cost_big_integrity, Cost_Range):
    clear_console()
    print(
        f"Items for sale:\n"
        f"'malware' - MALWARES (get into the computer) - {Cost_MALWARES}$ each\n"
        f"'bruteforce' - BRUTEFORCE programs (hack the computer, and bank account) - {Cost_BBRUTEF}$ each\n"
        f"'virus' - Viruses (Weakening the computer) - {Cost_viruses}$ each\n"
        f"'ddos' - DDoS programs (Crash the computer) - {Cost_DDoS}$ each\n"
        f"'decoder' - Decoders (Decrypt the files) - {Cost_Decoders}$ each\n"
        f"'little integrity' - Little Integrity (+50 Integrity) - {Cost_little_integrity}$ each\n"
        f"'big integrity' - Big Integrity (+100 Integrity) - {Cost_big_integrity}$ each\n"
        f"'range' - Ranges of computers (+1 range of computers) - {Cost_Range}$ each\n\n"
    )
    print(f"Use '"+blue("buy")+"' command to buy an item")

def buy(Money, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Integrity, MAX_Integrity, ranges_of_computers, Cost_MALWARES, Cost_BBRUTEF, Cost_viruses, Cost_DDoS, Cost_Decoders, Cost_little_integrity, Cost_big_integrity, Cost_Range):

    All_items = ["malware", "bruteforce", "virus", "ddos", "decoder",
                 "little integrity", "big integrity", "range"]

    while True:
        print("\nwelcome to the DARKWEB.\nEnter the item's name or type 'back' if you don't want to purchase anything.")
        Chosen_item = input("Item name: ").strip().lower()

        if Chosen_item == "back":
            print("Leaving the shop...")
            return (Money, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Integrity, MAX_Integrity, ranges_of_computers)

        if Chosen_item not in All_items:
            print(red("Invalid item name. Please choose again at the shop."))
            continue  # restart loop

        try:
            Chosen_amount = int(input("Amount: "))
            if Chosen_amount <= 0:
                print(red("Please enter a positive number."))
                continue
        except ValueError:
            print(red("Please enter a valid number."))
            continue

        # Pick correct cost
        if Chosen_item == "malware":
            Current_cost = Cost_MALWARES
        elif Chosen_item == "bruteforce":
            Current_cost = Cost_BBRUTEF
        elif Chosen_item == "virus":
            Current_cost = Cost_viruses
        elif Chosen_item == "ddos":
            Current_cost = Cost_DDoS
        elif Chosen_item == "decoder":
            Current_cost = Cost_Decoders
        elif Chosen_item == "little integrity":
            Current_cost = Cost_little_integrity
        elif Chosen_item == "big integrity":
            Current_cost = Cost_big_integrity
        elif Chosen_item == "range":
            Current_cost = Cost_Range

        transaction = Current_cost * Chosen_amount

        if Money < transaction:
            print(red("You don't have enough money!"))
            time.sleep(2)
            continue  # don’t deduct, let them try again

        # Deduct money
        Money -= transaction
        clear_console()
        # Apply purchase
        if Chosen_item == "malware":
            Number_OF_MALWARES += Chosen_amount
        elif Chosen_item == "bruteforce":
            NUMBER_OF_BBRUTEF += Chosen_amount
        elif Chosen_item == "virus":
            NUMBER_OF_viruses += Chosen_amount
        elif Chosen_item == "ddos":
            NUMBER_OF_DDoS += Chosen_amount
        elif Chosen_item == "decoder":
            Number_OF_Decoders += Chosen_amount
        elif Chosen_item == "little integrity":
            Integrity += 50 * Chosen_amount
            MAX_Integrity += 50 * Chosen_amount
        elif Chosen_item == "big integrity":
            Integrity += 100 * Chosen_amount
            MAX_Integrity += 100 * Chosen_amount
        elif Chosen_item == "range":
            ranges_of_computers += Chosen_amount
            print("Router upgraded. You can now access more computers.")

        print(f"\n{time_tag()} " + green(f"Transaction completed!\n"))
        print(f"You bought {Chosen_amount} {Chosen_item}(s) for {transaction}$.\n")

        return (Money, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Integrity, MAX_Integrity, ranges_of_computers)

#[work] list 5 computer-----------------------------------------------------------
def Work(ranges_of_computers, Money):
    n = ranges_of_computers
    fee = 100*n
    clear_console()
    computers = [Computer() for _ in range(n)]

    if len(computers) >= 2 and Money < fee:
        print(red("Scanning impossible due to the lack of money."))
        return computers, Money

    print("\n=== List of computers to hack ===\n")
    for i, c in enumerate(computers, start=1):
        print(
            green(f"Computer {i}:\n")+
            f"  IP Address: {c.IP}\n"
            f"  UserName: {c.UserName}")
        if c.contract_Type in ['Virus Installation', 'CyberPunking']:
            print(f"  Mission: "+ blue(f"{c.contract_Type}"))
            print(f"  Desired viruses amount to install: {c.virus_count}")
        else:
            print(f"  Mission: "+blue((f"{c.contract_Type}")))
        if c.IsDone == True:
            print("  Mission Status: " + green("COMPLETED\n"))
        else:
            print("  Mission Status: " + yellow("not completed\n"))

    if len(computers) >= 2:
        Money -= fee
        print(yellow(f"Searching fee: {fee}$.") + f" Your current amount of money: {Money}")
    else:
        print("If your range is bigger than 1, you will pay fee for each scanning. (when the command = 'work')")
    print("\nUse '"+blue("nmap") + "' to target a computer and to find out more information. Use '" + blue("map") + "' to recall this list.")
    
    return computers, Money

def ShowPCs(computers):
    clear_console()
    print("\n=== List of computers to hack ===\n")
    for i, c in enumerate(computers, start=1):
        print(
            green(f"Computer {i}:\n")+
            f"  IP Address: {getattr(c, 'IP', 'N/A')}\n"
            f"  UserName: {getattr(c, 'UserName', 'N/A')}")
        if c.contract_Type in ['Virus Installation', 'CyberPunking']:
            print(f"  Mission: " + (blue(f"{c.contract_Type}")))
            print(f"  Desired viruses amount to install: {getattr(c, 'virus_count', 0)}")
        else:
            print(f"  Mission: " + blue(getattr(c, 'contract_Type', 'N/A')))
        if c.IsDone == True:
            print("  Mission Status: " + green("COMPLETED\n"))
        else:
            print("  Mission Status: " + yellow("not completed\n"))
    print("\nUse '"+blue("nmap") + "' to target a computer and to find out more information. Use '" + blue("work") + "' to refresh this list.")
    return computers

def pre_work(ranges_of_computers):
    n = ranges_of_computers
    clear_console()
    computers = [Computer() for _ in range(n)]

    for i in range(3):
        print("Please wait")
        print("Loading computers for tracking" + "." * (i + 1))
        time.sleep(0.5)
        clear_console()
    return computers

def track(computers):
    if len(computers) == 1:
        tracked_computer = computers[0]
        for i in range(3):
            clear_console()
            print(f"Tracking IP: {tracked_computer.IP}" + "." * (i + 1))
            time.sleep(1)

        print(f"\nTRACKING was successful.\n\nOwner: {tracked_computer.UserName}.")
        time.sleep(1)
        print(f"Mission: " + blue(tracked_computer.contract_Type))
        if tracked_computer.contract_Type == 'Virus Installation':
            print(f"Desired amount of installed viruses: {tracked_computer.virus_count}")
        print(f"Payment: {tracked_computer.payment}$")
        time.sleep(1)
        print(f"Current Integrity: {tracked_computer.Comp_Integrity}.\nBanking data: {tracked_computer.Banking}$.\nFiles on the computer: {[file.name for file in tracked_computer.files]}\n")
        print(blue("\nHint:") + " write '"+ blue("hack") + "' to start hacking, '" + blue("malware") + "' to weaken their system or '" + blue("profile") + "' to search Public Database about the target.\n")
        tracked_computer.BonusGiven = False
        time.sleep(1)
        return tracked_computer
    else:
        while True:
            try:
                choice = int(input(f"Select a computer to track (1-{len(computers)}): "))
                if 1 <= choice <= len(computers):
                    tracked_computer = computers[choice - 1]

                    for i in range(3):
                        clear_console()
                        print(f"Tracking IP: {tracked_computer.IP}" + "." * (i + 1))
                        time.sleep(1)

                    for i in range(3):
                        if i == 0:
                            print(f"\nTRACKING was successful.\n\nYou have tracked " + green(f"Computer {choice}") + f".\n\nOwner: {tracked_computer.UserName}.")
                            time.sleep(1)
                        if i == 1:
                            print(f"Mission: " + blue(tracked_computer.contract_Type))
                            if tracked_computer.contract_Type == 'Virus Installation':
                                print(f"Desired amount of installed viruses: {tracked_computer.virus_count}")
                            print(f"Payment: "+ green(f"{tracked_computer.payment}$"))
                            time.sleep(1)
                        if i == 2:
                            print(yellow(f"Current Integrity: {tracked_computer.Comp_Integrity}"))
                            print(f"Banking data: {tracked_computer.Banking}$")
                            print(f"Files on the computer: {[file.name for file in tracked_computer.files]}\n")
                            time.sleep(1)
                    print(blue("\nHint:") + " write '"+ blue("hack") + "' to start hacking, '" + blue("malware") + "' to weaken their system or '" + blue("profile") + "' to search Public Database about the target.\n")
                    tracked_computer.BonusGiven = False
                    return tracked_computer
                else:
                    print(red(f"Please enter a number between 1 and {len(computers)}."))
            except ValueError:
                print(red("Invalid input. Please enter a number."))

def Profile(tracked_computer):
    Newname= ""
    WholeName = []
    for y in range(2):
        clear_console()
        if y == 0:
            print(f"{time_tag()} Overwritting Public Data...\n")
        if y == 1:
            print(f"{time_tag()} Searhing the database for Target...\n")
        time.sleep(1.5)
    if tracked_computer.difficulty_level == "Easy":
        print(f"{time_tag()} " + green(f"Match Found.\n "))
        while True:
            print(f"\n----------------------\nPublic Database\n----------------------")
            for i in range(1, 2):
                clear_console()
                print(f"Current name of the Target: {tracked_computer.UserName}\nCurrent Name: {WholeName}")
                Newname = input(f"write 'quit' for quitting the database.\nGive me the user new {i}. name:\n")
                WholeName.append(Newname)
            FullName = " ".join(WholeName)

            if FullName != tracked_computer.UserName and len(WholeName) == 2:
                tracked_computer.UserName = FullName
                tracked_computer.NameChanged = True
                print(green("\nName has been overwritten successfully."))
                time.sleep(1.5)
                clear_console()
                break

            elif FullName == tracked_computer.UserName and len(WholeName) == 2:
                print(red("\nYou have to change the name."))
                time.sleep(1.5)

            if Newname == 'quit' or ('quit' in WholeName):
                print("\nQuitting the Public Database...")
                time.sleep(1.5)
                clear_console()
                break
    else:
        print(f"{time_tag()} " + red(f"No match found in the Public Database."))
    # Return the (possibly modified) tracked_computer so callers keep the updated object
    return tracked_computer

def send_malware(tracked_computer, Number_OF_MALWARES, Integrity):
    Amount = 0
    success = False
    clear_console()
    choice = input(f"Are you sure you want to send malware to this computer?\n(Tracked computer's Integrity: {tracked_computer.Comp_Integrity}, your current Malware amount: {Number_OF_MALWARES}) (y/n): ").strip().lower()
    while choice not in ['y', 'n']:
        choice = input(red("Invalid input. Please enter 'y' or 'n': ")).strip().lower()

    if choice == 'y':
        clear_console()
        for i in range(6):
            print(f"{time_tag()} Sending malware" + "." * (i + 1))
            if i >= 2:
                print(f"\nTarget pc: {tracked_computer.IP}")
            if i == 3:
                print(f"\nCurrent Integrity of the target: {tracked_computer.Comp_Integrity}")
            if i == 4:
                print(f"\n{time_tag()} Forging CLICKBAIT message...")
            if i == 5:
                if Number_OF_MALWARES > 0:
                    Number_OF_MALWARES -= 1
                    if tracked_computer.difficulty_level == 'Easy':
                        if chance(90):
                            print(green("Malware successfully sent!"))
                            Amount = random.randint(1, 3)*100
                            tracked_computer.Comp_Integrity -= Amount
                            success = True
                        else:
                            print(yellow("Malware failed to send."))
                            success = False
                    elif tracked_computer.difficulty_level == 'Medium':
                        if chance(85):
                            print(green("Malware successfully sent!"))
                            Amount = random.randint(2, 7)*100
                            tracked_computer.Comp_Integrity -= Amount
                            success = True
                        else:
                            print(yellow("Malware failed to send."))
                            success = False
                    elif tracked_computer.difficulty_level == 'Hard':
                        if chance(75):
                            print(green("Malware successfully sent!"))
                            Amount = random.randint(3, 9)*100
                            tracked_computer.Comp_Integrity -= Amount
                            success = True
                        else:
                            print(yellow("Malware failed to send."))
                            success = False
                else:
                    print(red("You don't have Malware."))
            time.sleep(1)
            clear_console()
        if success:
            print(f"{time_tag()} " + green(f"SENDING MALWARE was successful.\nYou have sent malware to {tracked_computer.UserName}'s computer! Target's integrity reduced by: {Amount}\n"))
            return tracked_computer, Number_OF_MALWARES, Integrity
        else:
            print(yellow("SENDING MALWARE failed."))
            if tracked_computer.Located != True:
                tracked_computer.NoticeHacking = True
            Integrity -= random.randint(1,5)*100
            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
            print(yellow("Your pc has been damaged by the counter programs.\n"))
            return tracked_computer, Number_OF_MALWARES, Integrity

    elif choice == 'n':
        print("SENDING MALWARE was cancelled.")
        clear_console()
        return tracked_computer, Number_OF_MALWARES, Integrity
    else:
        print(red("Invalid."))

def Hostile_terminal(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity):
    hack_terminal = ""
    clear_console()
    print("Write 'info' for help.")
    while True:
        print(f"\nYou are in control of PC: {tracked_computer.IP}")
        if tracked_computer.NoticeHacking == False:
            print(f"Hacking status:"+green(" UNNOTICED"))
        else:
            print("Hacking status:"+yellow(" ALERTED"))
        print("Your current objective:"+ blue(f" {tracked_computer.contract_Type} ") + green(f"(payment: {tracked_computer.payment}$)"))
        if tracked_computer.contract_Type == 'Virus Installation':
            print(f"Desired amount of installed viruses: {tracked_computer.Virus_Installed}/{tracked_computer.virus_count}")
        if tracked_computer.Located == True:
            print(f"\n{tracked_computer.UserName} has been assassinated.")
        if tracked_computer.contract_Type == 'CyberPunking':
           (tracked_computer, Money, Downloaded_Files) = CyberPunking(tracked_computer, Money, Downloaded_Files)
        if tracked_computer.contract_Type == 'Cyber Attack':
            (tracked_computer, Money, Downloaded_Files) = Cyber_Attack(tracked_computer, Money, Downloaded_Files)
        if tracked_computer.contract_Type == 'Zero Day protocol':
            (tracked_computer, Money) = Zero_Day_Protocol(tracked_computer, Money)
        if tracked_computer.contract_Type == 'Delete ALL files':
            (tracked_computer, Money) = Delete_Files_Mission(tracked_computer, Money, Downloaded_Files)
        print(f"\n----------------------\n{tracked_computer.UserName}'s Computer\n----------------------")
        hack_terminal = input("\nhacker terminal: ")
        if hack_terminal == "info":
            info2()
        elif hack_terminal == "sell":
            if tracked_computer.contract_Type not in ['CyberPunking', 'Cyber Attack']:
                (Downloaded_Files, Money) = sell_files(Downloaded_Files, Money)
            elif not Downloaded_Files:
                print("You have no more files to sell.\n")
                time.sleep(1.2)
            else:
                clear_console()
                print("You cannot sell this files.\n")
        elif hack_terminal == "stats":
            (Money, Honor, Integrity, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders) = stats2(Money, Honor, Integrity, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders)
        elif hack_terminal == "scan":
            Hostile_terminal_stats(tracked_computer)
        elif hack_terminal == "install":
            (tracked_computer, NUMBER_OF_viruses) = virus_install(tracked_computer, NUMBER_OF_viruses)
            if tracked_computer.contract_Type == 'Virus Installation':
                (tracked_computer, Money) = Virus_Mission(tracked_computer, Money)
        elif hack_terminal == "bank":
            (tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor) = deposit_money(tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor, Integrity)
        elif hack_terminal == "ping":
            if tracked_computer.Located == True:
                clear_console()
                print("Target is already assasinated.\n")
            else:
                (tracked_computer, Honor) = Locate(tracked_computer, Honor)
        elif hack_terminal == "expose":
            (tracked_computer, Downloaded_Files, Money, Honor) = Expose_files(tracked_computer, Downloaded_Files, Money, Honor)
        elif hack_terminal == "send":
            (tracked_computer, Downloaded_Files, Money) = Send_files(tracked_computer, Downloaded_Files, Money)
        elif hack_terminal == "cook":
            if Downloaded_Files != []:
                clear_console()
                print(red("You have to deal with the downloaded files before quitting.\n"))
            else:
                (tracked_computer, NUMBER_OF_DDoS, Integrity, Money) = DDoS_attack(tracked_computer, NUMBER_OF_DDoS, Integrity, Money)
                if tracked_computer.Comp_Integrity <= 0:
                    print(f"Quitting {tracked_computer.UserName}'s computer...")
                    clear_console()
                    return tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity
        elif hack_terminal == "files":
            (tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity) = download_files_menu(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity)
        elif hack_terminal == "quit":
            if Downloaded_Files != []:
                clear_console()
                print(red("You have to deal with the downloaded files before quitting.\n"))
            else:
                print(f"Quitting {tracked_computer.UserName}'s computer...")
                clear_console()
                return tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity
        else:
            print(red("Invalid command.\n"))

def download_files_menu(tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity):
    while True:
        clear_console()
        print(f"Files on {tracked_computer.UserName}'s PC (Downloaded: {len(Downloaded_Files)})\n")
        for idx, f in enumerate(tracked_computer.files, start=1):
            status = ["DECRYPTED"] if getattr(f, "DECRYPTED", False) else ["CRYPTED"]
            print(f"{idx}. {f.name} [{' / '.join(status)}]")

        choice = input("\nEnter the number of the file to download (or 'back'): ").strip().lower()

        if choice == "back":
            clear_console()
            return tracked_computer, Integrity, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, NUMBER_OF_BBRUTEF, Number_OF_MALWARES, Money, Honor, MAX_Integrity

        try:
            idx = int(choice)
        except ValueError:
            print(red("Invalid input. Please enter a number or 'back'."))
            time.sleep(1.2)
            continue

        if idx < 1 or idx > len(tracked_computer.files):
            print(red("Invalid file number."))
            time.sleep(1.2)
            continue

        f = tracked_computer.files[idx - 1]

        if f.kind == "bonus":
            # ha dekódolt, kiosztjuk a bónuszt és eltávolítjuk (NEM adjuk a Downloaded_Files-hez)
            if getattr(f, "DECRYPTED", False):
                bonus_type = getattr(f, "bonus_type", None)

                if bonus_type == "Decoder":
                    Number_OF_Decoders += random.randint(1, 50)
                    print(green("You received Decoder(s)!"))
                elif bonus_type == "BruteForce":
                    NUMBER_OF_BBRUTEF += random.randint(1, 30)
                    print(green("You received BruteForce(s)!"))
                elif bonus_type == "Malware":
                    Number_OF_MALWARES += random.randint(1, 25)
                    print(green("You received Malware(s)!"))
                elif bonus_type == "Virus":
                    NUMBER_OF_viruses += random.randint(1, 20)
                    print(green("You received Virus(s)!"))
                elif bonus_type == "DDoS":
                    NUMBER_OF_DDoS += random.randint(1, 10)
                    print(green("You received DDoS(s)!"))
                elif bonus_type == "Integrity":
                    Amount = random.randint(10, 100)
                    Integrity += Amount
                    MAX_Integrity += Amount
                    print(green(f"You received Integrity Patch! (+{Amount} Integrity)"))
                elif bonus_type == "Honor":
                    Honor += 20
                    print(green("You received Honor Badge! (+20 Honor)"))
                else:
                    # ha nincs bonus_type, csak értesítjük
                    print("You received an unknown bonus.")

                # töröljük a fájlt a célgépről (nem kerül Downloaded_Files-be)
                del tracked_computer.files[idx - 1]
                print(f"Bonus {f.name} has been collected and removed from the list.")
                time.sleep(1.2)
                continue

            # ha CRYPTED -> felajánljuk a dekódolást (marad a gépen ha nem dekódolod)
            decision = ""
            while decision not in ['y', 'n']:
                decision = input("\nDo you want to try to decode it now? (y/n): ").strip().lower()
                if decision == 'y':
                    if Number_OF_Decoders > 0:
                        Number_OF_Decoders -= 1
                        if chance(85):
                            f.DECRYPTED = True
                            print(f"{time_tag()} " + green(f"{f.name} has been successfully DECRYPTED."))
                        else:
                            tracked_computer.NoticeHacking = True
                            print(f"{time_tag()}" + yellow(f" Decoding {f.name} failed."))
                            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                    else:
                        print(red("You don't have any Decoders left."))
                elif decision == 'n':
                    print("Decoding cancelled.")
                else:
                    print(red("Invalid input. Please enter 'y' or 'n'."))
            time.sleep(1.2)
            continue

        # -------------------
        # DECOY fájlok kezelése
        # -------------------
        elif f.kind == "decoy":
            # minijáték: success -> nothing (optionally reward), fail -> Integrity loss
            print(f"{f.name} is a decoy file.")
            if getattr(f, "DECRYPTED", False):
                print("This decoy file was DECRYPTED — you still need to pass the challenge to safely collect info.")
            else:
                print("This is a decoy file. Protect yourself!")

            if timed_word_challenge(tracked_computer):
                print(green("You successfully countered the decoy trap."))
                # opcionális jutalom lehet itt (pl. Honor += 10) — most nem adunk automatikus jutalmat
            else:
                Rand_Amount = random.randint(2, 4)*100
                Integrity -= Rand_Amount
                tracked_computer.NoticeHacking = True
                print(yellow(f"You triggered the decoy trap! Integrity decreased by {Rand_Amount}."))
                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))

            # a decoy EGYÉRTELMŰEN eltűnik (nem kerül Downloaded_Files-be)
            del tracked_computer.files[idx - 1]
            print(f"Decoy {f.name} removed from the list.")
            time.sleep(1.2)
            continue

        # -------------------
        # IMPORTANT fájlok: ha CRYPTED -> felajánlunk dekódolást; ha már DECRYPTED -> letöltjük
        # -------------------
        if f.kind == "important":
            # Új viselkedés: csak akkor tölthető le automatikusan, ha már DECRYPTED == True.
            # Ha még CRYPTED (vagy nincs DECRYPTED attribútum), felajánljuk a dekódolást.
            if not getattr(f, "DECRYPTED", False):
                # fájl CRYPTED -> kérdezzük meg a játékost, hogy dekódolni akarja-e most
                decision = ""
                while decision not in ['y', 'n']:
                    decision = input(f"\nDo you want to try to decode it now? (y/n)\nCONFIRM: ").strip().lower()
                    if decision == 'y':
                        if Number_OF_Decoders > 0:
                            Number_OF_Decoders -= 1
                            if chance(85):
                                f.DECRYPTED = True
                                print(f"{time_tag()} " + green(f"{f.name} has been successfully DECRYPTED."))
                                time.sleep(0.8)
                                # ha sikerült dekódolni, folytatjuk lefele és ténylegesen letöltjük
                            else:
                                tracked_computer.NoticeHacking = True
                                print(f"{time_tag()}" + yellow(f" Decoding {f.name} failed."))
                                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                                time.sleep(1.2)
                                # sikertelen dekódolás esetén NEM töröljük, egyszerűen visszatérünk a menübe
                        else:
                            print(yellow("You don't have any Decoders left."))
                            time.sleep(1.2)
                    elif decision == 'n':
                        print("Decoding cancelled. The file remains on the remote machine.")
                        time.sleep(1.2)
                    else:
                        print(red("Invalid input. Please enter 'y' or 'n'."))

                # ha a felhasználó választott 'y' és a dekódolás sikeres volt, akkor a következő rész letölti
                if not getattr(f, "DECRYPTED", False):
                    # ha még mindig nincs DECRYPTED, nem töltjük le — csak folytatjuk a ciklust
                    continue

            # ha ide eljutunk, a fájl DECRYPTED == True (vagy eredetileg is az volt) -> letöltjük
            f.Downloaded = True
            Downloaded_Files.append(f)
            del tracked_computer.files[idx - 1]
            print(f"{time_tag()} Successfully downloaded {f.name}.")
            time.sleep(1.2)
            # ha szeretnéd, itt adhatsz extra feldolgozást a letöltött fájlokra
            continue

        # -------------------
        # ha ide jutunk: ismeretlen "kind" vagy fincs. Felajánljuk a dekódolást, ha kell.
        # -------------------
        if not getattr(f, "DECRYPTED", False):
            decision = ""
            while decision not in ['y', 'n']:
                clear_console()
                decision = input(f"\nDo you want to decode {f.name} now? (y/n): ").strip().lower()
                if decision == 'y':
                    if Number_OF_Decoders > 0:
                        Number_OF_Decoders -= 1
                        if chance(85):
                            f.DECRYPTED = True
                            print(f"{time_tag()} " + green(f"{f.name} has been successfully DECRYPTED."))
                        else:
                            tracked_computer.NoticeHacking = True
                            print(f"{time_tag()}" + yellow(f" Decoding {f.name} failed."))
                            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                    else:
                        print(yellow("You don't have any Decoders left."))
                elif decision == 'n':
                    print("Decoding cancelled.")
                else:
                    print(red("Invalid input. Please enter 'y' or 'n'."))
        time.sleep(1.5)

def deposit_money(tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor, Integrity):
    BruteForce = ""
    hack_counter = 0
    Original_Money = tracked_computer.Banking
    BruteForce2 = ""
    choice = ""
    clear_console()
    print(f"Accessing bank account requrires BruteForce program.\n\n Your currrent amount of BruteForces: {NUMBER_OF_BBRUTEF}")
    while BruteForce not in ['y', 'n']:
        BruteForce = input("Do you want to use a BruteForce program to access the bank account? (y/n): ").strip().lower()
        if BruteForce == 'y':
            if NUMBER_OF_BBRUTEF > 0:
                NUMBER_OF_BBRUTEF -= 1
                print(f"{time_tag()} Using BruteForce program...")
                print(f"\n{time_tag()} Running bruteforce.exe...")
            else:
                print(yellow("You don't have any BruteForce programs left."))
                return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor
        elif BruteForce == 'n':
            print("Accessing bank account cancelled.")
            return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor
        else:
            print(red("Invalid input. Please enter 'y' or 'n'."))
    clear_console()

    for i in range(3):
        print(f"{time_tag()} Accessing bank account" + "." * (i + 1))
        if i >= 2:
            print(f"\nTarget pc: {tracked_computer.IP}")
        if i == 3:
            print(f"\n{time_tag()} Collecting information about the {tracked_computer.UserName}'s bank account")
            time.sleep(1.5)    
        time.sleep(0.5)
        clear_console()

    if tracked_computer.Comp_Integrity * 1.5 > Integrity:
        print(f"{time_tag()}" + yellow(" Accessing bank account failed. Target PC's Integrity is too high."))
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
        return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor
    else:
        print(f"You are about to access {tracked_computer.UserName}'s bank account.\n\nDo you want to crack it MANUALLY or with the use of Bruteforce (y/n): ")

    def post_crack_menu():
        nonlocal Money, Honor, tracked_computer, hack_counter

        while True:
            clear_console()
            print(f"Welcome back, {tracked_computer.UserName}.\n")
            print(f"Your Account: {Money}$\n{tracked_computer.UserName}'s Account: {tracked_computer.Banking}$\n\n\nDo you want to transfer (t) or withdraw (w) money? (t/w)\nType 'quit' to exit bank terminal.")
            choice_local = input(f"\n{tracked_computer.UserName}'s banking account terminal: ").strip().lower()

            if choice_local == 'quit':
                clear_console()
                print("Exiting bank terminal...")
                time.sleep(1)
                break

            if choice_local == 't':
                try:
                    amount = int(input("Enter amount to transfer: "))
                except ValueError:
                    print("\nPlease enter a valid integer amount.")
                    time.sleep(1)
                    continue
                if amount > Money:
                    print(red("\nInsufficient funds in the target's account."))
                else:
                    tracked_computer.Banking += amount
                    Money -= amount
                    if amount > Original_Money*0.1 and hack_counter == 0 and Original_Money != 0:
                        Honor += 55
                        print(f"\nYour Honor has increased by 55.\nCurrent Honor: {Honor}")
                        choice_local = "quit"
                    print(f"\n{time_tag()} Successfully transferred {amount}$ to {tracked_computer.UserName}'s account from your account.")
                    time.sleep(3)
                    return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor

            elif choice_local == 'w':
                try:
                    amount = int(input("Enter amount to withdraw: "))
                except ValueError:
                    print(red("Please enter a valid amount."))
                    time.sleep(1)
                    continue
                if amount > tracked_computer.Banking:
                    print(red("Insufficient funds in the target's account."))
                else:
                    if tracked_computer.difficulty_level == 'Easy' and hack_counter == 0 and tracked_computer.contract_Type not in ["Drain Money", 'Zero Day protocol']:
                        Honor -= 150
                    tracked_computer.Banking -= amount
                    Money += amount
                    if tracked_computer.Located != True:
                        tracked_computer.NoticeHacking = True
                        print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                    print(f"\nSuccessfully withdrew {amount}$ from {tracked_computer.UserName}'s account to your account.")
                    time.sleep(3)

            else:
                print("Invalid input. Please enter 't' or 'w'.")
            hack_counter += 1  

    while BruteForce2 not in ['y', 'n']:
        BruteForce2 = input("\nConfirmation: ").strip().lower()
        if BruteForce2 == 'n':
            if NUMBER_OF_BBRUTEF > 0:
                NUMBER_OF_BBRUTEF -= 1
                clear_console()
                for i in range(4):
                    if i == 1:
                        print(f"Target IP: {tracked_computer.IP}")
                    if i == 2:
                        print(f"\n{time_tag()} Using BRUTEFORCE to crack {tracked_computer.UserName}'s bank password" + "."*3)
                    if i == 3:
                        print(f"\n{time_tag()} Running bruteforce.exe...")
                    time.sleep(1)
                for i in range(3):
                    if i == 1:
                        print(f"\n{time_tag()} " + green(f"You have CRACKED the password."))
                    if i == 2:
                        print(f"\n{time_tag()} " + green(f"Access to bank account GRANTED."))
                    time.sleep(1)
                post_crack_menu()  

            else:
                print(yellow("You don't have any BruteForce programs left."))
                return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor

        elif BruteForce2 == 'y':
            if PassWord(tracked_computer, Integrity) == True:
                print(f"{time_tag()} " + green(f"You have CRACKED the password."))
                print(f"\n{time_tag()} " + green(f"Access to bank account GRANTED."))
                post_crack_menu()  
            else:
                print(f"{time_tag()}" + yellow(" You FAILED to crack the password"))
                if tracked_computer.Located != True:
                    tracked_computer.NoticeHacking = True
                    print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
        else:
            print(red("Invalid input. Please enter 'y' or 'n'."))
    return tracked_computer, Money, NUMBER_OF_BBRUTEF, Honor

def virus_install(tracked_computer, NUMBER_OF_viruses):
    clear_console()
    choice = input(f"Are you sure you want to install a virus on this {tracked_computer.UserName}'s computer? (y/n): ").strip().lower()
    while choice not in ['y', 'n']:
        choice = input(red("Invalid input. Please enter 'y' or 'n': ")).strip().lower()

    if choice == 'y':
        clear_console()
        for i in range(5):
            if i == 1:
                print(f"Target pc: {tracked_computer.IP}\n")
            if i == 2:
                print(f"{time_tag()} Installing virus" + "." * 3)
            if i == 3:
                print(f"\n{time_tag()} Current Integrity of the target: {tracked_computer.Comp_Integrity}\n")
            if i == 4:
                clear_console()
                if NUMBER_OF_viruses > 0:
                    NUMBER_OF_viruses -= 1
                    if tracked_computer.difficulty_level == 'Easy':
                        if chance(90):
                            print(f"{time_tag()} " + green(f"Virus successfully installed!\n"))
                            tracked_computer.Comp_Integrity -= random.randint(1, 3)*100
                            tracked_computer.Virus_Installed += 1
                        else:
                            print(f"{time_tag()}" + yellow("Virus installation FAILED.\n"))
                            if tracked_computer.Located != True:
                                tracked_computer.NoticeHacking = True
                                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                    elif tracked_computer.difficulty_level == 'Medium':
                        if chance(80):
                            print(f"{time_tag()} " + green(f"Virus successfully installed!\n"))
                            tracked_computer.Comp_Integrity -= random.randint(2, 4)*100
                            tracked_computer.Virus_Installed += 1
                        else:
                            print(f"{time_tag()}" + yellow("Virus installation FAILED.\n"))
                            if tracked_computer.Located != True:
                                tracked_computer.NoticeHacking = True
                                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                    elif tracked_computer.difficulty_level == 'Hard':
                        if chance(75):
                            print(f"{time_tag()} " + green(f"Virus successfully installed!\n"))
                            tracked_computer.Comp_Integrity -= random.randint(3, 5)*100
                            tracked_computer.Virus_Installed += 1
                        else:
                            print(f"{time_tag()}" + yellow("Virus installation FAILED."))
                            if tracked_computer.Located != True:
                                tracked_computer.NoticeHacking = True
                                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
            time.sleep(3)
        print(f"{time_tag()} Virus INSTALLATION process COMPLETED.\nCurrent Integrity of the target: {tracked_computer.Comp_Integrity}")

    elif choice == 'n':
        print("VIRUS INSTALLATION was cancelled.")
    return tracked_computer, NUMBER_OF_viruses

def DDoS_attack(tracked_computer, NUMBER_OF_DDoS, Integrity, Money):
    clear_console()
    if Integrity < tracked_computer.Comp_Integrity * 2:
        print(f"{time_tag()}" + yellow(f" DDoS attack FAILED.\nYour Integrity ({Integrity}) is too low compared to the target's Integrity ({tracked_computer.Comp_Integrity})."))
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
        NUMBER_OF_DDoS = NUMBER_OF_DDoS - 1
        return tracked_computer, NUMBER_OF_DDoS, Integrity, Money
    print(f"Current amount of DDoS programs: {NUMBER_OF_DDoS}. It will destoy the computer entirely if successful.")
    choice = input(f"\nAre you sure you want to start a DDoS attack on this {tracked_computer.UserName}'s computer? (y/n):\n\nCONFIRM: ").strip().lower()
    while choice not in ['y', 'n']:
        choice = input(red("Invalid input. Please enter 'y' or 'n': ")).strip().lower()

    if choice == 'y':
        clear_console()
        for i in range(5):
            if i == 1:
                for d in range(10):
                    print(f"Target pc: {tracked_computer.IP}.\n\nConnecting to the remote PC's connections... ({d*10}%)")
                    time.sleep(1)
                    clear_console()
            if i == 2:
                print(f"{time_tag()} Starting DDoS attack" + "." * 3)
                time.sleep(2)
            if i == 3:
                print(f"\n{time_tag()} Overloading {tracked_computer.UserName}'s computer with traffic" + "."*3)
                print(f"{time_tag()} System response time is slowing down...")
                print(f"{time_tag()} CPU is overheating...")
                time.sleep(2)
            if i == 4:
                tracked_computer.Comp_Integrity = 0
                print(f"\n{time_tag()} " + green(f"DDoS attack successful!\n\n{tracked_computer.UserName}'s computer integrity is now {tracked_computer.Comp_Integrity}."))
                tracked_computer.NoticeHacking = True
                print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
                Money += tracked_computer.payment
                NUMBER_OF_DDoS -= 1
                tracked_computer.IsDone = True
                time.sleep(2)
            clear_console()
        print(f"\nYou earned {tracked_computer.payment}$. Your current Money: {Money}$\n")
        time.sleep(2)

    elif choice == 'n':
        print("DDoS ATTACK was cancelled.")
    else:
        print(red("Invalid input entered.\n"))
    return tracked_computer, NUMBER_OF_DDoS, Integrity, Money

def Locate(tracked_computer, Honor):
    clear_console()
    IsSuccess = HangerGame(tracked_computer, Integrity)
    if IsSuccess:
        for i in range(5):
            if i == 1:
                print(f"{time_tag()} Locating {tracked_computer.UserName} current Position" + "."*3)
                time.sleep(1)
            if i == 2:
                print(f"\n{time_tag()} Searching pc for other devices connected to the network" + "."*3+f"\n{tracked_computer.UserName}'s phone has been found.")
                time.sleep(1)
            if i == 3:
                print(f"\n{time_tag()} Pinging {tracked_computer.UserName}'s phone" + "."*3 + "\nTarget's position has been REVEALED.\nSaving coordinates...")
                time.sleep(1)
            if i == 4:
                print(f"\n{time_tag()} Sending {tracked_computer.UserName}'s coordinates to the Assassin...")
                print(f"\n{time_tag()} " + green(f"Coordinates sent successfully!"))
        tracked_computer.Located = True
        if tracked_computer.contract_Type not in [ "Assassination", 'Zero Day protocol']:
            Honor -= 300
            print(yellow('Assasination was unneccesary.'))
    else:
        print("You failed to ping other devices of the target.")
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
    time.sleep(3)
    clear_console()
    return tracked_computer, Honor
      
def Expose_files(tracked_computer, Downloaded_Files, Money, Honor):
    done = False
    clear_console()
    if tracked_computer.contract_Type not in ["Expose Confidential Information", 'CyberPunking']:
        print(red("This is not an expose contract.\n"))
        return tracked_computer, Downloaded_Files, Money, Honor
    if not Downloaded_Files:
        print("You haven't downloaded any files yet.\n")
        return tracked_computer, Downloaded_Files, Money, Honor
    while not done:
        clear_console()
        print("Downloaded files:")
        for i, f in enumerate(Downloaded_Files, start=1):
            print(f"{i}. {f.name}")
        choice = input("\nSelect a file number to expose (or type 'back' to cancel): ").strip().lower()
        if choice == "back":
            print("Expose cancelled.")
            return tracked_computer, Downloaded_Files, Money, Honor
        try:
            idx = int(choice)
        except ValueError:
            print(red("Invalid input. Please enter a valid file number or 'back'.\n"))
            time.sleep(1.2)
            continue
        if idx < 1 or idx > len(Downloaded_Files):
            print(red("Invalid file number.\n"))
            time.sleep(1.2)
            continue

        selected_file = Downloaded_Files.pop(idx - 1)
        print(f"You exposed '{selected_file.name}'. It has been removed from your downloaded files.")
        if tracked_computer.contract_Type == "Expose Confidential Information":
            Money += tracked_computer.payment
            tracked_computer.IsDone = True
            tracked_computer.NoticeHacking = True
            print(f"\n{time_tag()}" + yellow("Intrusion DETECTED!\n"))
            number = random.randint(30, 70)
            Honor += number
            time.sleep(3)
            clear_console()
            print(f"\n{time_tag()} " + green(f"{tracked_computer.payment}$ transferred to your bank account.\n"))
            print(green(f"Your Honor increased by {number}.\n"))
            time.sleep(2)
        else:
            clear_console()
        done = True

    return tracked_computer, Downloaded_Files, Money, Honor

def Send_files(tracked_computer, Downloaded_Files, Money):
    done = False
    clear_console()
    if tracked_computer.contract_Type not in ['Data Theft', 'Cyber Attack']:
        print(red("This is not an data theft contract.\n"))
        return tracked_computer, Downloaded_Files, Money
    if not Downloaded_Files:
        print("You haven't downloaded any files yet.\n")
        return tracked_computer, Downloaded_Files, Money
    while not done:
        clear_console()
        print("Downloaded files:")
        for i, f in enumerate(Downloaded_Files, start=1):
            print(f"{i}. {f.name}")
        choice = input("\nSelect a file number to send (or type 'back' to cancel): ").strip().lower()
        if choice == "back":
            print("Expose cancelled.")
            return tracked_computer, Downloaded_Files, Money
        try:
            idx = int(choice)
        except ValueError:
            print(red("Invalid input. Please enter a valid file number or 'back'.\n"))
            time.sleep(1.2)
            continue
        if idx < 1 or idx > len(Downloaded_Files):
            print(red("Invalid file number.\n"))
            time.sleep(1.2)
            continue

        selected_file = Downloaded_Files.pop(idx - 1)
        print(f"You sent '{selected_file.name} to the buyer'. It has been removed from your downloaded files.")
        if tracked_computer.contract_Type == 'Data Theft':
            Money += tracked_computer.payment
            tracked_computer.IsDone = True
            clear_console()
            print(f"\n{time_tag()} " + green(f"{tracked_computer.payment}$ transferred to your bank account.\n"))
            time.sleep(2)
        else:
            clear_console()
        done = True

    return tracked_computer, Downloaded_Files, Money

def _safe_randint(a: int, b: int) -> int:
    # Biztosítja, hogy mindig a <= b legyen a randint hívásnál.
    low = min(a, b)
    high = max(a, b)
    return random.randint(low, high)

def sell_files(Downloaded_Files, Money):
    if not Downloaded_Files:
        print("You have no files to sell.")
        return Downloaded_Files, Money

    while True:
        BetGuess = random.randint(3, 8)
        BetSellPrice = random.randint(10, 100)  # buyer eredeti kínálata (k)
        BetORIGINALPrice = BetSellPrice
        PreviousPrice = 0

        clear_console()
        print("Downloaded files:")
        for i, f in enumerate(Downloaded_Files, start=1):
            print(f"{i}. {f.name}")

        choice = input("\nSelect a file number to sell (or type 'back' to cancel): ").strip().lower()
        if choice == "back":
            clear_console()
            break

        try:
            idx = int(choice)
        except ValueError:
            print(red("Invalid input. Please enter a valid file number or 'back'.\n"))
            time.sleep(1.2)
            continue

        if idx < 1 or idx > len(Downloaded_Files):
            print(red("Invalid file number."))
            time.sleep(1.2)
            continue

        # tárgyalás
        while BetGuess > 0:
            print("\nIf you fail to negotiate the price will be RANDOM.")
            print(blue(f"\nPrevious offer: {PreviousPrice}"))
            print(f"(actual price: {PreviousPrice * 200}$)")
            print(yellow(f"\nTarget Price: {BetORIGINALPrice}"))
            print(f"(actual price: {BetORIGINALPrice * 200}$)")
            try:
                Your_Price = int(input("\nEnter your price between 1–100 (multiplied by 200): "))
            except ValueError:
                print(red("Invalid number."))
                time.sleep(1.2)
                continue

            if Your_Price > 100:
                print(red("Your price is too high (max 100)."))
                time.sleep(1.2)
                continue
            if Your_Price < 10:
                print(red("Your price is too low (min 1)."))
                time.sleep(1.2)
                continue

            # ha az ár túl magas a vevőnek (te többért adnád)
            if Your_Price > BetORIGINALPrice:
                BetGuess -= 1
                PreviousPrice = Your_Price

                # 70% eséllyel a vevő visszalép (emeli a célárat a te ajánlatod irányába),
                # 30% eséllyel lejjebb viszi a célárat (húzódik vissza).
                if chance(70):
                    # emelés: új célár valahol az eredeti és a te ajánlatod között
                    low = BetORIGINALPrice
                    high = Your_Price
                    new_target = _safe_randint(low, high)
                    BetORIGINALPrice = new_target
                    print(green(f"\nThe buyer has RAISED the target price: {BetORIGINALPrice} $.\n"))
                    time.sleep(2)
                    if BetORIGINALPrice == Your_Price:
                        print(green("Your price was accepted by the buyer."))
                        Money += Your_Price * 200
                        selected_file = Downloaded_Files.pop(idx - 1)
                        print(f"You sold '{selected_file.name}' for {Your_Price}\n(actual pirce: {Your_Price*200}$).")
                        time.sleep(1.5)
                        break
                else:
                    # csökkentés: vevő visszalép, lejjebb viszi a célárat
                    # csökkentés mértéke: véletlen 1..min(15, BetORIGINALPrice-10)
                    if BetORIGINALPrice > 10:
                        max_decrease = min(15, BetORIGINALPrice - 10)
                        decrease = random.randint(1, max(1, max_decrease))
                        BetORIGINALPrice = max(10, BetORIGINALPrice - decrease)
                    else:
                        BetORIGINALPrice = 10
                    print(yellow(f"\nThe buyer has LOWERED the target price: {BetORIGINALPrice}$.\n"))
                    time.sleep(2)

                time.sleep(1.5)
                clear_console()

            else:
                # sikeres eladás (Your_Price <= BetORIGINALPrice)
                print("Your price was accepted by the buyer.")
                Money += Your_Price * 500
                selected_file = Downloaded_Files.pop(idx - 1)
                print(f"You sold '{selected_file.name}' for {Your_Price}\n(actual price: {Your_Price*500}$).")
                time.sleep(1.5)
                break

        else:
            # ha elfogytak a próbák (BetGuess == 0)
            print("Buyer stopped negotiating. A random price will be paid.")
            if idx - 1 < len(Downloaded_Files):
                selected_file = Downloaded_Files.pop(idx - 1)
                sell_price = random.randint(1, 10) * 500
                Money += sell_price
                print(f"You sold '{selected_file.name}' for {sell_price}$.\n")
                break
            else:
                # védelem, ha közben megváltozott a lista hossza
                print("Something went wrong: selected file no longer exists.")
            time.sleep(1.5)

    return Downloaded_Files, Money

def hack_attack(Money, Honor, Integrity, survived_days):
    clear_console()
    print(f"{time_tag()}" + yellow(" Your PC has been BREACHED!\nYou have been targeted by other hackers due to low Honor."))
    if timed_word_challenge2() == False:
        if chance(70):
            loss = random.randint(8, 15)*1000
            Money -= loss
            print(f"{time_tag()}" + yellow(f"Your bank account was hacked!\n You lost {loss}$."))
        else:
            loss = random.randint(5, 8)*100
            Integrity -= loss
            print(f"{time_tag()}" + yellow(f"Your system was hacked!\nYou lost {loss} Integrity."))
    else:
        Honor += 10
        print(f"{time_tag()} " + green(f"You successfully defended against the rival hacker but he got away without any trace left.\n\n Honor INCREASED by 10."))
    return Money, Honor, Integrity

def Hostile_terminal_stats(tracked_computer):
    clear_console()
    print(f"Current Integrity of the target: {tracked_computer.Comp_Integrity}\nFiles on the computer: {[file.name for file in tracked_computer.files if not file.decoy]}\nBanking: {tracked_computer.Banking}$")
