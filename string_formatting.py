name = "   Sibteali Tala    "
print(name.index("t"))

# returns index for first match and not for all we get to match in the string
print("ali" in name)


def replace_domain(email, old_domain, new_domain):
    mail = []
    for l in email:
        if "@" + old_domain in l:
            index = l.index("@" + old_domain)
            new_email = l[:index] + "@" + new_domain
            mail.append(new_email)
        else:
            mail.append(l)

    return mail


email = ["sibteali786@yahoo.com", "juanidNaqvi@yahoo.com", "Memoona23@yahoo.com", "Ale23@ad.com"]
print(replace_domain(email, "yahoo.com", "gmail.com"))

# Python string Methods
print(name.upper())  # to upper case
print(name.strip())  # trim surroudning whitespace
print(name.lstrip())
print(name.rstrip())
print("How many times e occured in name ? \n", name.count("e"))
print(name.endswith("Tala"))  # checks if ends with this substring
print(name.isnumeric())  # returns false as is string not a number
num = "1223"
print(num.isnumeric())
# joins given element by this initial gievn string which is empty space
empty_str = " "
print(empty_str.join(["This", "is", "a", "phrase", "joined", "by", "join"]))
print(name.split())

# further expressions
price = 7.5
price_tax = price * 1.09
print(price, price_tax)
print("Base Price: ${:.2f}. With Tax: ${:.2f}".format(price, price_tax))

# Practical Example
print("Temperature in Celsius and Fahrenheit")


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))




# >3 means keep 3 align text to right upto three spaces, >6 means align text to right upto 6 spaces


