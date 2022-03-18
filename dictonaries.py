# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
file_counts = {"jpg": 10, "txt": 14, "py": 23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)

# new values replaces the previous if samilar otherwise gets added in the end
file_counts["png"] = 20
print(file_counts)

# updating a value
file_counts["txt"] = 16
print(file_counts)

# deleting a value
del file_counts["png"]
print(file_counts)

# Iterating over the dictionary
for key, value in file_counts.items():
    print("There are {1} files with extension .{0}".format(key, value))

# Dicionary
print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)


# couting the number of times a value appears in dictioanry
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letter("tenant"))
print(count_letter("Counting letters in a long string given"))