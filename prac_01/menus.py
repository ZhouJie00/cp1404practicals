# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message


name = input("Enter name: ")


options =""
while options!="Q":

    options = input("(H)ello\n(G)oodbye\n(Q)uit\n")

    if options == "H":
        print(f"Hello {name}")
    elif options == "G":
        print(f"Goodbye {name}")
    elif options == "Q":
        print("Finished.")
    else:
        print("Invalid choice")



