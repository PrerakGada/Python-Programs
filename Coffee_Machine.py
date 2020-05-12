def print_machine_state(machine_ingredients):
    print("The coffee machine has:")
    for ingredient in machine_ingredients.keys():
        if ingredient != 'money':
            print(machine_ingredients[ingredient], 'of', ingredient)
    print('$' + str(machine_ingredients['money']) + ' of money')
    pass


def buy_coffee(machine_ingredients):
    # mapping coffee type options
    coffee_type_options = {'1': 'espresso', '2': 'latte', '3': 'cappuccino'}
    # setting coffee costs
    coffee_cost = {
        'espresso':
            {
                'water': 250,
                'milk': 0,
                'coffee beans': 16,
                'money': -4,
                'disposable cups': 1
            },
        'latte':
            {
                'water': 350,
                'milk': 75,
                'coffee beans': 20,
                'money': -7,
                'disposable cups': 1
            },
        'cappuccino':
            {
                'water': 200,
                'milk': 100,
                'coffee beans': 12,
                'money': -6,
                'disposable cups': 1
            }
    }
    option = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n'))
    coffee_type = coffee_type_options.get(option)
    if coffee_type:
        ingredients_left = {'enough': True}
        for ingredient in machine_ingredients.keys():
            ingredients_left[ingredient] = machine_ingredients[ingredient] - coffee_cost[coffee_type][ingredient]
            if ingredients_left[ingredient] < 0:
                print('Sorry, not enough', ingredient)
                ingredients_left['enough'] = False
        if ingredients_left['enough']:
            print('I have enough resources, making you a coffee!')
            for ingredient in machine_ingredients.keys():
                machine_ingredients[ingredient] = ingredients_left[ingredient]
    pass


def fill_ingredients(machine_ingredients):
    machine_ingredients['water'] += int(input('Write how many ml of water do you want to add:\n'))
    machine_ingredients['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    machine_ingredients['coffee beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
    machine_ingredients['disposable cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    pass


def take_machine_money(machine_ingredients):
    print('I gave you $' + str(machine_ingredients['money']))
    machine_ingredients['money'] = 0
    pass


def implement_machine_action(action, machine_ingredients):
    if action == 'buy':
        buy_coffee(machine_ingredients)
    elif action == 'fill':
        fill_ingredients(machine_ingredients)
    elif action == 'take':
        take_machine_money(machine_ingredients)
    elif action == 'remaining':
        print_machine_state(machine_ingredients)
    pass


def turn_on_coffee_machine(machine_ingredients):
    action = None
    while action != 'exit':
        action = input('Write action (buy, fill, take, remaining, exit):\n').lower()
        implement_machine_action(action, machine_ingredients)
    return


# defining initial amount of ingredients
initial_machine_ingredients = {
    'water': 400,
    'milk': 540,
    'coffee beans': 120,
    'disposable cups': 9,
    'money': 550
}

turn_on_coffee_machine(initial_machine_ingredients.copy())
