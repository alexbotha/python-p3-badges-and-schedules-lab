def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    y = []
    for names in names:
        y.append(f'Hello, my name is {names}.')
    return y

def assign_rooms(names):
    y = []
    value = 0
    for names in names:
        value = value + 1
        y.append(f"Hello, {names}! You'll be assigned to room {value}!")
    return y

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)
