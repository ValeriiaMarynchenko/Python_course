#Виконайте форматування виведення списку чисел Фібоначчі за допомогою f-рядку

fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Виведення списку чисел Фібоначчі
print(fibonacci)

#Виконайте форматований вивід матриці за допомогою f-рядка та потрійних лапок за потреби.
#Вирішення питання минулого уроку(потрібно замість спроби виведення всього двувимірного списку виводити 
#тільки рядок, створений за допомогою вкладеного циклу`for`)

list1 = []

for i in range(10):
    row = []
    for ii in range(10):
        row.append(ii**3)
    list1.append(row)
    print(i, row)

#print(list1)

#Виконайте форматований вивід за допомогою f-рядка

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

# Виконайте форматування зворотнього сортування 
my_list = [1, 7, 23, 34, 0]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)