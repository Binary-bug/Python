# imelda = "More Mayhem","Imilda May",2011 ,(
#      (1,"Pulling the Rug"), (2,"Psycho"),(3,"Mayhem"),(4,"kentish town waltz"))
# #
# print("title:",imelda[0],"\nArtist",imelda[1],"\nyear",imelda[2],"\n",imelda[3][0],"\t",imelda[3][1],"\t",imelda[3][2])

## alternatively extract the elements of the tuple


# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     print("\t",song)


# if a tuple contains a list, then the contents of the list can be changed even though tuples are immutable
imelda = "More Mayhem","Imilda May",2011 ,(
     [(1,"Pulling the Rug"), (2,"Psycho"),(3,"Mayhem"),(4,"kentish town waltz")])

print(imelda)

imelda[3].append((5,"All for you"))

title, artist, year, tracks = imelda
tracks.append((6,"Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    print("\t",song)



