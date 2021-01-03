#pizza order

#small pizza = 12
#medium pizza = 15
#medium pizza = 20


#pepperoni small = 3
#pepperoni medium = 5
#pepperoni large = 8

#extra_cheese_small =3
#extra_cheese_med =5
#extra_cheese_med =8

start_order = input('''
                    size of pizza you want?\n
                    s = small\n
                    m = medium\n
                    l =large\n\n
                    ''')
if start_order == 's':
    bill = 12
    print (f'Your bill is now: ${bill}')
if start_order == 'm':
    bill = 15
    print (f'Your bill is now: ${bill}')
if start_order == 'l':
    bill = 20
    print (f'Your bill is now: ${bill}')
topping = input('''Do you want pepperoni?
                   y = yes 
                   n = no\n\n''')
if topping == 'n':
    #TODO: figure out how to handle the no answers!
    #continue
if topping == 'y' and start_order =='s':
    bill += 3
    print (f'You want pepperoni. So, your bill is now: ${bill}')
if topping == 'y' and start_order =='m':
    bill += 6
    print (f'You want pepperoni. So, your bill is now: ${bill}')
if topping == 'y' and start_order =='l':
    bill += 9
    print (f'You want pepperoni. So, your bill is now: ${bill}')
extra_cheese = input('''Do you want extra cheese?\n
                        y =yes\n
                        n=no\n''')
if extra_cheese == 'n':
    continue
if extra_cheese == 'y' and start_order =='s':
    bill += 2
    print(f'You want extra cheese. So, your bill is now: ${bill}')
if extra_cheese == 'y' and start_order =='m':
    bill += 4
    print(f'You want extra cheese. So, your bill is now: ${bill}')
if extra_cheese == 'y' and start_order =='l':
    bill += 6
    print(f'You want extra cheese. So, your bill is now: ${bill}')
    print (f'''Thank you for placing your order with\n
    PizzaAutoMat!\n\n
    Your bill is now: ${bill}''')     
else:
    print (f'''Thank you for placing your order with\n
    PizzaAutoMat!\n\n
    Your bill is now: ${bill}''')




