shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
#
# for item in shopping_list:
#     if item=='spam':
#         continue
#     print("Buy "+item)
#

# # breaking out of the for loop
#
# for item in shopping_list:
#     if item == 'spam':
#         break
#     print("Buy "+item)

# meal = ["egg","bacon","spam","sausages"]
# nasty_food_item=''
# for item in meal:
#     if item=="spam":
#         nasty_food_item=item
#         break
# if nasty_food_item:
#     print("Can't I have anything without spam in it")


meal = ["egg","bacon","spam","sausages"]

for item in meal:
    if item=="spam":
        nasty_food_item=item
        break
else: # this else is the continuation of the break, if the if inside the for loop is executed then it will not go into the else
    print("I'll have a plate of that,then,please")
    nasty_food_item = ''

if nasty_food_item:
    print("Can't I have anything without spam in it")


