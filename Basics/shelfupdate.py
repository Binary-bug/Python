import shelve

blt = ["bacon","tomato","bread"]

beans_on_toast = ["beans","bread"]

scrambled_eggs = ["eggs","butter","milk"]

soup = ["tin of soup"]

pasta = ["pasta","cheese"]

with shelve.open('recipes',writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup



    #3 TO APPEND items this wont work, since shelve doesnt know that items have been
    #updated

    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    for snack in recipes:
        print(snack, recipes[snack])

    #Method 1: append to a copy and assign the copy to the same key

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

    print('*'*40)
    #Method 2 to set True WriteBacks fro shelve
    recipes["pasta"].append("milk")


    for snack in recipes:
        print(snack, recipes[snack])

    ## sync method
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    ## the above didnt work because sync clears the cache. so writeback wont work
