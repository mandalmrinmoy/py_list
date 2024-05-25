fruit_list=["Mango","Orange","Apple","Guava"]
print(fruit_list)
print(fruit_list[0:2])
print(fruit_list[-1])
change_fruit=fruit_list[1:2]=["Banana"]
print(change_fruit)
print(fruit_list)
fruit_list.insert(4,"Orange")
print(fruit_list)
fruit_list.append("Strawberry")
print(fruit_list)
for fruit in fruit_list:
    print(fruit)
if "Mango" in fruit_list:
    print("Here has a mango")