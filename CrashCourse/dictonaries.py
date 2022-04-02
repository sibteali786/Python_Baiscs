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


# Set

# Used when you want to store a bunch of elements and be certain that they are only present once


# Examples
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return (emails)


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user in group_dictionary[group]:
                if user_groups.keys() and user in user_groups.keys():
                    if group not in user_groups[user]:
                        user_groups[user].append(group)
                else:
                    user_groups[user] = []
                    user_groups[user].append(group)
            # Now add the group to the the list of
    # groups for this user, creating the entry
    # in the dictionary if
    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for fruit, price in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
