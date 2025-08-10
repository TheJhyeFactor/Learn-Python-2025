"""
Simple Contact Book — Overview

Goal:
Build a small command-line program that lets you store, search, and display contact information (like names and phone numbers).

"""

contacts = {
    1: {
        "name": "jak",
        "lastname": "man",
        "number": "0412826486"
    },
    2: {
        "name": "random man",
        "lastname": "weridper",
        "number": "0412826486"
    }
}

def get_next_id():
    if contacts:
        return max(contacts.keys()) + 1
    else:
        return 1 # incase contacts is empty




def add_contact():
    firstname = input(str("Please input the name of person you want to add to your conatact list: "))
    lastname = input(str(f"Please enter the last name for your contact: "))
    number = input(str(f"Now please enter {firstname} {lastname}'s Number:  "))
    confirm = input(f"Please confrim is the Contac details are correct: \nFirstName: {firstname} \nLastName {lastname} \nNumber: {number}\n Please enter Y for yes N for No\n: ").lower()
    new_id = get_next_id()
    if  confirm == "y":
        print("Contact added !!")
        contacts[new_id] = { # i need to ensure we are adding a random id and or ++ as this needs to be able to incress based on 
            "name": firstname,
            "lastname": lastname,
            "number": number
        }
        print(contacts)
    elif confirm == "n":
        print("Okay well now you get to start again happy.")
        add_contact()
    else:
        print("Bruh just enter in the options I showed you haha.")
        add_contact()
    return main_menu()
    
        
    


def update_contact():
    num_search = input(str("Please enter the Mobile number of the contact you are trying to update: "))
    for contact_id, person in contacts.items():
        if person["number"] == num_search:
            num_upconfrim = input(f"Confrim contact to update: {person}\n Do you want to update this contact ? Y(yes) : N(no)").lower()
            
            if num_upconfrim == "y":
                field = input(f"What field do you want to update: f(Firstname): L(Lastname): M(Mobile Number)\n Please enter the letter according to the field you want to update:- ").lower()
                if field == "f":
                    updated_firsname = input(str("Please enter new Firstname: "))
                    contacts[contact_id]["name"] = updated_firsname
                    print(f"Firstname updated: {person}")
                elif field == "l":
                    updated_lastname = input(str("Please enter new lastname: "))
                    contacts[contact_id]["lastname"] = updated_lastname
                    print(f"Lastname number updated: {person}")
                elif field == "m":
                    updated_mobile = input(str("Please enter new mobile number: "))
                    contacts[contact_id]["number"] = updated_mobile
                    print(f"Mobile number updated: {person}")
                else:
                    print("invaild option")
                    num_upconfrim
            elif num_upconfrim == "n":
                update_contact()
            else:
                print("Bruh just enter in the options I showed you haha.")
                update_contact()
            return main_menu

def delete_user():
    num_search = input(str("Please enter the Mobile number of the contact you are trying to delete: "))
    for contact_id, person in contacts.items():
        if person["number"] == num_search:
            contact_del = input(f"Confirm contact to update: {person}\n Do you want to update this contact ? Y(yes) : N(no)").lower()
            return main_menu()


def show_contact():
    for contact_id, person in contacts.items():
        print(person)
        return main_menu()
    

def main_menu():
    menu_selec = input(str("welcome to the Contacts App\n Please Select a menu:\n 1:Add a Contact\n 2:Update Contact\n 3:Delete Contact\n 4:Show all contacts\n: "))
    if menu_selec == "1":
        add_contact()
    elif menu_selec == "2":
        update_contact()
    elif menu_selec == "3":
        delete_user()
    elif menu_selec == "4":
        show_contact()
    else:
        print(f"Input invaild please try again")
        main_menu()



main_menu()