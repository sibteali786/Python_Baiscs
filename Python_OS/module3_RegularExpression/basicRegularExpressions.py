import re

result = re.search(r"aza","plaza bazaaar")  # matches the first occurence and returns an object
# which has  start to ending position also mentions the matching result
print(result)

# if nothing is matched the return none

# search with starting characters
print(re.search(r"^a","aelia")) # matches words starting with a

# match anything in between given characters using dot " . "
print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","clapping"))
print(re.search(r"p.ng","sponge"))

# script for check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other
# character in between.

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


# for case insensitive
print(re.search(r"^a","Aelia",re.IGNORECASE)) # matches words starting with a while being case insensitive