"""
for döngüsü ile liste öğlerin ortalaması
"""
list_1=[10,20,30,40,50]
total=0
for i in list_1:
    total+=i
avg=total/len(list_1)
print(avg)

"""
fonksiyon calismasi-1
"""
def otopark_ucret(saat):

    ucret=0
    if saat<=1:
        ucret=5
    elif saat>1 and saat<=5:
        ucret+=saat*4
    else:
        ucret+=saat*3
    return ucret

print("Otoparkimiza hosgeldiniz. Ucret tarifemiz su sekildedir: ")
print("1 saat icin 5 tl",
          "1-5 arasi saat basi 4 tl",
          "5 saatten fazlasi saat basi 5 tl'dir")
    
print("kac saat kalacaksiniz?")
saat=int(input())
ucr=otopark_ucret(saat)
print(ucr)


"""
basit dictionary calismasi
"""

dic={1:"mehmet",2:"arikan",3:"memo"}

for i,j in dic.items():
    print(i,".nci oge",j,"dir.")
 
x={a for a in dic.values()}
print(x)


"""
lambda foksiyon örnekleri
"""


x=lambda a: a*a
print(x(2))

x=lambda a,b,c:(a*b*c)**3
print(x(2,3,4))

"""
fonksiyon calismasi-2
"""

def rectangle(m,n):
    for i in range(m):
        
            print("*"*n)
    
rectangle(2,4)


"""
fonksiyon calismasi-3
"""

def closest(n):
    lists=[1,3,5,6,10]
    x=[b for b in lists if n>b]
    largest=0
    for i in x:
        if i==x:
            x==i
    print(i)


closest(8)    


"""
fonksiyon calismasi-4
"""



def dortgen_bul(a,b,c,d):
    if(a==b==c==d):
        print("Kare veya eskenar dörtgen")
    elif((a==b) and (c==d) or (a==c) and (b==d) or (a==d) or (b==c)):
        print("Dikdörtgen")
    elif((a!=b) and (c!=d) or (a!=c) and (b!=d) or (a!=d) or (b!=c)):
        print("Yamuk")
    else:
        print("girdiginiz degerlere göre dörtgen belirtmemektedir.")
print("birinci kenari giriniz.")
a=eval(input())
print("ikinci kenari giriniz.")
b=eval(input())
print("üçüncü kenari giriniz.")
c=eval(input())
print("dördüncü kenari giriniz.")
d=eval(input())
dortgen_bul(a,b,c,d)

"""
list calismasi-1
"""
import random
name=["Ahmet","Mehmet","Ali","Nurdan","İrem","Kerem","Gülşah","Serra"]
surname=["Arikan","Oz","Yaprak","Yılmaz","Koc","Sabancı","Oguzcan","Torun"]

x=random.choice(name)
y=random.choice(surname)
for i in range(len(x)):
    for j in range(len(y)):
      x=random.choice(name)
      y=random.choice(surname)
      print("Seçilen isim:",x ,"ve soyisim:", y)


"""
fonksiyon calismasi-5
"""

def factorial(n):
    number=1
    for i in range(n,1,-1):
        number*=i
        
    print(number)
    return number
print("Bir sayı giriniz.")
num=int(input())
factorial(num)

"""
fonksiyon calismasi-6
"""

def dikdortgen_cevre(a,b):
    return (2*(a+b))
def dikdortgen_alan(a,b):
    return (a*b)
print("dikdortgen icin kisa kenari giriniz.")
a=int(input())
print("dikdörtgen icin uzun kenari giriniz.")
b=int(input())

print("Cevre: ",dikdortgen_cevre(a,b))

print("Alan: ",dikdortgen_alan(a,b))


"""
fonksiyon calismasi-7
"""

def prime_nums(a,b):
    count=0
    for i in range(a,b+1):
        if i>1:
          for j in range(2,i):
            if(i%j)==0:
                break
          else:
            print("prime nums: ",i)
            count+=1
    print(f"There are {count} numbers in these range.")

print("enter first number: ")
a=int(input())
print("enter second number: ")
b=int(input())
prime_nums(a,b)

"""
class calismasi-1
"""
class hesap_makinesi:

 def topla(self,a,b):
    return (a+b)
 def cikar(self,a,b):
    return (a-b)
 def bolme(self,a,b):
    if b==0:
        print("sifira bölme olamaz!")
        return 0
    
    return (a/b)
 def carpma(self,a,b):
    return (a*b)
 def mod_alma(self,a,b):
        if b==0:
           print("sifira bölme olamaz!")
           return 0
        return (a%b)
 def us_alma(self,a,b):
    return (a**b)
 def sqroot(self,a,b):
    return (pow(a,b))**0.50

hm=hesap_makinesi()
print("Hesap makinesine hosgeldiniz.")
print("birinci sayiyi giriniz.")
a=int(input())
print("ikinci sayiyi giriniz.")
b=int(input())

while True:
   print("lütfen yapmak istediginiz islemi giriniz.")
   print("1-toplama,2-cikarma,3-bölme,4-carpma,5-mod almak,6-üs almak,7-karekök almak, 0-program çikisi")
   secenek=str(input())
   if secenek=='1':
     print(hm.topla(a,b))
   elif secenek=='2': 
     print( hm.cikar(a,b))
   elif secenek=='3':
     print(hm.bolme(a,b))
   elif secenek=='4':
     print(hm.carpma(a,b))
   elif secenek=='5':
     print(hm.mod_alma(a,b))
   elif secenek=='6':
     print( hm.us_alma(a,b))
   elif secenek=='7':
     print(hm.sqroot(a,b))
   elif secenek=='0':
       print("program sona erdi.")
       break
   else:
     print("yanlis sayi girdiniz.tekrar deneyiniz!")
else:
 print("yanlis fonksiyon!")
 
"""
fonksiyon calismasi-8
"""

def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
  
def permutation(a,b):
    return fact(a)/(fact(a-b))

def combination(a,b):
    return permutation(a,b)/(fact(b))

print("birinci sayiyi giriniz.")
a=int(input())
print("ikinci sayiyi giriniz.")
b=int(input())
print("Permutasyon: ",permutation(a,b))
print("Kombinasyon: ",combination(a,b))

"""
class calismasi-2
"""

import math
class Circle:
    def perimeter(self,r):
        return 2*math.pi*r
    def area(self,r):
        return math.pi*r*r
c=Circle()
print("Enter radius: ")
r=int(input())
print("Area: ",c.area(r))
print("Perimeter: ",c.perimeter(r))

"""
fonksiyon calismasi-9
"""

def choice():
    print("hosgeldiniz... <T>iyatro için T'yi, <S>inema için S'yi seçiniz.")
    sec=str(input())
    print("Eğer ögrenciyseniz , E'ye degilseniz H'yi seciniz.")
    ogCheck=str(input())
    bakiye=100 # elimizdeki bakiyenin 100 tl olduğunu varsayıyoruz.
    if (sec=='T' or sec=='t') and (ogCheck=='H' or ogCheck=='h'):
        print("Tiyatroya hosgeldiniz. 10 tl'lik ücret alimi olacaktır.")
        bakiye=bakiye-10
        print("Kalan bakiyeniz: ",bakiye)
    elif (sec=='S' or sec=='s') and (ogCheck=='H' or ogCheck=='h'):
        print("Sinemaya hosgeldiniz. 15 tl'lik ücret alimi olacaktır.")
        bakiye=bakiye-15
        print("Kalan bakiyeniz: ",bakiye)
    elif (sec=='T' or sec=='t') and (ogCheck=='E' or ogCheck=='e'):
        print("Tiyatroya hosgeldiniz. 50% indirim yapilarak ücret alimi olacaktır.")
        bakiye=bakiye-(10*0.5)
        print("Kalan bakiyeniz: ",bakiye)
    elif (sec=='S' or sec=='s') and (ogCheck=='E' or ogCheck=='e'):
        print("Sinemaya hosgeldiniz. 50% indirim yapilarak ücret alimi olacaktır.")
        bakiye=bakiye-(15*0.5)
        print("Kalan bakiyeniz: ",bakiye)
    else:
        print("yanlis giris yaptiniz!")
        
choice()

"""
genel calisma-1
"""

print("Enter a number")
check=int(input())
count=0
for i in range(2,check):

    if (check%i)==0:
        count+=1
        break

if (count!=0):
    print("not prime")
else:
    print("prime")
    
"""
class calismasi-3
"""

class TekCift:
     
    def tek_toplam(self,a):
        count=0
        for i in range(1,a):
          if i%2!=0:
            count+=i
        return count

    def cift_toplam(self,a):
        count_2=0
        for i in range(1,a):
         if i%2==0:
            count_2+=i
        return count_2

tc=TekCift()
print("bir sayi giriniz.")
a=int(input())
print("Tek sayilarin toplami: {0}".format(tc.tek_toplam(a)))
print("Cift sayilarin toplami: {0}".format(tc.cift_toplam(a)))


"""
genel calisma-2
"""

import random
print("---Sayi Tahmin oyununa hosgeldiniz.---")
while True:
  print("0-100 araliğinda bir sayi giriniz. ")
  sayi=int(input())
  sayi_2=random.randint(0,100)
  if sayi<0 and sayi>100:
      print("Lütfen 0-100 arasi sayi giriniz.")
      break
  if sayi==sayi_2:
      print("Tebrikler sayiyi buldunuz!")
      break
  else:
      print(f"sayiyi bulamadiniz. sayimiz: {sayi_2} idi.")


"""
fonksiyon calismasi-10
"""

def even_check(ilkSayi,sayi):
    count=0
    sayac=0
    for i in range(ilkSayi,sayi+1):
        if i%2==0:
            count+=i
            sayac=sayac+1
    avg=count/sayac
    print("Girilen çift sayiya kadar ki toplam: {}".format(count))
    print("Ortalama: {}".format(avg))
print("ilk sayiyi giriniz.")
fs=int(input())
print("son sayiyi giriniz.")
s=int(input())
even_check(fs,s)

"""
list calisma-2
"""

from math import pi
print("Cm olarak sayi giriniz.(inc'e) çevrilecek")
sayi=int(input())
print("Bit olarak sayi giriniz.(byte'a) çevrilecek.")
bit=int(input())
list_mix=[pi,(sayi*2.54),bit*8,"windows"]
for i in list_mix:
    print(i)

"""
list calismasi-3
"""

days=["Monday","Tuesday","Wednesday","Thursday","Friday"]

days.append("Saturday")
days.insert(2,"memoday")
print(days)
days.remove("memoday")
print(days)
# print(days.__dir__()) printing list methods
days.extend(["Arikanday","Mehmetday"])
print(days)
days.pop(6)
print(days)
days.sort()
print(days)

print(days.index("Mehmetday"))


"""
list calismasi-4
"""

list_1=[10,11,12,13,14,15,16,17,18,19,20]
list_2=[21,22,23,24,25]
new_list=list_1+list_2
for i in new_list:
    if i%4==0:
       print(i)
count=0
