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

def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" "*left_margin,text)


centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam spam and spam")
