def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory.keys(): # loop which iterates over each of the values
            inventory[k] = inventory[k]+1
        else:
            inventory[k] = 1
    
    
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v),k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))


bag = {'gold coin':42,'rope':1}
dragonLoot =['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(bag, dragonLoot)
displayInventory(bag)
