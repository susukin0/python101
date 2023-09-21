sayi1 = int(input("ilk sayiyi giriniz: "))

sayi2 = int(input("ikinci sayiyi giriniz: "))

islem = str(input("hangi islemi yapmak istersin (*, +, -, /): "))

if islem == "+":
    print(sayi1 + sayi2)

elif islem == "-":
    print(sayi1 - sayi2)

elif islem == "/":
    print(sayi1 / sayi2)

elif islem == "*":
    print(sayi1 * sayi2)
    
else:
    print("gecersiz deger. ")

