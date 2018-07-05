def python_food():
    print("spam and eggs")


# calling the function
python_food()


#if you dont explicitly use return None is returned

print(python_food())

#if function call is an arguemnt to print, function is executed
# and its result is passed as an argument to print

#here python_food() returns None


print('*'*40)

def python_food2():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" "*left_margin,text)


python_food2()
print('*'*40)



# def centre_text(*args): # sending multiple arguments
#     text =""
#     for arg in args:                #concatenating is not efficient though
#         text +=str(arg) + " "
#     left_margin = (80 - len(text)) // 2
#     print(" "*left_margin,text)
#

##modifying centre_text to behave like print

# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
#     text =""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)
#
#
# with open("centered",'w') as centered_file:
#     centre_text("spam and eggs",file=centered_file)
#     centre_text(12,file=centered_file)
#     centre_text("spam, spam spam and spam",file=centered_file)
#     centre_text("first","second",3,4,"spam",sep=':',file=centered_file)

##modifying centre_text to use return

def centre_text(*args, sep=' '):
    text =""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# #with open("centered",'w') as centered_file:
# print(centre_text("spam and eggs"))
# print(centre_text(12))
# print(centre_text("spam, spam spam and spam"))
# print(centre_text("first","second",3,4,"spam",sep=':'))

with open("centered",'w') as centered_file:
    print(centre_text("spam and eggs"),file=centered_file)
    print(centre_text(12),file=centered_file)
    print(centre_text("spam, spam spam and spam"),file=centered_file)
    print(centre_text("first","second",3,4,"spam",sep=':'),file=centered_file)

