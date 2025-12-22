import random
import os
import time

import threading
import sys

from datetime import datetime
#---------------------------------------------------------------------
from other import *
from var import *
#---------------------------------------------------------------------

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def chance(percent: float) -> bool:
    return random.random() < (percent / 100)

def time_tag():
    return datetime.now().strftime("[%H:%M:%S]")

#---------------------------------------------------------------------
def DDoS_Mission(tracked_computer, Money):
    if tracked_computer.contract_Type =="Sabotage the system" and not tracked_computer.IsDone:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your bank account.\n"))
    else:
        print(green("Misison Completed"))
    return tracked_computer, Money


def Cyber_Attack(tracked_computer, Money, Downloaded_Files):
    if tracked_computer is None:
        return tracked_computer, Money, Downloaded_Files

    FirstP = False
    SecondP = False

    if any(f.kind == "important" for f in tracked_computer.files):
        print(yellow("\nThere are still important files among the tracked computer's files to send!"))
    elif any(f.kind == "important" for f in Downloaded_Files):
        print(yellow("\nThere are still important files among your files to send!"))
    else:
        print("\nNo important files among the tracked computer's files.")
        FirstP = True

    if tracked_computer.Comp_Integrity <= 0 and FirstP:
        print(f"{tracked_computer.UserName}'s PC has been destroyed.")
        SecondP = True
    elif tracked_computer.Comp_Integrity <= 0 and not FirstP:
        print(yellow("You need to complete the first part of the mission!"))
    else:
        print(f"\n{tracked_computer.UserName}'s PC has NOT been destroyed yet.")

    if FirstP and SecondP and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"\nMission COMPLETED.\n\n{time_tag()}" + green(f" You received {tracked_computer.payment}$ into your bank account."))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))
    else:
        print("\nMission is yet to complete.\n")

    return tracked_computer, Money, Downloaded_Files


def CyberPunking(tracked_computer, Money, Downloaded_Files):
    if tracked_computer is None:
        return tracked_computer, Money, Downloaded_Files

    FirstP = False
    SecondP = False

    if any(f.kind == "important" for f in tracked_computer.files):
        print(yellow("\nThere are still important files among the tracked computer's files to expose!"))
    elif any(f.kind == "important" for f in Downloaded_Files):
        print(yellow("\nThere are still important files among your files to expose!"))
    else:
        print("\nNo important files among the tracked computer's files.")
        FirstP = True

    if tracked_computer.Virus_Installed < tracked_computer.virus_count:
        print(yellow(f"\nYou have installed {tracked_computer.Virus_Installed}/{tracked_computer.virus_count} viruses."))
    elif tracked_computer.Virus_Installed == tracked_computer.virus_count and FirstP:
        SecondP = True
        clear_console()
        print(f"You have installed required amount of viruses!\n\n{time_tag()}" + green(f" You have received {tracked_computer.payment}$ into your bank account\n"))
    elif tracked_computer.Virus_Installed == tracked_computer.virus_count and not FirstP:
        print(yellow("You need to complete the first part of the mission!"))
    else:
        clear_console()
        print("\nYou have already reached the desired amount of installed viruses.")

    if FirstP and SecondP and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"\nMission COMPLETED.\n\n{time_tag()}" + green(f" You received {tracked_computer.payment}$ into your bank account."))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))
    else:
        print("\nMission is yet to complete.\n")

    return tracked_computer, Money, Downloaded_Files


def Zero_Day_Protocol(tracked_computer, Money):
    if tracked_computer is None:
        return tracked_computer, Money

    FirstP = False
    SecondP = False

    if tracked_computer.contract_Type == 'Zero Day protocol' and tracked_computer.Banking == 0:
        FirstP = True
        print((f"\nYou drained the bank account of {tracked_computer.UserName}."))
    else:
        print(yellow(f"\nYou need to empty {tracked_computer.UserName}'s bank account"))

    if tracked_computer.contract_Type == 'Zero Day protocol' and tracked_computer.Located:
        SecondP = True
    else:
        print(yellow(f"\n{tracked_computer.UserName} needs to be assassinated."))

    if FirstP and SecondP and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"\nMission COMPLETED.\n\n{time_tag()}" + green(f" You received {tracked_computer.payment}$ into your bank account."))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))
    else:
        print("\nMission is yet to complete.\n")

    return tracked_computer, Money


def Virus_Mission(tracked_computer, Money):
    if tracked_computer is None:
        return tracked_computer, Money

    if tracked_computer.Virus_Installed < tracked_computer.virus_count:
        print(f"\nYou have installed {tracked_computer.Virus_Installed}/{tracked_computer.virus_count} viruses.\n")
    elif tracked_computer.Virus_Installed == tracked_computer.virus_count and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        clear_console()
        print(f"You have installed required amount of viruses!\n\n{time_tag()}" + green(f" You have received {tracked_computer.payment}$ into your bank account\n"))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))
    else:
        clear_console()
        print("\nYou have already reached the desired amount of installed viruses.\n")

    return tracked_computer, Money


def Money_Drain(tracked_computer, Money):
    if tracked_computer is None:
        return tracked_computer, Money

    if tracked_computer.contract_Type == "Drain Money" and tracked_computer.Banking == 0 and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"You drained the bank account of {tracked_computer.UserName}.\n\n{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your bank account."))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))

    return tracked_computer, Money


def Assassination(tracked_computer, Money):
    if tracked_computer is None:
        return tracked_computer, Money

    if tracked_computer.contract_Type == "Assassination" and tracked_computer.Located and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"\n{tracked_computer.UserName} has been assassinated.\n")
        print(f"{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your bank account.\n"))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))

    return tracked_computer, Money


def Data_Theft(tracked_computer, Money, Downloaded_Files):
    if tracked_computer is None:
        return tracked_computer, Money, Downloaded_Files

    for f in Downloaded_Files:
        if (tracked_computer.contract_Type == "Data Theft" and f.important and f.Downloaded and f.Sent and f.mission == "Data Theft" and tracked_computer.IsDone == False):
            Money += tracked_computer.payment
            tracked_computer.IsDone = True
            print(f"\nYou successfully stole important data from {tracked_computer.UserName}.\n\n{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your account.\n"))
            Downloaded_Files.remove(f)
            break
        elif tracked_computer.IsDone == True:
            print(green("\nMission completed."))

    return tracked_computer, Money, Downloaded_Files


def Expose_Confidential_Information(tracked_computer, Honor, Money, Downloaded_Files):
    if tracked_computer is None:
        return tracked_computer, Honor, Money, Downloaded_Files

    for f in Downloaded_Files:
        if (tracked_computer.contract_Type == "Expose Confidential Information" and f.important and f.Downloaded and f.Published and f.mission == "Expose Confidential Information" and tracked_computer.IsDone == False):
            Money += tracked_computer.payment
            Honor += 40
            tracked_computer.IsDone = True
            print(f"\nYou successfully exposed confidential information from {tracked_computer.UserName}.\n\n{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your account.\nYour Honor decreased by 40 points.\n"))
            Downloaded_Files.remove(f)
            break
        elif tracked_computer.IsDone == True:
            print(green("\nMission completed."))

    return tracked_computer, Honor, Money, Downloaded_Files


def Delete_Files_Mission(tracked_computer, Money, Downloaded_Files):
    if tracked_computer is None:
        return tracked_computer, Money

    if tracked_computer.contract_Type == 'Delete ALL files' and len(tracked_computer.files) == 0 and len(Downloaded_Files) == 0 and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"\nYou deleted all files of the Target PC. ({tracked_computer.IP})\n\n{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your account."))
    elif tracked_computer.IsDone == True:
        print(green("\nMission completed."))
    elif tracked_computer.contract_Type == 'Delete ALL files' and len(tracked_computer.files) != 0:
        print(yellow("\nNot all files has been deleted yet from the Target's PC."))
    elif tracked_computer.contract_Type == 'Delete ALL files' and len(Downloaded_Files) != 0:
        print(yellow("\nNot all files has been deleted yet from the your PC."))

    return tracked_computer, Money


def Profile_Mission(tracked_computer, Money, Integrity):
    if tracked_computer is None:
        return tracked_computer, Money, Integrity

    if tracked_computer.contract_Type == 'Identity Theft' and tracked_computer.NameChanged and not tracked_computer.NoticeHacking and tracked_computer.IsDone == False:
        Money += tracked_computer.payment
        tracked_computer.IsDone = True
        print(f"{time_tag()}" + green(f" {tracked_computer.payment}$ transferred to your account."))
    elif tracked_computer.contract_Type == 'Identity Theft' and tracked_computer.IsDone:
        if tracked_computer.NoticeHacking:
            loss = random.randint(3,6)*100
            Integrity -= loss
            Money -= tracked_computer.payment
            tracked_computer.contract_Type = 'OFFLINE'
            print(f"\n{time_tag()}" + yellow(f" Intrusion DETECTED!\n\nYour PC has BREACHED!\n-{loss} integrity.\n\n") + f"{time_tag()}" + yellow(f" {tracked_computer.payment}$ has been WITHDRAWN from you bank account.\n"))
        else:
            print(green("\nMission completed."))

    elif tracked_computer.contract_Type == 'Identity Theft' and tracked_computer.NoticeHacking and not tracked_computer.IsDone:
        print(yellow("Target noticed you breaching the system, you will not receive payment."))
        tracked_computer.contract_Type = 'OFFLINE'
    elif tracked_computer.contract_Type == 'Identity Theft' and tracked_computer.Located and tracked_computer.NameChanged:
        print(yellow("You have killed the target. You should have changed their profile first. No payment will be transferred."))
        

    return tracked_computer, Money, Integrity

def Sneaky_Bonus(tracked_computer, Money):
    Bonus = 0
    if tracked_computer is not None:
        if (tracked_computer.contract_Type != 'Identity Theft' and tracked_computer.IsDone and not tracked_computer.NoticeHacking and not tracked_computer.BonusGiven):
            if tracked_computer.difficulty_level == 'Easy':
                Bonus = random.randint(1, 5) * 1000
            elif tracked_computer.difficulty_level == 'Medium':
                Bonus = random.randint(10, 15) * 1000
            elif tracked_computer.difficulty_level == 'Hard':
                Bonus = random.randint(20, 40) * 1000
            Money += Bonus
            tracked_computer.BonusGiven = True
            print(green(f"\nUnnoticed hacking bonus: {Bonus}$"))
        elif tracked_computer.NoticeHacking and not tracked_computer.BonusGiven:
            tracked_computer.BonusGiven = True
            print(yellow("Hacking exposed."))

    return tracked_computer, Money
