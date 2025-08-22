items = ["apple","banana","mango"]

print(items)
print(items[0])
print(items[0:3])

items.append("kiwi")
print(items)

i = "kiwi"
if i in items:
    print("Item present ")
else:
    print("Item not present ")

while True:
    print("Enter choice : 1.Add 2.Remove 3.Display 4.Exit")
    ch =input("Enter your choice")
    if ch=="1":
        item = input("Enter item to add : ")
        items.append(item)
        print("Item added successfully")
    elif ch=="2":
        items.remove("kiwi")
        print("Kiwi removed ")
        print(items)
    elif ch=="3":
        print(items)

    