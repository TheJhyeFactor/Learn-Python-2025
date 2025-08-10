"""
Simple Contact Book — Overview

Goal:
Build a small command-line program that lets you store, search, and display contact information (like names and phone numbers).

"""

contacts = {
    1: {
        "name": "Jhye",
        "lastname": "omeley",
        "number": "0412826486"
    }
}

def add_contact():
    firstname = input(str("Please input the name of person you want to add to your conatact list: "))
    lastname = input(str(f"Please enter the last name for your contact: "))
    number = input(str(f"Now please enter {firstname} {lastname}'s Number:  "))
    c = input(f"Please confrim is the Contac details are correct: Name: {firstname} {lastname} \n Number: {number}\n Please enter Y for yes N for No\n: ")
    confrim = c.lower()
    if  confrim == "y":
        print("Contact added !!")
        contacts[2] = {
            "name": {firstname},
            "lastname": {lastname},
            "number": {number}
        }
        print(contacts)
    elif confrim == "n":
        print("Okay well now you get to start again happy.")
        add_contact()
    else:
        print("Bruh just enter in the options I showed you haha.")
        add_contact()
        
    


def update_contact():
    num_search = input(str("Please enter the Mobile number of the contact you are trying to update: "))
    
    for key, person in contacts.items():
        if person["number"] == num_search:
            print(person)


def delete_user(firstname,number):
    pass


def show_contact(firstname,number):
    pass


def main_menu():
    print("welcome to the confr")




update_contact()