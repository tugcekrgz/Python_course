"""
Daire Alanı : πr²
Daire Çevresi: 2πr 

*Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.(π :3.14)"""

pi=3.14
r=float(input("lütfen yarı çapı giriniz: ")) #ondalıklı olabilir unutma direkt int yazma!
daireAlan= pi*(r**2)
daireCevre=2*pi*r

print(daireAlan)
print(daireCevre)

#print("Alanı: "+ daireAlan+"Çevresi: "+daireCevre)
#bunu yapabilmemk için değişkenleri str yapmak gerekli çünkü şu an float