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
fruits = ["pineaple","banana","Apple","Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.insert(0,"Orange")   #
print(fruits)

fruits.insert(25,"Peach")   # even though index 25 does not exist but even then it puts it to last index
print(fruits)

fruits.remove("Orange") # Removes first occurrence and gives error if not found
print(fruits)

fruits.pop(5)   # removes element that given index
print(fruits)

# Iteration
animals = ["Lion","Zebra","Dolphin","Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters : {}, Average length: {}".format(chars,chars/len(animals)))