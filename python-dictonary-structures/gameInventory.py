stuff = {'rope': 0, 'torch': 0, 'gold coin': 42, 'dagger':1, 'arrow': 12}


def inventory_display(inventory_stuff):
    print('Inventory:')
    item_total = 0
    for key, value in inventory_stuff.items():
        print(key + ' ' + str(value))
        item_total += value
    print('Total number of items: ' + str(item_total))


def add_to_inventory(inventory, added_items):
    for key in added_items:
        inventory.setdefault(key, 0)  # default is to add nothing
        inventory[key] = inventory[key] + 1  # add 1 to keys
    return inventory


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin']

inventory_display(stuff)
add_to_inventory(stuff, dragon_loot)
print()
print()
inventory_display(stuff)




