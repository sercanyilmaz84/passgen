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

type exit to close the program.

""" + ENDC

# cls is for windows and clear is for linux
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def createpass():
	while True:
		try:
			ui = input(WARNING + "\n\nWhat do you want to create password for?(Facebook, Twitter etc.)>> "+ ENDC)
			#this adds a clean way to exit the program
			if ui == "exit":
				break
			secure_pass = random.SystemRandom()
			passwd = "".join(secure_pass.choice(symb) for i in range(20))
			print(OKGREEN + f"[+] Your {ui} password is:",passwd + ENDC)
			#this is a better way of opening files 
			with open("mypasses.txt", 'a') as passlist:
				passlist.write(f"Your {ui} password is:" + passwd + "\n")
		except:
			break
clear()
print(banner)
createpass()