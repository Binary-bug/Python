locations={0:"you are sitting in front of a computer learning python",
           1:"You are standing at the end of a road",
           2:"You are at the top of a hill",
           3:"You are inside a building, a well house for a small stream",
           4:"you are in a valley, beside a stream",
           5:"You are in a forest"}

exits={0:{"Q":0},
       1:{"W":2,"N":3,"E":5,"S":4,"Q":0},
       2:{"N":5,"Q":0},
       3:{"W":1,"Q":0},
       4:{"N":1,"W":2,"Q":0},
       5:{"W":2,"S":1,"Q":0}}


vocab = {"QUIT":"Q",
         "NORTH":"N",
         "SOUTH":"S",
         "WEST":"W",
         "EAST":"E"}
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
# #parse user input using the vocabulary dictionary
#     if len(direction>1):
#         for word in vocab:
#             if word in direction:
#                 direction=vocab[word]
# alternative code
    if len(direction)>1:
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]


    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")


# print(locations[0].split())
# print(locations[3].split(','))
# print(' '.join(locations[0].split()))



