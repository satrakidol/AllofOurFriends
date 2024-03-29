paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

total_friends = paul_friends

for i in tina_friends:
    if i not in total_friends:
        total_friends.append(i)

print(total_friends)


