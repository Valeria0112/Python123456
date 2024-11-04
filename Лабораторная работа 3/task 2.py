# TODO Напишите функцию find_common_participants
def find_common_participants(str1_, str2_, n=","):
    set_first_group = set(str1_.split(n))
    set_second_group = set(str2_.split(n))
    common_list = set_first_group.intersection(set_second_group)
    common_list = list(common_list)
    common_list.sort()
    return(common_list)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, n="|"))


