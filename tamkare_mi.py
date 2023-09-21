
baslangic = int(input("kactan itibaren karekok kontrolu istiyorsun: "))

bitis = int(input("kaca kadar istiyorsun: "))

for i in range(baslangic, bitis + 1):

    karekok = i ** 0.5

    
    if karekok.is_integer():
        print(i)
