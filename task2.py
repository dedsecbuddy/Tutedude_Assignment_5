list = []
for i in range(1,11):
    list.append(i)

print(f"Original List : {list}")

list2 = list[0:5]
print(f"Extracted first five elements: {list2}")
list2.reverse()
print(f"Reversed extracted elements: {list2}")
