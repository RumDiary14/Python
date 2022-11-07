a = 5
if a / 2 == 0:
    print("even number")
else:
    print("odd numer")

a = 5
print("even number") if a / 2 == 0 else print("odd number")


sound = "chin"
if sound == "meow":
    print("cat")
elif sound == "bark":
    print("dog")
elif sound == "chin":
    print("bird")
else:
    print("unknown animal ")


num = -781
type = ""
type2 = ""

if abs(num) // 10 == 0:
    type = "1"
elif abs(num) // 10 < 10:
    type = "2"
else:
    type = "3"
if num > 0:
    type2 = "positive"
else:
    type2 = "negative"
print("it is zero") if not num else print("it is a " + type2 + " value with " + type + " num")









