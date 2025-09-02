
#This is going to use sys time & if its x time in the Am good morining X time in the Afternoon good afternoon or X time goodnight, A basic if else statment


print('this is going to say hello')


def gh():
    g = input("Please enter in a letter: ")
    
    
    #this is always going to be true due to how we handle our input, so really a needless check
    if type(g) == str:
        print(f"You entered: {g}")
    else:
        print("Why")

gh()

