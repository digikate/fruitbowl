def get_integer(m):
    my_integer = 0
    get_result = True
    while get_result:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("you have not entered an integer")
            continue
        get_result = False
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def double_loop_print(L):
    for i in range(0, len(L)):
        output = "{} : {}".format(i, L[i])
        print(output)
        for j in range(0, len(L[i])):
            output = "{} : {}".format(j, L[i][j])
            print(output)


def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:10} ----- {:10} ----- {:<10}".format(L[i][0], L[i][1], L[i][2])
        print(output)


def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{:3} : {:10} {:10} {:10}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)


def add_new_entry(L):
    print("Start adding new entry.")
    fruit = get_string("Please enter the new fruit:")
    colour = get_string("Please enter the fruit colour:")
    number = get_integer("Please enter the number of this fruit:")
    new_L = [fruit, colour, number]
    L.append(new_L)


def update_fruit(L):
    print_with_indexes(L)
    my_index = get_integer("Please enter the index number to update the fruit:")
    new_fruit = get_string("Please enter the new name:")
    old_fruit = L[my_index][0]
    L[my_index][0] = new_fruit
    output_message = "{} has now been changed to {}.".format(old_fruit, new_fruit)
    print(output_message)


def update_colour(L):
    print_with_indexes(L)
    my_index = get_integer("Please enter the index number to update the fruit colour:")
    new_colour = get_string("Please enter the new fruit colour:")
    old_colour = L[my_index][1]
    L[my_index][1] = new_colour
    output_message = "{} has now been changed to {}.".format(old_colour, new_colour)
    print(output_message)

def update_number(L):
    print_with_indexes(L)
    my_index = get_integer("Please enter the index number to update the number of fruit:")
    new_number = get_integer("Please enter the new number:")
    old_number = L[my_index][2]
    L[my_index][2] = new_number
    output_message = "{} has now been changed to {}.".format(old_number, new_number)
    print(output_message)

def input_action():
    my_input = int(input("Please choose an option"))
    return my_input
def menu():
    my_l = [
        ["Apple", "Red", 5],
        ["Pear", "Green", 7],
        ["Mango", "Yellow/Orange", 2],
        ["Kiwi Fruit", "Brown", 9],
        ["Peaches", "Yellow", 3]
    ]

    my_menu = '''
    1 : Adding a new entry
    2 : Update fruit
    3 : Update colour
    4 : Update number
    5 : Print fruit bowl
    0 : Quit
    '''
    run = True
    while run is True:

        print(my_menu)
        user_choice = input_action()
        if user_choice == 1:
            add_new_entry(my_l)
        elif user_choice == 2:
            update_fruit(my_l)
        elif user_choice == 3:
            update_colour(my_l)
        elif user_choice == 4:
            update_number(my_l)
        elif user_choice == 5:
            single_loop_print(my_l)
        elif user_choice == 0:
            run = False
            print("Thank you")
        else:
            print("Unrecognised entry")


menu()




