# importing a module and defining it as n
import names as n 

# Creating a function called names
def names(): 
    x = input("Press enter to get a name: ")
    if x == "":
        print(n.get_full_name())

# executing the same function 1000000 ** 2 times
for i in range(1000000 ** 2):
    names()
    