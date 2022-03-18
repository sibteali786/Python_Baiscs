# def get_word(sentence, n):
# 	# Only proceed if n is positive
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")
#
# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing


# modifying contents
fruits = ["pineaple", "banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.insert(0, "Orange")  #
print(fruits)

fruits.insert(25, "Peach")  # even though index 25 does not exist but even then it puts it to last index
print(fruits)

fruits.remove("Orange")  # Removes first occurrence and gives error if not found
print(fruits)

fruits.pop(5)  # removes element that given index
print(fruits)

# Iteration
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters : {}, Average length: {}".format(chars, chars / len(animals)))


def skip_elements(elements):
    # code goes here
    new_list = []
    for index, elem in enumerate(elements):
        if index % 2 == 0:
            new_list.append(elem)
        else:
            continue
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# List Comprehension
multiples = []
# for x in range(1,11):
#     multiples.append(x*7)
# print(multiples)

# using comprehension
multiples = [x * 7 for x in range(1, 11)]
print(multiples)

languages = ["Python", "Ruby", "Scala", "Go", "JS"]
lengths = [len(x) for x in languages]
print(lengths)

# Conditional Comprehension
x = [x for x in range(0, 101) if x % 3 == 0]
print(x)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [x[:x.index("hpp")] + "h" if x.endswith("hpp") else x for x in filenames]

print(newfilenames)


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = " "
    # Separate the text into words
    words = text.split()
    new_list = []
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + "ay"
        new_list.append(word)
        # Turn the list back into a phrase

    return say.join(new_list)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


def group_list(group, users):
    members = group + ": " + " ".join(users)
    return members


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


def guest_list(guests):
    for x in guests:
        name, age, profession = x
        print("{0} is {1} years old and works as {2}".format(name,age,profession))


# print("{name} is {age} years old and works as {}".format(name=name,age = age, profession = profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
