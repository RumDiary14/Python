
# Cyle While
counter = 5
while counter > 0:
    print("iteration, counter =", counter)
    counter = counter - 1
print("--------")
print(counter)

#Cycle For

for number in range(5):
    print(number)

# break and continue

for number in range(10):
    if number == 3:
        break
    print(number)

for number in range(10):
    if number == 3:
        continue
    print(number)

# examples

for number in range(101):
    if number == 0:
        continue
    elif number % 2 == 0:
        print(number)

counter = 0
end_value = 101
while counter < end_value:
    if counter % 2 == 0:
        print(counter)
    counter += 1

#example2

word = "hello"
for key in word:
    if key == "l":
        print("s")
    else:
        print(key)

#example3

start = 99
stop = 0
while start > stop:
    if start % 5 == 0:
        print(start)
    start -= 1
