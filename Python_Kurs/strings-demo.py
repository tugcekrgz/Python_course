website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizinde kaç karakter bulunmaktadır?

print(len(course)) #benim 

result=len(course) #hoca
print(result)

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10]) #benim

result=website[7:10] #hoca
print(result)

# 3- 'website' içinden com karakterlerini alın.

print(website[-4:-1])#benim yanlış sonuç verdi

result=website[22:25] #hoca1
print(result)

length=len(website) #hoca2
result=website[length-3:length]
print(result
)
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

print(course[:15]) #benim 1.soru
print(course[43:59]) #benim 2.soru

print(course[0:15]) #hoca 1.soru
print(course[:15]) # hoca 1.soru
print(course[-15:]) #hoca 2.soru



# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(course[::-1]) #benim 

result=course[::-1] #hoca
print(result)

#NOT!!
s='12345' *5
print(s[::5])
#########################


name, surname, age, job = 'Bora','Yılmaz',32,'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz,Yaşım 32 ve mesleğim mühendis.'

print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job} .')       #benim
print('Benim adım {} {}, Yaşım {} ve mesleğim {} .'.format(name,surname,str(age),job)) #benim 

result="Benim adım"+ name+ "" + surname+ ",Yaşım"+str(age)+"ve mesleğim"+job  #hoca
print(result)

result='Benim adım {0} {1},Yaşım {2} ve mesleğim {3}.'.format(name,surname,str(age),job) #hoca
result=f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job} .'

# 7-'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

#a="Hello world"
#print(a.upper(w)) benim

s='Hello world'          #hoca
s= s[0:6] + 'W'+ s[-4:]
print(s)

s='Hello world'    #hoca
s.replace('w','W') 

s = 'Hello world'      #gpt
index = s.index('w')   
s = s[:index] + s[index].upper() + s[index+1:]
print(s)  # hello World


# 8-'abc' ifadesini yan yana 3 defa yazdırın.

print('abc'*3) #benim

result='abc ' *3 #hoca
