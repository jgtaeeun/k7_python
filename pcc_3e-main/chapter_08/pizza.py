def make_pizza(size, *toppings):   #*toppings은 크기가 정해지지 않음, *toppings은 튜플임. 
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:   #toppings은 튜플이고,  topping은 튜플의 각 요소이다.
        print(f"- {topping}")

make_pizza(16, 'pepperoni')         #toppings('pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  #toppings('mushrooms', 'green peppers', 'extra cheese')