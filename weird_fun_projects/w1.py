import random

alphabet_both = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
number = tuple("12345678910")
special = ("!", "@", "$", "%", "&", "&")

master_lst = tuple(alphabet_both + number + special)


def input_passlen():
    pass_len = int(input("Please enter in the length you want you password to be: For secuirty the min lenght is 6 char long:\nEnter Lenght: "))
    
    if pass_len >= 6:
        print(f"{pass_len}")
    else:
        print(f"Hey bro not cool man, maybe you should retake maths becasue {pass_len} is smaller than 6 -_- \n Now i am going to give you another chance to get it right:\n")
        input_passlen()
        

    
#def passowrd_gen():

#random.choice()
#pass



print(master_lst)