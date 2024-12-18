# ввод трёх целых чисел.
first = int(input("Введите первое число"))
second = int(input("Введите второе число"))
third = int(input("Введите третье число"))
# Проверка условий
if first==second==third: # Равенство всех трех чисел
    print(3)
elif first==second or first==third or second==third: # равенство двух из трех чисел
    print(2)
else: # Ни одно из условий не выполняется
    print(0)