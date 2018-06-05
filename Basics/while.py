# i=0
# while i<10:
#     # print("i is now {}".format(i))
#     i+=1
#
# available_exits = ["east","north","south","west"]
# chosen_exit=""
#
#
# while chosen_exit not in available_exits:
#     chosen_exit=input("please choose a direction")
#     if chosen_exit == "quit":
#         print("game over")
#         break
# else:
#     print('Arent you glad, you got out of there')

# guessing game with random number  generator
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess an integer between 1 and {}".format(highest))
guess=int(input())
if guess!=answer:
    if guess < answer:
        print('Please guess higher')
    else:
        print("please guess lower")
    guess=int(input())
    if guess==answer:
        print("Well done, you have guessed it")
    else:
        print("Sorry, you have not guessed it correctly")
else:
    print("You have got it correct the first try")




