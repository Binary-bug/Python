characters = set(input("Please enter the text : "))
vowels = ('a','e','i','o','u')
# vowels = frozenset("aeiou") quicker to types
print(sorted(characters.difference(vowels)))