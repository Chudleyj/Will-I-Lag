#Ping function code derived from: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
#Python app to test ping of popular game servers.
#CREATED BY: Justin Chudley
#This code has been released as open source at: https://github.com/Chudleyj/Will-I-Lag

from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import time

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0

def get_league_server():

    print("Which League server are you on?")

    while(True):
        print ("Enter 1 for: NA")
        print ("Enter 2 for: EUW")
        print ("Enter 3 for: EUNE")
        print ("Enter 4 for: OCE")
        print ("Enter 5 for: LAN")
        server_choice = raw_input()

        if(server_choice == "1"):
            return "104.160.131.3"

        elif(server_choice == "2"):
            return "104.160.141.3"

        elif(server_choice == "3"):
            return "104.160.142.3"

        elif(server_choice == "4"):
            return "104.160.156.1"

        elif(server_choice == "5"):
            return "104.160.136.3"

        else:
            print("Error. Invalid choice. Please try again.")

def get_overwatch_server():

    print("Which Overwatch server are you on?")
    
    while(True):
        print ("Enter 1 for: US West")
        print ("Enter 2 for: US Central")
        print ("Enter 3 for: Brazil")
        print ("Enter 4 for: Europe")
        print ("Enter 5 for: Korea")
        print ("Enter 6 for: Taiwan")
        server_choice = raw_input()

        if(server_choice == "1"):
            return "24.105.30.129"

        elif(server_choice == "2"):
            return "24.105.62.129"

        elif(server_choice == "3"):
            return "54.207.107.12"

        elif(server_choice == "4"):
            return "185.60.114.159"

        elif(server_choice == "5"):
            return "211.234.110.1"

        elif(server_choice == "6"):
            return "203.66.81.98"

        else:
            print("Error. Invalid choice. Please try again.")

def get_HOS_server():

    print("Which Heroes of the Storm server are you on?")

    while(True):
        print ("Enter 1 for: US West")
        print ("Enter 2 for: US Central")
        print ("Enter 3 for: Australia")
        print ("Enter 4 for: Singapore")
        print ("Enter 5 for: Brazil")
        print ("Enter 6 for: Europe")
        print ("Enter 7 for: Korea")
        print ("Enter 8 for: Taiwan")
        server_choice = raw_input()

        if(server_choice == "1"):
            return "24.105.30.129"

        elif(server_choice == "2"):
            return "24.105.62.129"

        elif(server_choice == "3"):
            return "103.4.114.233"

        elif(server_choice == "4"):
            return "202.9.67.59"

        elif(server_choice == "5"):
            return "54.207.104.145"

        elif(server_choice == "6"):
            return "185.60.112.157"

        elif(server_choice == "7"):
            return "182.162.116.1"

        elif(server_choice == "8"):
            return "203.69.111.4"

        else:
            print("Error. Invalid choice. Please try again.")

def get_WoW_server():

    print("Which World of Warcraft server are you on?")

    while(True):
        print ("Enter 1 for: US")
        print ("Enter 2 for: Europe")
        print ("Enter 3 for: Korea")
        print ("Enter 4 for: Taiwan")
        print ("Enter 5 for: Oceania")
        server_choice = raw_input()

        if(server_choice == "1"):
            return "24.105.30.129"

        elif(server_choice == "2"):
            return "185.60.112.157"

        elif(server_choice == "3"):
            return "211.115.104.1"

        elif(server_choice == "4"):
            return "210.71.148.11"

        elif(server_choice == "5"):
            return "103.4.115.248"

        else:
            print("Error. Invalid choice. Please try again.")

print("Welcome to Will I Lag. Choose your game below: ")

valid = False

while(not valid):

    print("Enter 1 for: League of Legends")
    print("Enter 2 for: Overwatch")
    print("Enter 3 for: Heroes of the Storm")
    print("Enter 4 for: World of Warcraft")
    choice =  raw_input()

    if(choice == "1"):
        host = get_league_server()
        valid = True

    elif(choice == "2"):
        host = get_overwatch_server()
        valid = True

    elif(choice == "3"):
        host = get_HOS_server()
        valid = True

    elif(choice == "4"):
        host = get_WoW_server()
        valid = True

    else:
        print("Error. Invalid choice. Please try again.")
        valid = False

print("")
print("Pinging Server...")
print("")

i = 0
while(i < 10):
    ping(host)
    i = i + 1
    time.sleep(1.5)
