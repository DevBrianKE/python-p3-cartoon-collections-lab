def roll_call_dwarves(dwarves):
    # Loop through each dwarf, using enumerate to track index starting at 1
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def roll_call_dwarves(dwarves):
    # List comprehension to print dwarves with numbering
    [print(f"{index + 1}. {dwarf}") for index, dwarf in enumerate(dwarves)]





def summon_captain_planet(planeteer_calls):
    # Use a loop to capitalize each call and add '!' at the end
    new_calls = []
    for call in planeteer_calls:
        new_calls.append(call.capitalize() + '!')
    return new_calls

def summon_captain_planet(planeteer_calls):
    # List comprehension to capitalize each call and add '!'
    return [call.capitalize() + '!' for call in planeteer_calls]





def long_planeteer_calls(calls):
    # Loop through the list of calls and check if any call is longer than 4 characters
    for call in calls:
        if len(call) > 4:
            return True
    return False

def long_planeteer_calls(calls):
    # Use any() and list comprehension to check if any call is longer than 4 characters
    return any(len(call) > 4 for call in calls)




def find_the_cheese(snacks):
    # List of known cheeses
    cheeses = ["cheddar", "gouda", "camembert"]
    
    # Use a loop to find the first cheese in the list
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None

def find_the_cheese(snacks):
    # Use list comprehension and next() to find the first cheese or return None
    cheeses = ["cheddar", "gouda", "camembert"]
    return next((snack for snack in snacks if snack in cheeses), None)