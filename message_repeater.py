import time
import pyautogui           ######## If you don't have this pyautogui module then install it by just typing " pip install pyautogui " in terminal. ########

# msg = "good day 💔🥳"
msg = input("Enter your message that repeats: ")
n = input("How many times ?: ")

print("Now in the count-down of 5 ....👇")
time.sleep(2)

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Now working on Task ....... ")

for i in range(0,int(n)):
	time.sleep(.5)
	pyautogui.typewrite(msg + '\n') 

print('Waaoooo 😮 Tasking Complete......! 🤩')
