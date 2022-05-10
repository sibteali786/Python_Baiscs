import re

result = re.search(r"aza", "plaza bazaaar")  # matches the first occurrence and returns an object
# which has start to ending position also mentions the matching result
print(result)

# if nothing is matched the return none

# search with starting characters
print(re.search(r"^a", "aelia"))  # matches word starting with a

# match anything in between given characters using dot " . "
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))


# script for check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other
# character in between.

def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

# for case insensitive
print(re.search(r"^a", "Aelia", re.IGNORECASE))  # matches words starting with a while being case insensitive

# it matches both versions of capitalized and lowercase string
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[Pp]ython", "python"))

# we can use a-z to define a range of lowercase characters to match
print(re.search(r"[a-z]way", "the end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))  # Do not matches as space was not included in a-z

# Exapnding our search results with a-zA-Z0-9
print(re.search(r"Cloud[a-zA-Z0-9]", "Cloudy"))
print(re.search(r"Cloud[a-zA-Z0-9]", "Cloud8"))


# Example
def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Carrot sign ^ used in the brackets matches anything except the one mentioned in the brackets
print(re.search(r"[^a-zA-Z]", "This is a Sentence."))  # matches non alphabet letters
print(re.search(r"[^a-zA-Z ]", "This is a Sentence."))  # matche the dot as its only which is not excluded

# The pipe | character matches with either one mentioned in brackets
print(re.search(r"cat|dog", "This is a cat."))
print(re.search(r"cat|dog", "This is a dog."))
print(re.search(r"cat|dog", "I Like cats and dogs."))  # matches only first one
print(re.findall(r"cat|dog", "I like cats and dogs."))  # matches all of them

#  Repeated Matches
print(re.search(r"Py.*n", "Pygmalion"))  # match anything between py and n , zero or n number to times
print(re.search(r"Py.*n", "Python Programming"))  # matches all until g as * is greedy in terms of matching
print(re.search(r"Py[a-z]*n", "Python Programming"))  # matches the python only as we like to match only characters and
# not the spaces as well
print(re.search(r"Py[a-z]*n", "Pyn"))  # zero match possibility

#  Some other Repetetion qualifiers include plus ( + ) and ( ? )
# + matches one or more occurrences of the character which comes before it
print(re.search(r"o+l+", "goldfish"))  # matches only the ol
print(re.search(r"o+l+", "woolly"))  # matches ooll as + plus indicates one or more repetition
print(re.search(r"o+l+", "boil"))  # does not match as i comes in between "o" and "l"

# Example
def repeating_letter_a(text):
    result = re.search(r"[a|A].*[a|A]", text)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

#  ? either zero or one times
print(re.search(r"p?each", "to each their own"))  # matches as ? matches zero match
print(re.search(r"p?each", "I like peaches"))  # matches as p occurs only once


# match a particular pattern or character like dot ( . ) or comma ( , ) or Question mark ( ? )
print(re.search(r"\.com","welcome"))    # do not matches
print(re.search(r"\.com","mydomain.com"))   # matches .com

# \w matches any alphanumeric character like letters, numbers and undercores
print(re.search(r"\w*","This is our idea")) # matches only "this" as \w do not matches empty space
print(re.search(r"\w*","This_is_our_idea")) # matches as it includes underscores

# \d for matching digits
# \s for matching whitespace characters like space, newline or tabs
# \b for word boundaries

def check_character_groups(text):
    result = re.search(r"\w+\s*\d+",text)
    return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# regex101.com r checking regular expression