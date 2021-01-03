#fancy pizza order 

#pizza order


#--- basis price ---

#small pizza = 12
#medium pizza = 15
#medium pizza = 20

# ---price for pepperoni depending on pizza size ---
#pepperoni small = 3
#pepperoni medium = 5
#pepperoni large = 8

# --- price for cheese depending on pizza size ----
#extra_cheese_small =3
#extra_cheese_med =5
#extra_cheese_med =8

from collections import namedtuple

Price = namedtuple("Price", ["standard", "luxury", "VIP"])

#what is the underscore for?
size_list = Price._fields # the underscore is IMPORTANT

basis = Price(1200,1500,2000)
extra_bed = Price(30,50,90)
one_child = Price(40,50,80)
bottle_wine =Price(10,22,33)
spa =Price(150,270,350)

# ask for pizza size

def accept_answer(question, list_of_possible_answers):
    """takes user input and renders it lower case for processing
    """
    while True:
        answer = input(question + " >>>")
        if answer.lower() in [a.lower() for a in list_of_possible_answers]:
            return answer.lower()
            
print("pizza sizes and prices:")            
for size in size_list:
    print(size, "cost", getattr(basis, size))
size = accept_answer("How big do you want your resort? Type\nstandard\nluxury\nVIP\n", size_list )
cost = getattr(basis, size)        
for extra in ("extra_bed","one_child", "bottle_wine","spa"):
    #what does locals do?
    #what is the notation for[extra]?
    #how do I use getattr?
    price_for_extra = getattr(locals()[extra], size) # use globals() if inside a class/function
    print(extra, " will cost:", price_for_extra)
    if accept_answer(f"Do you want {extra}? (yes or no)", ["yes", "no"]) == "yes":
        cost += price_for_extra
print("Your total cost is:", cost)



