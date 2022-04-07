file = open("spider.txt")

# read a single line of file
print(file.readline())

#  Read all the way to end
print(file.read())

file.close()

with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()    # makes a list of it where each element is seperated by endline character
file.close()
print(lines)

