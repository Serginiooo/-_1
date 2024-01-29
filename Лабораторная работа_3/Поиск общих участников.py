# TODO Напишите функцию find_common_participants
def find_common_participants(first,second,razdelitel=","):
    fgroup = first.split(razdelitel)
    sgroup = second.split(razdelitel)
    summ = list(set(fgroup).intersection(sgroup))
    return summ
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group,participants_second_group,"|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
