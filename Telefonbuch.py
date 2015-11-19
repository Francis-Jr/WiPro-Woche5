__author__ = 'jakobunfried'

entries = {}  # zugriff z.B. d["Jakob"]=017647343383 , key muss Hashable (unterscheidbar) sein.
# if key in d
# iterieren: for key in d:

clear = "\n" * 20


def new_entry():
    print "Creating new entry"
    name = raw_input("Name: ")
    # TODO deal with wrong input
    number = raw_input("Number: ")
    entries[name] = number
    print clear


def find_entry():
    print "Search"
    name = raw_input("Name: ")
    if name in entries:
        print clear
        print name
        print entries[name]
    else:
        print"Eintrag exisitiert nicht!"
    print""
    print""


def list_entries():
    print "Listing entries"
    for key in entries:
        print key + " : " + entries[key]
    print""
    print""


tasks = {"1": new_entry,
         "2": find_entry,
         "3": list_entries,
         }


def main_menu():
    print "Menu"
    print "(1) new entry"
    print "(2) find entry"
    print "(3) list entries"
    print "(4) quit"
    inp = raw_input()
    print clear
    return inp


while True:
    task = main_menu()
    if task == "4":
        break  # DO NOT REMOVE WITHOUT REPLACEMENT!!!
    else:
        tasks[task]()
