#Create a random number to input in the guess loop
import secrets

randoNum = secrets.SystemRandom().randrange(1,10)
mainLoop = []
#Test
#print(randoNum)

#Guess loop
while True:
	mainLoop = int(input("Guess the number: "))
	if mainLoop == randoNum:
		break
	if mainLoop > randoNum:
		print("Lower")
	elif mainLoop < randoNum:
		print("Higher")

#Print the winning message using ANSI code to color it green.
print("""\033[1;32m
 __     ______  _    _  __          _______ _   _ _
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_(_)

""")
