'''
Made by maybe
Discord Maybe#1337
'''
import time
import keyboard

banner='''
  _____  _                       _   _______        _      _____                                           
 |  __ \(_)                     | | |__   __|      | |    / ____|                                          
 | |  | |_ ___  ___ ___  _ __ __| |    | | _____  _| |_  | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 | |  | | / __|/ __/ _ \| '__/ _` |    | |/ _ \ \/ / __|  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | |__| | \__ \ (_| (_) | | | (_| |    | |  __/>  <| |_   ____) | |_) | (_| | | | | | | | | | | |  __/ |   
 |_____/|_|___/\___\___/|_|  \__,_|    |_|\___/_/\_\\__| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                                | |                                        
                                                                |_|
'''

def TextSpammer():
    print(banner)
    user_msg = input("What Do You Want To Spam ? :")
    try:
        spam_amount = int(input("How Many Times Do You Want To Spam ? :"))
        wait_time = int(input("How many seconds do you want to wait until the spamming starts ? : "))
    except:
        print("The value given is not a valid number")
        return
    
    
    counter = 0
    spam_msg = '\n' + user_msg
    print("Wait 5 Sec Before The Spam Starts ....")
    time.sleep(wait_time)
    while True:
        if counter >= spam_amount:
            break
        else:
            keyboard.write(spam_msg)
            counter += 1


TextSpammer()
