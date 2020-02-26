def print_banner():
    print("~~~~~~~~~~AD Attack List Generator~~~~~~~~~~~")
    print('Written by:              __o           o')
    print('                       _ \<_          <|/')
    print('         ~~/\O~^~~    (_)/(_)         / >')
    print('        ________    ___   __        _____')
    print('       / ______/\  /   |_/  |\     /  _  \\')
    print('      / /______\/ / /|   /| ||    /  /\/ /\\')
    print('     / _____/\   / / |__/ | ||   /  __  \\\/')
    print('    / / ____\/  / / /\__\/| ||  /  /\_/ /\\')
    print('   /_/ /       /_/ /      |_|| /_______/ /')
    print('   \_\/unky    \_\/c      \_\| \_______\/eef')
    print('                    02/26/2020')
print_banner()

count = 1
first_names = []
last_names = []

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" When typing the name, Caps will be ignored.")

while True:                                  #first/last name input loop
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("Possible User #", count)
    first_names.append(input("First Name >"))
    last_names.append(input("Last Name  >"))
    
    while True:                             #y/n input correct?
        res = input("More users? (y/n)")
        if res == "y" or res == "n":
            break
        else:
            print("Type either 'y' or 'n'!")
    if res == "n":
        break

    count += 1

users = []
for indx, user in enumerate(first_names):   #Create List of Users
    first_name = user.lower()               #Caps can be ignored in AD
    last_name = last_names[indx].lower()
    users.append(first_name + " " + last_name)

wordlist = []
# complete first- and last name like: johnsmith john.smith john-smith
def complete_names():
    for item in users:
        wordlist.append(item.replace(" ", ""))      #johnsmith
        wordlist.append(item.replace(" ", "."))     #john.smith
        wordlist.append(item.replace(" ", "-"))     #john-smith

# initial of first name and full last name like: jsmith j.smith j-smith
def initial_of_first():
    for item in users:
        split = item.split()
        split[0] = split[0][:1]
        wordlist.append(split[0]+split[1])          #jsmith
        wordlist.append(split[0] + "." + split[1])  #j.smith
        wordlist.append(split[0] + "-" + split[1])  #j-smith

# first three chars of first and last name like: johsmi joh.smi joh-smi
def first_three():
    for item in users:
        split = item.split()
        split[0] = split[0][:3]
        split[1] = split[1][:3]
        wordlist.append(split[0] + split[1])        #johsmi
        wordlist.append(split[0] + "." + split[1])  #joh.smi
        wordlist.append(split[0] + "-" + split[1])  #joh-smi

def write_list():
    with open("user_list.txt", "w") as f:
        for word in wordlist:
            f.write("%s\n" % word)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("###     Generating Wordlist for Users:   ###")

for user in users:
    print(user)

complete_names()
initial_of_first()
first_three()
print("###   Saving Wordlist to user_list.txt   ###")
write_list()
print("###         Done! Happy Hacking!         ###")
