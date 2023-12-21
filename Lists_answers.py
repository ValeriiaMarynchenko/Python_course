hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
user_nunber = (int(input("Enter an ineger to replace the middle number: ")))
hat_list[int(len(hat_list)//2)] = user_nunber
print(hat_list)
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))


my_list = [1, 7, 23, 34, 0]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

# Задайте розмірність двовимірного списку (кількість рядків і стовпців)
rows = 3
cols = 4

# Створіть двовимірний список за допомогою генератора списків
two_dimensional_list = [[0 for _ in range(cols)] for _ in range(rows)]

# Заповніть двовимірний список значеннями (це приклад, можна змінювати значення за бажанням)
value = 1
for i in range(rows):
    for j in range(cols):
        two_dimensional_list[i][j] = value
        value += 1

# Виведіть двовимірний список
for row in two_dimensional_list:
    print(row)



my_list = [1, 4, 6, 2, 7, 3]

swapped = True

while swapped:
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i +1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            
            print(my_list)

        else:
            swapped = False


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_1 = []

for i in range(len(my_list) - 1):
    if i not in list_1:
        list_1.append(i)
print(my_list)
print("The list with unique elements only:")
print(list_1)
