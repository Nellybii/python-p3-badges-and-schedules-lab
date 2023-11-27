def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(f"Hello, my name is {name}.")
    return badge_list

result = batch_badge_creator("yuda", "fames")
print(result)