#!/usr/bin/env python
calculation_of_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_units}"
    elif num_of_days == 0:
        return "You entered a 0, please enter a valid positive number"

def validate_and_exec():
    if user_input.isdigit():
        user_input_number =  int(user_input)
        calculated_value = days_to_units(user_input)
        print(calculated_value)
    else: 
        print("Your input is not a valide number. Don't ruin my program!")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_exec()