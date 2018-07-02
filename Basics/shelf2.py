import shelve

fruit2 = shelve.open('ShelfTest2')
fruit2['orange'] = "a sweet. orange, citrus fruit"
fruit2['apple'] =  "good for making cider"
fruit2['lemon'] = "a sour, yellow citrus fruit"
fruit2['grape'] = "a small, sweet fruit growing in bunches"
fruit2['lime'] = "a sour, green fruit"


while True:
    shelf_key = input("Please enter a fruit")
    if shelf_key == "quit":
        break
    description = fruit2.get(shelf_key)
    print(description)


fruit2.close()

## a shelve key must be a string otherwise there is no much difference

## u can use values and items methods on shelve as well

