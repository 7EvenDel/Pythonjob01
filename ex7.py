def print_even_numbers(n):
    m = 6
    for i in range(-n, n, m):
        if i % 2 == 0:
            print(i)

n = int(input("Введіть число: "))

# Викликаємо функцію з заданим значенням n
print_even_numbers(n)
