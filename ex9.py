my_list = [1, 2, 3, 4, 5]

my_list.extend([3, 6, 7])
print("Розширений список:", my_list)

my_list.insert(1, 33333)
print("Список з вставкою:", my_list)

my_list.reverse()
print("Список у зворотньому порядку:", my_list)

my_list.append(3)
print("Список з 3 в кінці:", my_list)

my_list.remove(3)
print("Список після видалення першого елементу зі значенням 3:", my_list)

my_list.sort()
print("Список у порядку збільшення:", my_list)

my_list.clear()
print("Очищений список:", my_list)