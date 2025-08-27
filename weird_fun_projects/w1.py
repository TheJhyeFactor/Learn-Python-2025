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
    print("Now get ready for your passowrd hehe you ready ????")
    passowrd_gen(master_lst, pass_len)
        

   # need to update this to join the elements in the array when printed for the user also should maybe make 3 random choices and then join then selectino from each tuple making sure its = to the users len request then join the elemtns idk 
def passowrd_gen(pas_char, pas_len):
    n = int(pas_len)
    print(type(n))
    passwrdf = random.choices(pas_char, k=n)
    
    print(f"here is your password: {passwrdf}")

# just going to be a qucik one to night we are going to join the elments that are returned from the output of the pass genrator so the user can have an easy time reading / copying their pasword / we might also make it save as a file

input_passlen()