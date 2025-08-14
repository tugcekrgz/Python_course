name='Tuğçe'
surname='Karagöz'
age=21

#print('My name is '+name + ''+surname +'and I am' + age +'years old.')

#burada hata alırız çünkü age bir int değişkeni ve biz burada string toplama işlemi yapıyoruz.
#peki nasıl çözebiliriz?
#1- yukarıda tanımladığımız age değişkenin değerini string olarak atarız.
#2-print ile yazdıracağımız mesajda yaptığımız string toplama işleminde age değişkeninde veri tipi dönüşümü yaparız.

print('My name is '+name + ''+surname +'and \n I am' + str(age) +'years old.')

greeting='My name is '+name + ''+surname +'and I am' + str(age) +'years old.'

print(greeting)
print(greeting[0]) #M çıktısı verir.
print(len(greeting)) #43
print(greeting[42]) #.
print(greeting[-1]) #.

print(greeting[2:5])
print(greeting[3:])
print(greeting[:15])
print(greeting[2:35:2])