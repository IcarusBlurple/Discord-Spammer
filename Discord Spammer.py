'''
Made by maybe
Discord Maybe#1337
'''
import time
import keyboard



def TextSpammer():
    print('''
            Discord Text Spammer
          ''')
    user_msg = input("What Do You Want To Spam ? :")
    spam_amount = int(input("How Many Times Do You Want To Spam ? :"))
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
