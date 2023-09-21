
number1 = float(input("ilk kenar: "))

number2 = float(input("ikinci kenar: "))

number3 = float(input("ucuncu kenar: "))

if number1 == number2 == number3:
    print("eskenar ucgendir.")

elif number1 == number2 or number1 == number3 or number2 == number3:
    print("ikizkenar ucgendir.")

else:
    print("cesitkenar ucgendir.")
