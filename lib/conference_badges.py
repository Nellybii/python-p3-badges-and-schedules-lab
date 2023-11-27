def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(f"Hello, my name is {name}.")
    return badge_list
# print(batch_badge_creator(["Arel", "Carol"]))
def assign_rooms(names):
    visitors = []
    for i, name in enumerate(names, start=1):
        visitors.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return visitors

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for room_assignment in rooms:
        print(room_assignment)
    
printer(["Arel", "Carol", "Guido", "Charles"])

