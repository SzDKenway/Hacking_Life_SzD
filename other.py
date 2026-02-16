import random
import os
import time

import threading  # Ez a modul lehetővé teszi több szál (thread) indítását, párhuzamosan futó feladatokhoz
import sys

from datetime import datetime

#---------------------------------------------------------------------
from var import *
# from function import *
# from missions import *
#---------------------------------------------------------------------

def get_save_dir():
    if getattr(sys, 'frozen', False):
        # EXE mappa
        base_path = os.path.dirname(sys.executable)
    else:
        # fejlesztés alatt (py futtatás)
        base_path = os.getcwd()

    save_dir = os.path.join(base_path, "saved_g")

    try:
        os.makedirs(save_dir, exist_ok=True)
    except Exception as e:
        print("[ERROR] FOLDER CREATION ERROR:", repr(e))
        time.sleep(5)

    return save_dir

SAVE_DIR = get_save_dir()

def Save_game(Username, Money, Honor, Integrity, MAX_Integrity, survived_days,
              Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses,
              NUMBER_OF_DDoS, Number_OF_Decoders, ranges_of_computers,
              Downloaded_Files, Hostile_EASY_additional_integrity,
              Hostile_MEDIUM_additional_integrity,
              Hostile_HARD_additional_integrity, Savings):

    if not Username or any(c in Username for c in r'\/:*?"<>|'):
        print("Invalid username for filename!")
        return

    file_path = os.path.join(SAVE_DIR, f"{Username}_save.txt")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"{Username}\n")
            file.write(f"{Money}\n")
            file.write(f"{Honor}\n")
            file.write(f"{Integrity}\n")
            file.write(f"{MAX_Integrity}\n")
            file.write(f"{survived_days}\n")
            file.write(f"{Number_OF_MALWARES}\n")
            file.write(f"{NUMBER_OF_BBRUTEF}\n")
            file.write(f"{NUMBER_OF_viruses}\n")
            file.write(f"{NUMBER_OF_DDoS}\n")
            file.write(f"{Number_OF_Decoders}\n")
            file.write(f"{ranges_of_computers}\n")
            file.write(f"{Hostile_EASY_additional_integrity}\n")
            file.write(f"{Hostile_MEDIUM_additional_integrity}\n")
            file.write(f"{Hostile_HARD_additional_integrity}\n")
            file.write(f"{Savings}\n")

            for f in Downloaded_Files:
                file.write(f"{f.name},{f.kind},{getattr(f, 'DECRYPTED', False)},{getattr(f, 'Downloaded', False)},{getattr(f, 'bonus_type', '')}\n")

        clear_console()
        print(green("Game saved successfully."))

    except Exception as e:
        print("SAVE ERROR:", e)
        time.sleep(10)

def Load_game(Username):

    file_path = os.path.join(SAVE_DIR, f"{Username}_save.txt")
    print("Looking for:", file_path)

    if not os.path.exists(file_path):
        print("\nNo save file found.")
        time.sleep(3)
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        Username = lines[0].strip()
        Money = float(lines[1].strip())
        Honor = int(lines[2].strip())
        Integrity = int(lines[3].strip())
        MAX_Integrity = int(lines[4].strip())
        survived_days = int(lines[5].strip())
        Number_OF_MALWARES = int(lines[6].strip())
        NUMBER_OF_BBRUTEF = int(lines[7].strip())
        NUMBER_OF_viruses = int(lines[8].strip())
        NUMBER_OF_DDoS = int(lines[9].strip())
        Number_OF_Decoders = int(lines[10].strip())
        ranges_of_computers = int(lines[11].strip())
        Hostile_EASY_additional_integrity = int(lines[12].strip())
        Hostile_MEDIUM_additional_integrity = int(lines[13].strip())
        Hostile_HARD_additional_integrity = int(lines[14].strip())
        Savings = int(lines[15].strip())

        Downloaded_Files = []
        for line in lines[16:]:
            parts = line.strip().split(',')
            if len(parts) >= 5:
                name, kind, DECRYPTED, Downloaded, bonus_type = parts
                f = type('File', (object,), {})()
                f.name = name
                f.kind = kind
                f.DECRYPTED = DECRYPTED == 'True'
                f.Downloaded = Downloaded == 'True'
                f.bonus_type = bonus_type if bonus_type else None
                Downloaded_Files.append(f)

        return (Username, Money, Honor, Integrity, MAX_Integrity, survived_days,
                Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses,
                NUMBER_OF_DDoS, Number_OF_Decoders, ranges_of_computers,
                Downloaded_Files, Hostile_EASY_additional_integrity,
                Hostile_MEDIUM_additional_integrity,
                Hostile_HARD_additional_integrity, Savings)

    except Exception as e:
        print("\nLoading saved file failed.")
        time.sleep(3)
        return None

def HangerGame(tracked_computer,Integrity):
    number_of_guess = 0
    tries = 0
    success = False

    # Számolja a megengedett rossz találatokat a Comp_Integrity és az Integrity alapján
    try:
        if tracked_computer.Comp_Integrity * 1.7 <= Integrity:
            number_of_guess = random.randint(7, 10)
        elif tracked_computer.Comp_Integrity * 1.3 <= Integrity:
            number_of_guess = random.randint(5, 7)
        else:
            number_of_guess = random.randint(3, 5)
    except Exception:
        number_of_guess = random.randint(3, 5)

    # Egysoros jelszólista (6-15 karakter)
    jelszavak = ["rootkit","zeroday","kernel","firewall","bufferoverflow","exploit","payload","backdoor","sandbox","hackerterminal","hashcat","shellshock","packet","proxyserver","dataninja","binarybeast","codeinject","nullpointer","overclocked","glitchmaster","stackoverflow","crypter","cryptomage","rootaccess","packetdrop"]

    PS = random.choice(jelszavak)
    Solve = ["*"] * len(PS)
    NotGood = []   # tárolhat betűket és teljes hibás tippeléseket egyaránt
    tries = 0

    while True:
        # Ha kitaláltuk az összes betűt -> siker
        if "".join(Solve) == PS:
            clear_console()
            print(f"Current: {''.join(Solve)}")
            print(green("Hacking successful! (word completed)"))
            return True

        # Ha túl sok rossz próbálkozás történt -> bukás
        if tries >= number_of_guess:
            clear_console()
            print(f"Number of wrong tries: {tries}/{number_of_guess}")
            print(f"Current: {''.join(Solve)}")
            try:
                tracked_computer.NoticeHacking = True
            except Exception:
                pass
            return False

        # Állapot megjelenítése
        clear_console()
        print(f"Number of wrong tries: {tries}/{number_of_guess}")
        print(f"\nCurrent: {''.join(Solve)}")
        print(f"Previous wrong guesses: {', '.join(NotGood) if NotGood else 'None'}")

        user_input = input("Give a letter: ").lower().strip()

        if not user_input:
            print(red("No input given."))
            time.sleep(1.2)
            continue

        # Egyetlen karakter bevitele
        if len(user_input) == 1:
            tryPS = user_input
            if not tryPS.isalpha():
                print(red("Single alphabetical letter ONLY!"))
                time.sleep(1.2)
                continue

            if tryPS in NotGood or tryPS in Solve:
                print(red("You already tried this."))
                time.sleep(1.2)
                continue

            if tryPS in PS:
                print(green(f"Letter '{tryPS}' can be found in the solution!"))
                for i, letter in enumerate(PS):
                    if letter == tryPS:
                        Solve[i] = tryPS
            else:
                print(yellow(f"Letter '{tryPS}' is not included."))
                NotGood.append(tryPS)
                tries += 1

            time.sleep(1.2)
            continue

        # Elvileg ide nem érhetünk
        print(red("Invalid input."))
        time.sleep(1.2)

def timed_word_challenge(tracked_computer):
    import threading, time, random

    # Determine time limit based on difficulty
    if tracked_computer.difficulty_level == "Easy":
        timeout = 7
    elif tracked_computer.difficulty_level == "Medium":
        timeout = 6
    else:  # Hard
        timeout = 5

    WordToUse = [
        "PASSWORD", "FIREWALL", "ENCRYPTION", "MALWARE", "VIRUS", "EXPLOIT",
        "DECRYPT", "BRUTEFORCE", "PHISHING", "TROJAN", "KEYLOGGER", "BOTNET",
        "RANSOMWARE", "PROXY", "BACKDOOR", "ROOTKIT", "SQLINJECTION", "PACKET",
        "FIRMWARE", "SPOOFING", "ZERODAY", "SHELLCODE", "CIPHER", "AUTHENTICATE",
        "HASH", "PORTSCAN", "VULNERABILITY", "HONEYPOT", "CRYPTOGRAPHY", "DEBUG",
        "TOKEN", "PATCH", "BUG", "SPYWARE", "COOKIE", "SESSION", "DNS","VPN","LOG",
        "ALERT","CACHE","SCAN", "PING","TRACE", "SIGNAL"
    ]

    # Pick ONE random word
    chosen_word = random.choice(WordToUse)

    Characters = "0123456789"
    line = ""
    randomStart = random.randint(0, 100 - len(chosen_word))

    for i in range(100 - len(chosen_word)):
        if i == randomStart:
            line += chosen_word
        line += random.choice(Characters)

    print(blue("\nType the word correctly before time runs out!"))
    print(line)

    user_input = [None]
    def get_input():
        try:
            user_input[0] = input("Your answer: ").strip().upper()
        except EOFError:
            pass

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    start = time.time()
    while time.time() - start < timeout:
        if user_input[0] is not None:
            break
        time.sleep(0.1)

    if user_input[0] is None:
        print(yellow("\nTime is up! You failed."))
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(yellow(f"\n{time_tag()} Intrusion DETECTED!\n"))
        return False
    elif user_input[0] != chosen_word:
        print("\nIncorrect! You failed.")
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(yellow(f"\n{time_tag()} Intrusion DETECTED!\n"))
        return False
    else:
        print(green("\nCorrect! You succeeded."))
        return True

def timed_word_challenge2():
    import threading, time, random

    WordToUse = ["APPLE", "RIVER", "STONE", "BIRD", "CLOUD","TREE", "FROG", "WIND", "MOON", "FISH",
                 "SUN", "SAND", "LEAF", "RAIN", "STAR","WOOD", "BEE", "ICE", "DOG", "CAT",
                 "LION", "FOX", "DEER", "BEAR", "OWL","DUCK", "HORSE", "GOAT", "WOLF", "MOTH",
                 "PEAR", "GRAPE", "PLUM", "MELON", "ROSE","LILY", "MINT", "SEED", "SNOW", "ROCK"]

    # Pick ONE random word from the list
    chosen_word = random.choice(WordToUse)
    timeout = random.randint(6, 9)

    Characters = "0123456789"
    line = ""
    randomStart = random.randint(0, 100 - len(chosen_word))

    # Build scrambled line with hidden word
    for i in range(100 - len(chosen_word)):
        if i == randomStart:
            line += chosen_word
        line += random.choice(Characters)

    print(blue("\nType the word correctly before time runs out!"))
    print(line)

    user_input = [None]
    def get_input():
        try:
            user_input[0] = input("Your answer: ").strip().upper()
        except EOFError:
            pass

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    start = time.time()
    while time.time() - start < timeout:
        if user_input[0] is not None:
            break
        time.sleep(0.1)

    if user_input[0] is None:
        print(yellow("\nTime is up! You failed."))
        return False
    elif user_input[0] != chosen_word:
        print(yellow("\nIncorrect! You failed."))
        return False
    else:
        print(green("\nCorrect! You succeeded."))
        return True

def PassWord(tracked_computer, Integrity):
    clear_console()
    if tracked_computer.Comp_Integrity * 1.7 <= Integrity:
        number_of_guess = random.randint(7,10)
    elif tracked_computer.Comp_Integrity * 1.3 <= Integrity:
        number_of_guess = random.randint(5,7)
    else:
        number_of_guess = random.randint(3,5)
    
    guess = None
    Guess_Number= 0
    Win = False
    MinNum = 0
    MaxNum = 101
    PS = random.randint(1, 100)
    while Guess_Number < number_of_guess and guess != PS: 
        clear_console()
        print(f"The number is between 1-100.\nYou have {Guess_Number}/{number_of_guess} guesses\nValue is between {MinNum} and {MaxNum}")
        try:
            guess = int(input("Your current guess: "))
        except:
            print(red("Give a valid number!"))
        if guess > PS:
            MaxNum = guess
            print("Guess was too high!")
        elif guess< PS:
            MinNum = guess
            print("Guess was too low!")
        Guess_Number = Guess_Number + 1
    if Guess_Number > number_of_guess:
        Win = False
        print(yellow("You didn't say the magic word!"))
        if tracked_computer.Located != True:
            tracked_computer.NoticeHacking = True
            print(yellow(f"\n{time_tag()} Intrusion DETECTED!\n"))
        time.sleep(3)
    elif guess == PS:
        print(green(f"You figured the right number which was {PS}"))
        Win = True
        time.sleep(3)
    return Win

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def chance(percent: float) -> bool:
   return random.random() < (percent / 100)

def time_tag():
    return datetime.now().strftime("[%H:%M:%S]")

def File_Handler(Number_OF_Decoders, Downloaded_Files):
    while True:
        clear_console()
        if not Downloaded_Files:
            print("No downloaded files available.")
            time.sleep(1.5)
            return Number_OF_Decoders, Downloaded_Files

        print("Downloaded Files:")
        for idx, f in enumerate(Downloaded_Files, start=1):
            status = []
            if f.DECRYPTED:
                status.append("DECRYPTED")
            else:
                status.append("CRYPTED")
            print(f"{idx}. {f.name} {' / '.join(status)}]")

        choice = input("\nEnter the number of the file to select it, or 'back' to exit: ").strip().lower()
        if choice == "back":
            return Number_OF_Decoders, Downloaded_Files

        try:
            idx = int(choice)
            if idx < 1 or idx > len(Downloaded_Files):
                print(red("Invalid file number."))
                time.sleep(1.2)
                continue
        except ValueError:
            print(red("Please enter a valid number."))
            time.sleep(1.2)
            continue

        file = Downloaded_Files[idx - 1]

        # --- Handle commands for selected file ---
        while True:
            clear_console()
            status = []
            if file.DECRYPTED: status.append("DECRYPTED")
            else: status.append("CRYPTED")
            if file.Sent: status.append("sent")
            if file.Published: status.append("published")
            print(f"Selected file: {file.name} {' / '.join(status)}]")
            print(f"Your Decoders: {Number_OF_Decoders}")
            print("Available commands: decode, send, publish, back (to file list)")

            cmd = input("Enter command: ").strip().lower()
            if cmd == "back":
                break  # go back to file selection
            elif cmd == "decode":
                if file.DECRYPTED:
                    print(yellow(f"{file.name} is already DECRYPTED."))
                elif Number_OF_Decoders <= 0:
                    print(red("No decoders left!"))
                else:
                    file.DECRYPTED = True
                    Number_OF_Decoders -= 1
                    print(green(f"{file.name} has been DECRYPTED."))
            elif cmd in ["send", "publish"]:
                if cmd == "send" and file.Sent:
                    print(f"{file.name} has already been sent.")
                elif cmd == "publish" and file.Published:
                    print(f"{file.name} has already been published.")
                elif not file.DECRYPTED:
                    print(f"{file.name} must be DECRYPTED first!")
                else:
                    if cmd == "send":
                        file.Sent = True
                    else:
                        file.Published = True
                    # Remove the file from Downloaded_Files after action
                    Downloaded_Files.remove(file)
                    print(f"{file.name} has been {cmd}ed and removed from downloaded files.")
                    break  # go back to file selection
            else:
                print(red("Invalid command."))

            time.sleep(1.2)

def new_game(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings):
    Money = 10000
    Honor = 100 # below zero will cause problems
    Integrity = 1000 # HP
    MAX_Integrity = 1000
    survived_days = 0
    Number_OF_MALWARES = 10 # get into the computer (need SENDing first)
    NUMBER_OF_BBRUTEF = 10 # hack the computer, and bank account
    NUMBER_OF_viruses = 10 # Weakening the computer (INSTALL it after breaking the firewall)
    NUMBER_OF_DDoS = 5 # Crash the computer (COOKing the system)
    Number_OF_Decoders = 10 # Decrypt the files (DECODE it after downloading)
    Downloaded_Files = []
    ranges_of_computers = 1
    Hostile_EASY_additional_integrity = 0
    Hostile_MEDIUM_additional_integrity = 0
    Hostile_HARD_additional_integrity = 0
    Savings = 0
    return Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, ranges_of_computers, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, Savings

def pro_game_MOD(Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings):
    Money = 1000000
    Honor = 100 # below zero will cause problems
    Integrity = 100000 # HP
    MAX_Integrity = 100000
    survived_days = 0
    Number_OF_MALWARES = 500 # get into the computer (need SENDing first)
    NUMBER_OF_BBRUTEF = 500 # hack the computer, and bank account
    NUMBER_OF_viruses = 500 # Weakening the computer (INSTALL it after breaking the firewall)
    NUMBER_OF_DDoS = 500 # Crash the computer (COOKing the system)
    Number_OF_Decoders = 500 # Decrypt the files (DECODE it after downloading)
    Downloaded_Files = []
    ranges_of_computers = 5
    Hostile_EASY_additional_integrity = 0
    Hostile_MEDIUM_additional_integrity = 0
    Hostile_HARD_additional_integrity = 0
    Savings = 100
    clear_console()
    print(blue("PRO MOD activated"))
    return Money, Honor, Integrity, MAX_Integrity, survived_days, Number_OF_MALWARES, NUMBER_OF_BBRUTEF, NUMBER_OF_viruses, NUMBER_OF_DDoS, Number_OF_Decoders, Downloaded_Files, Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, ranges_of_computers, Savings

def add_Hostile_integrity(Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity, survived_days):
    if survived_days % 2 == 0 and survived_days > 0:
        if chance(45):
            Hostile_EASY_additional_integrity += 50
        elif chance(35):
            Hostile_MEDIUM_additional_integrity += 100
        elif chance(40):
            Hostile_HARD_additional_integrity += 200
    elif survived_days % 5 == 0:
        if chance(85):
            Hostile_EASY_additional_integrity += 50
        elif chance(75):
            Hostile_MEDIUM_additional_integrity += 100
        elif chance(65):
            Hostile_HARD_additional_integrity += 500
    return Hostile_EASY_additional_integrity, Hostile_MEDIUM_additional_integrity, Hostile_HARD_additional_integrity

def Savings_Holder(Savings):
    print(blue("***********SAVINGS****************"))
    Amount = random.randint(1, 1000)
    if Savings == 0:
        print("There is " + yellow("no saved money")+ " for trading.")
    elif chance(65):
        Savings += Amount
        print(green(f"Savings INCREASED to {Savings}$ (+{Amount})"))
    else:
        Savings -= Amount
        if Savings < 0:
            Savings = 0
        print(yellow(f"Savings DECREASED to {Savings}$ (-{Amount})"))
    print(blue("***********SAVINGS****************\n"))
    return Savings

def rent_payment(Money, survived_days, ranges_of_computers):
    rent = 10000*(survived_days/7)
    taxes = Money*random.randint(1,25)*0.01
    bonus = ranges_of_computers*5000
    others = 0
    if chance(70):
        others = random.randint(1, 5)*1000
    full = rent + bonus + taxes + others
    full = round(full)
    Money -= full
    print("\n*****************************")
    print(yellow(f"Rent: {full}\nRent base: {rent}\nRent bonus: {bonus}\nTaxes: {taxes}\nOther expenses: {others}\n\nYour current Money: {Money}$"))
    print("*****************************\n")
    time.sleep(3)
    return Money