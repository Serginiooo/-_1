users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
Dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
Dictionary["Общее количество"] = len(users)
Dictionary["Уникальные посещения"] = len(set(users))
print(Dictionary)
