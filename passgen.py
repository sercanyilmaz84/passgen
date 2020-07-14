#####################################
# Coded by Sercan Yılmaz
# Contact: sercanyilmaz@protonmail.com
#####################################
import random
from string import digits
from string import punctuation
from string import ascii_letters
import os

OKGREEN = '\033[92m'
ENDC = '\033[0m'
BOLD = '\033[1m'
WARNING = '\033[93m'
symb = ascii_letters + digits + punctuation

banner = OKGREEN + """

----------------------------
  Random Password Generator
   coded by sercan yılmaz
 sercanyilmaz@protonmail.com
----------------------------

""" + ENDC

def createpass():
	while True:
		try:
			ui = input(WARNING + "\n\nWhat do you want to create password for?(Facebook, Twitter etc.)>> "+ ENDC)
			secure_pass = random.SystemRandom()
			passwd = "".join(secure_pass.choice(symb) for i in range(20))
			print(OKGREEN + f"[+] Your {ui} password is:",passwd + ENDC)
			passlist = open('mypasses.txt',"a")
			passlist.write(f"Your {ui} password is:" + passwd + "\n")
			passlist.close()
		except:
			break
os.system("cls")
print(banner)
createpass()