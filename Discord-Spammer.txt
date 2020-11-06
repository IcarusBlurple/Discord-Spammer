# Discord-Spammer
A useless Discord spammer to anger the skids
'''
Made by Icarus
Discord Icarus#6179
'''
import time
import keyboard



def TextSpammer():
    print('''
            Discord Text Spammer
          ''')
    user_msg = input("Message To Spam :")
    spam_amount = int(input("How many times Spammed :"))
    counter = 0
    spam_msg = '\n' + user_msg
    print("Wait 5 Sec Before The Spam Starts ....")
    time.sleep(5)
    while True:
        if counter >= spam_amount:
            break
        else:
            keyboard.write(spam_msg)
            counter = counter + 1


TextSpammer()
