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
multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python","Ruby","Scala","Go","JS"]
lengths = [len(x) for x in languages]
print(lengths)

# Conditional Comprehension
x = [x for x in range(0,101) if x%3==0]
print(x)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [x[:x.index("hpp")] + "h" if x.endswith("hpp") else x for x in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]