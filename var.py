import random
import os
import time

import threading  # Ez a modul lehetővé teszi több szál (thread) indítását, párhuzamosan futó feladatokhoz
import sys

from datetime import datetime

#---------------------------------------------------------------------
# from other import *
# from function import *
# from missions import *
#---------------------------------------------------------------------
def green(text):
    return f"\033[32m{text}\033[0m"

def yellow(text):
    return f"\033[33m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"

def blue(text):
    return f"\033[36m{text}\033[0m"

# print(green("Success!"))
# print(yellow("Warning!"))
# print(red("Error!"))


def IP_address():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4)) 
    return ip

def chance(percent: float) -> bool:
   return random.random() < (percent / 100)

#Own stats--------------------------------------------------------------------------
Money = 20000
Honor = 100 # below zero will cause problems
Integrity = 1000 # HP
MAX_Integrity = 1000
survived_days = 0
Number_OF_MALWARES = 10 # get into the computer (need SENDing first)
NUMBER_OF_BBRUTEF = 10 # hack the computer, and bank account
NUMBER_OF_viruses = 10 # Weakening the computer (INSTALL it after breaking the firewall)
NUMBER_OF_DDoS = 10 # Crash the computer (COOKing the system)
Number_OF_Decoders = 10 # Decrypt the files (DECODE it after downloading)
ranges_of_computers = 1
Downloaded_Files = []
Hostile_EASY_additional_integrity = 0
Hostile_MEDIUM_additional_integrity = 0
Hostile_HARD_additional_integrity = 0
Savings = 0

# Shop items
Cost_MALWARES = 7000 # get into the computer
Cost_BBRUTEF = 1500 # hack the computer, and bank account
Cost_viruses = 1000 # Weakening the computer
Cost_DDoS = 12000 # Crash the computer
Cost_Decoders = 700 # Decrypt the files
Cost_little_integrity = 10000 # +50 Integrity
Cost_big_integrity = 22500 # +100 Integrity
Cost_Range = 25000 # +1 range of computers

FirstNames = (
    "Dorina", "Fanni", "Melani", "Vivien", "Ariana",  "Athena", "Mary", "Patricia", "Linda", "Barbara",
    "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Dorothy", "Lisa", "Nancy", "Karen", "Betty",
    "Helen", "Sandra", "Donna", "Carol", "Ruth", "Sharon", "Michelle", "Laura", "Sarah", "Deborah",
    "Jessica", "Shirley", "Cynthia", "Angela", "Melissa", "Amy", "Anna", "Rebecca", "Kathleen", "Martha",
    "Amanda", "Stephanie", "Carolyn", "Christine", "Marie", "Janet", "Catherine", "Ann", "Joyce", "Diane",
    "Alice", "Julie", "Heather", "Teresa", "Evelyn", "Jean", "Cheryl", "Katherine", "Ashley", "Judith",
    "Rose", "Janice", "Kelly", "Nicole", "Judy", "Christina", "Kathy", "Theresa", "Beverly", "Jane",
    "Rachel", "Andrea", "Kathryn", "Sara", "Anne", "Jacqueline", "Wanda", "Bonnie", "Julia", "Ruby",
    "Tina", "Paula", "Diana", "Annie", "Lillian", "Emily", "Robin", "Peggy", "Crystal", "Gladys",
    "Rita", "Connie", "Florence", "Tracy", "Edna", "Tiffany", "Carmen", "Rosa", "Cindy", "Grace",
    "Wendy", "Victoria", "Edith", "Kim", "Sherry", "Sylvia", "Josephine", "Ellen", "Elaine", "Carrie",
    "Charlotte", "Monica", "Esther", "Pauline", "Emma", "Juanita", "Anita", "Rhonda", "Hazel", "Amber",
    "Eva", "Debbie", "April", "Leslie", "Clara", "Eleanor", "Valerie", "Megan", "Alicia", "Suzanne",
    "Michele", "Veronica", "Jill", "Lauren", "Cathy", "Sally", "Regina", "Erica", "Beatrice", "Dolores",
    "Samantha", "Marion", "Dana", "Stacy", "Ana", "Melanie", "Loretta", "Yolanda", "Jeanette", "Laurie",
    "Katie", "Kristen", "Vanessa", "Sue", "Elsie", "Beth", "Vicki", "Carla", "Tara", "Rosemary",
    "Eileen", "Lucy", "Stacey", "Wilma", "Gina", "Kristin", "Jessie", "Natalie", "Agnes", "Vera",
    "Charlene", "Bessie", "Delores", "Melinda", "Allison", "Tamara", "Lillie", "Claudia", "Tanya",
    "Nellie", "Minnie", "Marlene", "Viola", "Marian", "Stella", "Caroline", "Vickie", "Mattie", "Lena"
)

Surnames = ("Shelby", "Ford","Smith", "Johnson", "Wick", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor",
            "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
            "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres",
            "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
            "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz",
            "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers",
            "Gutierrez", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim",
            "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet", "Gray",
            "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long",
            "Ross", "Foster")

NickNames = ("Dragon", "Shad0w", "Wolf", "Ghost", "Hunter", "Ninja", "Samurai", "Knight", "Warrior", "Ranger",
             "HAssassin0", "Sn1per", "Mercenary", "Viking", "P1rat3", "Spartan", "Gladiator", "Paladin", "Monk",
             "Druid", "Sorcerer", "Wizard", "Mage", "Alchemist", "Berserker", "Barbarian", "Rogue", "Thief",
             "Bandit", "Outlaw", "Rebel", "Renegade", "Maverick", "Nomad", "Wanderer", "Seeker", "Explorer",
             "Adventurer")

Othernames = ("Bank", "Comapany", "Comapany Limited", "Corporation", "UNKNOWN", "Industry", "Management", "Enterprise")
spacename = (" ", "'s ", "-")
def Random_Space():
    if chance(50):
        return f"{random.randint(1, 100)}"
    else:
        return f"_{random.randint(1,50)}"
    
        

BONUS_FILE_NAMES_EASY = ["fix_notes.txt", "repair_patch.exe", "small_donation.txt", "lucky_token.dat", "integrity_boost.info"]
BONUS_FILE_NAMES_MEDIUM = ["honor_letter.pdf", "bonus_credentials.txt", "minor_gift_receipt.pdf", "toolkit.zip", "utility_script.py"]
BONUS_FILE_NAMES_HARD = ["exploit_kit.tar.gz", "advanced_tool.key", "high_value_token.dat", "decoder_module.bin", "zero_day_notes.pdf"]

DECOY_FILE_NAMES = ["readme.txt", "not_for_you.txt", "temp.dat", "thumbnail.jpg", "placeholder.docx", "dummy_file.bin", "extra_savings.txt"]

IMPORTANT_FILE_NAMES_EASY = ["passwords.txt", "user_data.csv", "financial_report.pdf", "employee_records.docx"]
IMPORTANT_FILE_NAMES_MEDIUM = [ "client_data.csv", "contracts.docx", "presentation.pptx", "technical_specs.pdf"]
IMPORTANT_FILE_NAMES_HARD = ["confidential_contract.pdf", "intelligence_report.pdf", "encryption_keys.key", "black_ops_report.pdf"]

BONUS_ITEMS = ["Virus", "DDOS", "BruteForce", "Decoder", "Integrity_Patch", "Honor_Badge"]

class Computer:
    def __init__(self):
        self.difficulty_level = random.choice(['Easy', 'Medium', 'Hard'])
        self.IP = IP_address()
        self.Destroyed = False
        self.Located = False
        self.Virus_Installed = 0
        self.IsDone = False
        self.NoticeHacking = False
        self.BonusGiven = False
        self.NameChanged = False


        if self.difficulty_level == 'Easy':
            self.file_count = random.randint(1, 5)
            self.virus_count = 1
        elif self.difficulty_level == 'Medium':
            self.file_count = random.randint(3, 6)
            self.virus_count = random.randint(1, 3)
        else:  
            self.file_count = random.randint(5, 8)
            self.virus_count = random.randint(3, 5)
        self.ORIGINAL_file_count = self.file_count


        if self.difficulty_level == 'Easy':
            self.contract_Type = random.choice(['Data Theft', 'Virus Installation', 'Assassination', 'Identity Theft'])
            self.payment = random.randint(1, 5) * 1000
            userName_First = random.choice(FirstNames)
            userName_Second = random.choice(Surnames)
            self.UserName = userName_First + " " + userName_Second 
            self.Comp_Integrity = random.randint(4, 7) * 100 + Hostile_EASY_additional_integrity
            self.Banking = random.randint(1500, 5000)

        elif self.difficulty_level == 'Medium':
            self.contract_Type = random.choice(["Expose Confidential Information", 'Drain Money', 'Virus Installation', "Sabotage the system"])
            self.payment = random.randint(10, 20) * 1000
            if random.choice([True, False]):
                self.UserName = f"{random.choice(NickNames)}{Random_Space()}" 
            else:
                self.UserName = random.choice(FirstNames) + " " + random.choice(Surnames) 
            self.Comp_Integrity = random.randint(9, 15) * 100 + Hostile_MEDIUM_additional_integrity
            self.Banking = random.randint(5000, 15000)

        elif self.difficulty_level == 'Hard':
            self.contract_Type = random.choice(['CyberPunking', 'Zero Day protocol', 'Cyber Attack', 'Delete ALL files'])
            self.payment = random.randint(30, 60) * 1000
            if random.choice([True, False]):
                self.UserName = f"{random.choice(NickNames)}{Random_Space()}"
            else:
                other = random.choice(Othernames)
                if other == "UNKNOWN":
                    self.UserName = "UNKNOWN" 
                else:
                    self.UserName = random.choice(Surnames) + random.choice(spacename) + other 
            self.Comp_Integrity = random.randint(17, 25) * 100 + Hostile_HARD_additional_integrity
            self.Banking = random.randint(10000, 50000)


        self.files = [Computer.File(self) for _ in range(self.file_count)]


        if self.contract_Type in ["Data Theft", "Expose Confidential Information", 'CyberPunking', 'Cyber Attack']:
            if not any(getattr(f, "important", False) for f in self.files):

                important_file = Computer.File(self)
                important_file.kind = "important"
                important_file.important = True
                important_file.decoy = False

                if self.difficulty_level == "Easy":
                    important_file.name = random.choice(IMPORTANT_FILE_NAMES_EASY)
                elif self.difficulty_level == "Medium":
                    important_file.name = random.choice(IMPORTANT_FILE_NAMES_MEDIUM)
                else:
                    important_file.name = random.choice(IMPORTANT_FILE_NAMES_HARD)

                important_file.DECRYPTED = chance(70) if self.difficulty_level == "Easy" else (chance(80) if self.difficulty_level == "Medium" else chance(90))
                self.files[random.randrange(len(self.files))] = important_file


    class File:
        def __init__(self, computer):
            # CHANGED: unified file fields; note casing kept for your existing flags where possible
            self.name = ""
            self.kind = "normal"     # "bonus", "decoy", "important", "normal"
            self.DECRYPTED = False
            self.Downloaded = False
            self.Sent = False
            self.Published = False
            self.decoy = False
            self.important = False
            self.bonus = False
            self.bonus_type = None   # "Integrity", "Honor", "item"
            self.bonus_value = 0
            self.bonus_item = None
            self.worth = computer.payment
            self.mission = computer.contract_Type

            if chance(60):
                self.kind = "bonus"
                self.bonus = True

                if computer.difficulty_level == "Easy":
                    self.name = random.choice(BONUS_FILE_NAMES_EASY)
                elif computer.difficulty_level == "Medium":
                    self.name = random.choice(BONUS_FILE_NAMES_MEDIUM)
                else:
                    self.name = random.choice(BONUS_FILE_NAMES_HARD)

                if computer.difficulty_level == "Easy":
                    if chance(70):
                        self.bonus_type = random.choice(["Integrity", "Honor"])
                        if self.bonus_type == "Integrity":
                            self.bonus_value = random.randint(50, 150)
                        else:
                            self.bonus_value = random.randint(10, 50)
                    else:
                        self.bonus_type = "item"
                        self.bonus_item = random.choice(BONUS_ITEMS)
                elif computer.difficulty_level == "Medium":
                    if chance(65):
                        self.bonus_type = random.choice(["Integrity", "Honor"])
                        if self.bonus_type == "Integrity":
                            self.bonus_value = random.randint(30, 120)
                        else:
                            self.bonus_value = random.randint(5, 40)
                    else:
                        self.bonus_type = "item"
                        self.bonus_item = random.choice(BONUS_ITEMS)
                else:
                    if chance(60):
                        self.bonus_type = "item"
                        self.bonus_item = random.choice(BONUS_ITEMS)
                    else:
                        self.bonus_type = random.choice(["Integrity", "Honor"])
                        if self.bonus_type == "Integrity":
                            self.bonus_value = random.randint(100, 300)
                        else:
                            self.bonus_value = random.randint(20, 100)

                self.DECRYPTED = chance(30) if computer.difficulty_level == "Easy" else (chance(30) if computer.difficulty_level == "Medium" else chance(30))
                self.decoy = False
                self.important = False

            elif chance(48):
                self.kind = "decoy"
                self.decoy = True
                self.name = random.choice(DECOY_FILE_NAMES)
                self.DECRYPTED = chance(70) if computer.difficulty_level == "Easy" else (chance(80) if computer.difficulty_level == "Medium" else False)
                self.important = False
                self.bonus = False
                self.bonus_type = None

            else:
                self.kind = "important"
                self.important = True
                self.decoy = False
                if computer.difficulty_level == "Easy":
                    self.name = random.choice(IMPORTANT_FILE_NAMES_EASY)
                elif computer.difficulty_level == "Medium":
                    self.name = random.choice(IMPORTANT_FILE_NAMES_MEDIUM)
                else:
                    self.name = random.choice(IMPORTANT_FILE_NAMES_HARD)
                self.DECRYPTED = chance(70) if computer.difficulty_level == "Easy" else (chance(40) if computer.difficulty_level == "Medium" else chance(30))
                self.bonus = False
                self.bonus_type = None