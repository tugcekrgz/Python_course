message=' Hello There.My name is Tugce Karagoz '

a=message.upper() #stringin tüm harfleri büyür.

b=message.lower() #stringin tüm harfleri küçülür.

c=message.title() #her kelimenin ilk harfi büyür.

d=message.capitalize() #stringin sadece ilk harfi büyük olur.

e=message.strip() 

f=message.split('.') #stringi . dan ayırır parantezin içi boş olursa boşluklardan ayırır

g='*'.join(g)

index=message.find('Tugce') #stringin içinde "Tugce" nin başladığı indexi verir.
print(index)

isFound=message.startswith('B') #string B ile mi başlar?
print(isFound)

isFound=message.endswith('B') #string B ile mi biter?
print(isFound)

message=message.replace('Tugce','Erhan')
print(message)
message=message.replace(' ','*')
print(message)

message=message.replace('ç','c').replace('ö','o').replace(' ','-')

message=message.center(50,'*')
