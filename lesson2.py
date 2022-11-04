counter = 0
if counter < 10:
    counter += 1
else:
    pass # заглушка, котороя позволяет не возвращаться к "if"
print(counter)

# elif= one more if
animal = "bird"
if animal == "cat":
     print("Meow")
elif animal == "dog":
    print("Wof")
elif animal == "bird":
    print("twit")
else:
    print("I don't know this animal")

    # тернарный оператор
# example 1
value = 1 if 2 > 2 else 0
print(value)

# example 2

value = 10
result_value_greater_than_zero = True if value > 0 else False
print(result_value_greater_than_zero)

#example 3

product_price = 90
if product_price > 1000:
    product_price *= 0.9
elif product_price > 500:
    product_price *= 0.95
elif product_price > 100:
    product_price *= 0.97
print(product_price)

# тернарный

value_str = ""
print(None if value_str == "" else value_str)
# вывести "None" если пустая строка , а если другое то вывести значение
# print(None if value_str == "" else value_str) = print(None if not value_str else value_str)

#example

first_value = None
second_value = 2
operator = "/"
if first_value is None or second_value is None:
    print("Can't divide None value")
else:
    if operator == "+":
        print(first_value + second_value)
    elif operator == "-":
        print(first_value - second_value)
    elif operator == '/':
        if second_value == 0:
             print("Can't divide by 0")
        else:
         print(first_value / second_value)
    elif operator == "*":
     print(first_value / second_value)
    else:
     print("Operator is wrong. Choose from given: + = / *")
