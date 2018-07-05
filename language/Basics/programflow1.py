# name = input("Please enter your name")
#
#
# age = int(input("How old are you, {0}?".format(name)))
#
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put a vote in the ballot")
# else:
#     print("Please come back in {} years".format(18-age))
#
# elif usage

print("please guess a number between 1 and 10")
guess = int(input())


# if guess < 5:
#     print("please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("well done, you guessed it")
#     else:
#         print("you have not guessed correctly")
#
#
# elif guess > 5:
#     print("please guess lower")
#     guess= int(input())
#     if guess == 5:
#         print("well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("YOu got it first time")

if guess != 5:
    if guess < 5:
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("well done, you guessed it")
    else:
        print("you have not guessed correctly")
else:
    print("YOu got it first time")