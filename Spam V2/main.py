from colorama import *
import discum
import time

spamV2 = """ 
   _____   _____               __  __    __      __  ___  
  / ____| |  __ \      /\     |  \/  |   \ \    / / |__ \ 
 | (___   | |__) |    /  \    | \  / |    \ \  / /     ) |
  \___ \  |  ___/    / /\ \   | |\/| |     \ \/ /     / / 
  ____) | | |       / ____ \  | |  | |      \  /     / /_ 
 |_____/  |_|      /_/    \_\ |_|  |_|       \/     |____|
                                                          

"""

print(Fore.RED + spamV2)

token2 = str(input("Donnez le token :"))
id_channel = input("Donnez l'id du channel :")
message_spam = input("Donnez le message a spam :")

bot = discum.Client(token=token2, log=True)


def creat():
    newDM = bot.createDM([id_channel]).json()["id"]
    print(newDM)
    bot.sendMessage(newDM, "hi bitch")

def spam():
    var = bot.sendMessage(id_channel, message_spam)
    print(var)

while True:
    try:
        spam()
        time.sleep(0.01)
    except exception as e:
        print(e)