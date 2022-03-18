import sys


try:
    v = sys.argv[1]

except IndexError:
    print("Error: No searchterm provided. Try running \"sign {searchterm}\"")
    quit()

def get_input():
    if other_count > 0:
        v = input("Found {} other matches, show? Y/N: ".format(other_count))
        if v.lower() == "n":
            quit()
        elif v.lower() == "y":
            pass
        else:
            get_input()
    else:
        print("0 more results found")
        quit()

#v = input("Input symbol name or tag to search for: ")

with open("unimathsymbols.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)
best_count = 0
other_count = 0

print("--------------------BEST FIT--------------------")
print("{:10s}{:30s}{}".format("Symbol", "Command", "Comment"))

for line in lines:
    entities = line.split("^")
    if v.lower() == entities[1].lower():
        best_count += 1
        print("{:10s}{:30s}{}".format(entities[1], entities[2], entities[7]))
    elif "\\" + v.lower() == entities[2].lower():
        best_count += 1
        print("{:10s}{:30s}{}".format(entities[1], entities[2], entities[7]))
    elif v.lower() in entities[7].lower():
        other_count += 1


get_input()

print("\n-----------------OTHER MATCHES-----------------")
print("{:10s}{:30s}{}".format("Symbol", "Command", "Comment"))

for line in lines:
    entities = line.split("^")
    if v.lower() in entities[7].lower():
        print("{:10s}{:30s}{}".format(entities[1], entities[2], entities[7]))
