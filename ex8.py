import math

def count_password_combinations(num_cells):
    num_symbols = 25
    return math.factorial(num_symbols) // math.factorial(num_symbols - num_cells)

num_cells = 6

combinations = count_password_combinations(num_cells)
print("Кількість можливих комбінацій пароля:", combinations)