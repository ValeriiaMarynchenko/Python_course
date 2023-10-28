#Задача: Підрахувати суму парних чисел в заданому діапазоні.

#Потрібно використати цикл for, щоб пройтися по числах у заданому діапазоні, та умову if,
# щоб перевірити, чи число парне.

#--------------------------------------------------------------------
# Задайте діапазон чисел
start = 1
user_number = (int(input("Enter a number: "))) #запитуємо у користувача число яке буде останнім в діапазоні

# Ініціалізуйте змінну для збереження суми
sum_of_evens = 0

# Використайте цикл for для перебору чисел у діапазоні
for num in range(start, user_number + 1):
    # Перевірте, чи число парне
    if num % 2 == 0:#( % - обчислення залишку від ділення)
        sum_of_evens += num

# Виведення суми парних чисел
print("Сума парних чисел в діапазоні:", sum_of_evens)
#--------------------------------------------------------------------

#Задача: Визначити, скільки разів певне слово зустрічається у рядку.

#Тут можна використати цикл for, щоб перевірити кожне слово в рядку, та умову if, щоб порівняти 
#його з цільовим словом.
#--------------------------------------------------------------------
# Заданий рядок
text = "Бабин біб розцвів у дощ — буде бабі біб у борщ."

# Задане слово, яке потрібно знайти
word_to_count = "біб"

# Ініціалізуйте лічильник
counter = 0

# Використайте цикл for для подання рядка на слова
words = text.split()
for word in words:
    # Перевірте, чи слово співпадає зі словом для лічильника
    if word.strip(".,") == word_to_count:
        counter += 1

# Виведення кількості знайдених слів
print("Слово", word_to_count, "зустрілося", counter,  "разів.")
#--------------------------------------------------------------------

#Задача: Визначити, скільки разів потрібно подвоїти число, щоб воно перевищило певну межу.

#Ця задача може бути вирішена за допомогою циклу while, де ми будемо подвоювати число та перевіряти, 
#чи воно вже перевищило межу. Умова if використовується для перевірки цієї умови.

#--------------------------------------------------------------------
# Задайте початкове число та межу
initial_number = int(input("Яке число треба подвоювати: "))
limit = int(input("Яка межа подвоєння: "))

# Ініціалізуйте лічильник кількості подвоєнь
count = 0
#варіант 1
# Використайте цикл while для подвоєння числа та перевірки межі
while initial_number <= limit:
    initial_number *= 2
    count += 1

# Виведення кількості подвоєнь
print("Число подвоєно", count, "разів, щоб перевищити межу", limit, ".")

# Задайте початкове число та межу
initial_number = int(input("Яке число треба подвоювати: "))
limit = int(input("Яка межа подвоєння: "))

# Ініціалізуйте лічильник кількості подвоєнь
count = 0
# варіант 2
# Використайте цикл for для подвоєння числа та перевірки межі
for count in range(count, limit):
    if initial_number > limit: #перевіряємо чи не перевищило подвоєне число ліміт
        break #якщо перевищило виходимо з циклу, в тіло умовної конструкції нічого не дописуємо
    initial_number *= 2 # якщо умова не виконана, подвоюємо число
    count += 1


# Виведення кількості подвоєнь
print("Число подвоєно", count, "разів, щоб перевищити межу", limit, ".")






