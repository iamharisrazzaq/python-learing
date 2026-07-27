print("Hello, World!")

items = ["apple", "banana", "cherry", 1,2 ,False, True]

print(items)

items.append("orange") # add item in the last index of list

print(items)

items.insert(5, "grapes") # add item in the specific index of list
print(items)

items.remove("banana") # remove item from list
print(items)

items.pop(0) # remove item from specific index of list
print(items)

items.pop() # remove item from last index of list
print(items)

items.clear() # remove all items from list
print(items)

items = [1,2,3,4,4,5,6,6,6,6,6,7,8,1,1,1,1]
print(items.count(1)) # count the specific item in list

items.sort() # sort the list in ascending order
print(items)

items.sort(reverse=True) # sort the list in descending order
print(items)

items.reverse() # reverse the list
print(items)


 # return the index/location of specific item in list
print(items.index(6))