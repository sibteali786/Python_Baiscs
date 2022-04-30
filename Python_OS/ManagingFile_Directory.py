# Code written with this module can easily be run across different Os platforms

# windows, Linux and Mac OS with the precaution the absolute paths must be relevant to that specific OS
import os
import datetime
# os.remove("./hello.txt")    # delete he file with this name \

# os.rename("spider.txt","spiderNew.txt")
print(os.path.exists("./../CrashCourse/classes.py"))  # true if file exists in path specified
print(os.path.getsize("./../CrashCourse/classes.py")) # in bytes

print(os.path.getmtime("./../CrashCourse/classes.py"))  # prints seconds from 1st January 1970 thats a unix time stamp
# before this none of the file was created
timestamp = os.path.getmtime("./../CrashCourse/classes.py")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.getcwd())
# os.mkdir("new_dir") # creates new directory
# os.chdir("new_dir") # change current directory to given one
# os.rmdir()  # to remove an empty directory
print(type(datetime.datetime.fromtimestamp(timestamp)))
print(os.listdir()) # get contents of a directory
