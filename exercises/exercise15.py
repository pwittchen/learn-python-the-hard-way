# Exercise 15: Reading files
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()

# in order to read file named exercise15_data.txt run the following command:
# python exercise15.py exercise15_data.txt