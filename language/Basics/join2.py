locations={0:"you are sitting in front of a computer learning python",
           1:"You are standing at the end of a road",
           2:"You are at the top of a hill",
           3:"You are inside a building, a well house for a small stream",
           4:"you are in a valley, beside a stream",
           5:"You are in a forest"}

exits=[{"Q":0},
       {"W":2,"N":3,"E":5,"S":4,"Q":0},
       {"N":5,"Q":0},
       {"W":1,"Q":0},
       {"N":1,"W":2,"Q":0},
       {"W":2,"S":1,"Q":0}]

loc = 1

while True:
#   for direction in exits[loc].keys():
#      available_exits+= direction + ','
    available_exits=','.join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction=input("Available exits are " + available_exits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")





