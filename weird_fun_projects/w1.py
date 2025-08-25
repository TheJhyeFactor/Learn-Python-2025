import random

alphabet_both = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
number = tuple("12345678910")
special = ["!", "@", "$", "%", "&", "&"] 


def input_pas():
    pass_len = int(input("Please enter in the length you want you password to be: For secuirty the min lenght is 6 char long:\nEnter Lenght: "))
    if pass_len >= 6:
        print(f"{pass_len}")
    else:
        print("you suck")

input_pas()