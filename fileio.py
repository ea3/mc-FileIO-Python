# jabber = open("sample.txt", 'r')  # I can also use the complete path. THis is the relative path. The file has to be in the working directory.
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end="")
#
# jabber.close()
#
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end = '')


# with open("sample.txt") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("sample.txt") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')
