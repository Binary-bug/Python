#outer scope do not have access to variables inside inner scope
#but inner scope has access to variables at outer scope

# here nonlocal keyword is not needed unlike in os_recursion
# since variables in outer scope are not being modified

def spam1():

    def spam2():

        def spam3():
            z = "even more spam"
            z += y
            print("In spam3,locals are {}".format(locals()))
            return z

        y = " more spam " + x # y must exist before spam3 is called
        y += spam3() # do not combine these two assignments
        print("In spam2, locals are {}".format(locals()))
        return y
    x = "spam"
    x+= spam2() # x must exist before spam2() is called
    print("IN spam1, locals are{}".format(locals()))
    return x

print(spam1())

# at the module level, local scope is equivalent to global scope

print(locals())
print(globals())

# LEGB == local , enclosing (non-local and free) ,global , builtins,

# Above is the order in which pyhthon searches for names

