"""
Simple Contact Book — Overview

Goal:
Build a small command-line program that lets you store, search, and display contact information (like names and phone numbers).

"""

contacts = {
    "Jhye": "0438965894",
}

def add_contact():
    firstname = input(str("Please input the name of person you want to add to your conatact list: "))
    number = input(str(f"Now please enter {firstname}'s Number:  "))
    c = input(f"Please confrim is the Contac details are correct: Name: {firstname}\n Number: {number}\n Please enter Y for yes N for No\n: ")
    confrim = c.lower()
    if  confrim == "y":
        print("Contact added !!")
    elif confrim == "n":
        add_contact()
    else:
        print("Bruh just enter in the options I showed you haha")
        
    


def update_contact(firstname,number):
    pass


def delete_user(firstname,number):
    pass


def show_contact(firstname,number):
    pass



add_contact()