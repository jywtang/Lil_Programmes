def addtoInventory(inventory, stuff):
    for i in range(len(stuff)):
        inventory.setdefault(stuff[i],0)
        inventory[stuff[i]] += 1

def displayInventory(inventory):
    itemNum = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v), k)
        itemNum += v
    print('Total number of items: ' + str(itemNum))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addtoInventory(inv, dragonLoot)
displayInventory(inv)
