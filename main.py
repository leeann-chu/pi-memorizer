#LeeAnn Chu
#8/6/17
#Pi Memorizer in Python
import random
start = 1
repeat = 1

print("Would you like to try and memorize pi? You've come to the right place")
nice = ["Good Job!", "Way to go!", "Nice!", "Woot", "Yes!", "Noice"]
api = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489"
sapi = ([api[i:i+4] for i in range (0, len(api),4)])

while start == 1:
    upi = str(input("Starting with 3.14... write the rest of pi that you know: \n"))
    j = random.randint(0,5)
    supi = ([upi[i:i+4] for i in range (0, len(upi),4)])
    start = 0
    repeat = 1
    while (repeat == 1):
        repeat = 0
        start = 0
        error = 0
        for i in range (0,len(supi)):
            if supi[i] != sapi[i]:
                print("non, you heked up set" , i+1, end = " ")
                print("Pi:" , sapi[i], "Input:", supi[i])
                error += 1
        if error == 0:
            print(nice[j])
            print("You made it to set:" , i+1, end = "")
            print("!")
            print("You know", len(upi), "digits of pi")
        cont = int(input("1: Give me the next set \n2: Let me type it all in again \n3: Quit \n?: "))
        if cont == 1:
            start = 1
            print(sapi[len(supi)])
        if cont == 2:
            start = 1
        if cont == 3:
            print("We're sorry to see you go!")
            break
        if cont == 4:
            print(supi)
