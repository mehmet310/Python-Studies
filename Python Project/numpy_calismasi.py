#!/usr/bin/env python
# coding: utf-8

# <h1>Numpy Calismasi</h1>

# <h2>random integer sayilar uretilir,randint() </h2>

# In[1]:


import numpy as np #numpy kütüphanesinin dahil edilmesi


arr=np.random.randint(0,10,50)
print(arr)


# <h2>farkli verilerin cast edilmesi, dtype  </h2>

# In[2]:




# integerdan float veri tipine cast
arr=np.array([1,2,3.0,4,6],dtype="float")
print(arr)
# string'e cast
arr=np.array(["1",2.0,"3.0",4,6])
print(arr)


# <h2> sifir arrayi olusturmak zeros() </h2>

# In[3]:



arr=np.zeros([2,3]) # 2 boyutlu sifir arrayi
print(arr)
arr_2=np.zeros(3) # 1 boyutlu sifir arrayi
print(arr_2)
arr_3=np.zeros([1,2,3]) # n boyutlu
print(arr_3)


# <h2>istedigimiz veriler ile array olusturmak full() </h2>

# In[4]:




arr=np.full((2,4),4) # 2x4 matrisini 4 ile doldurur.
print(arr)
arr2=np.full((3,4,5),1) # 3 boyutlu 4x5lik matrisi 1 ile doldurur.
print(arr2)


# <h2>ardisik veri olusturmak,arange() </h2>

# In[5]:





arr=np.arange(1,31,2) # 1 den 31'e kadar(31 dahil degil) 2'li arttirim olur
print(arr)
arr2=np.arange(40,5,-5) # 40'dan 5'e(5 dahil degil) 5 azaltir.
print(arr2)


# <h2> linspace() ile düzenli veri bölmek</h2>

# In[6]:




array_1=np.linspace(1,20) # 1'den 20'ye(1 ve 20 dahil) default olarak 50 parcaya boler
print(array_1)
array_2=np.linspace(2,60,20) # 20 parcaya bolerek 60'a(2 ve 60 dahil) ulasir.
print(array_2)


# <h2>normal metodu ile normal dagilimdan yararlanmak </h2>

# In[15]:




array_1=np.random.normal(1,2,5) # 1=ort , 2=standart sapma, 5=dizi boyutu
print(array_1)
array_2=np.random.normal(3,2.5,10) 
# print(np.__dir__()) # numpy icin tum metotlar ...
print(array_2)


# <h2> reshape() ile yeniden boyutlandirma </h2>

# In[8]:


# reshape() ile yeniden boyutlandirma 

dizi=np.arange(1,11)
print(dizi.size) # size ile toplam boyutunu görebiliriz.
print(dizi.ndim) # ndim ile kac satir veya sütundan olustugunu gorebiliriz.
print(dizi)
dizi=dizi.reshape(2,5) #2x5lik yeniden boyutlandirma yapiliyor.
print(dizi)
dizi=dizi.reshape(5,2) # 5x2lik yeniden boyutlandirma yapiliyor.
print(dizi)


# <h2> birim matris kullanimi,eye() </h2>

# In[9]:



dizi=np.eye(3,3) #3x3luk birim matrisi olusturma
print(dizi)
dizi_2=np.eye(2,4) #2x4'luk birim matrisi olusturma
print(dizi_2)
dizi_3=np.eye(4) # otomatik 4x4luk birim matris olusturur
print(dizi_3)


# <h2> array ile ilgili calismalar</h2>

# In[10]:




arr=np.array([1,2,3,4,5,5,6,3,2,10,12,54,76,23,21,55,100])
new_arr=arr[0:16:2] # 1'den 16.indexe kadar 2'ser arttirarak ulastik
print(new_arr)
new_arr_2=arr[17:2:-1] # 17'den 2.indexe kadar 1'ser azaltarak ulastik
print(new_arr_2)

arr2=np.array([[1,2],[2,3],[3,4],[5,6]])

dizi=arr2*2 # her elemani 2 ile carpar
print(dizi)
dizi1=arr2.reshape(4,2) #yeniden boyutlandirma
dizi2=dizi+dizi1 # matris toplami
dizi3=dizi*dizi1 #matris carpimi
print(dizi2)

print(dizi3)
dizi4=arr2[0:2,1:3] # yeni dizide indexleme
print(dizi4)
dizi5=dizi.reshape(-1) # tek boyuta indirgenir.
print(dizi5)

arr3=np.array([[4,5],[6,7],[7,8],[8,9]])

conc_arr=np.concatenate([arr2,arr3]) # iki array birlestirilir.
print(conc_arr)

print("------------")
conc_arr1=np.concatenate([arr2,arr3],axis=1)  # eksen ile birlestirme
print(conc_arr1)
print("------------")
stack_arr=np.stack([arr2,arr3],axis=1) # stack metodu ile concatenate islemi
print(stack_arr)
print("------------")

h_stack_arr=np.hstack([arr2,arr3]) # yatay birlestirme conc_arr1 ile ayni sonucu verecektir
print(h_stack_arr)

print("------------")
arr4=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
split_arr=np.split(arr4,[1,6]) # split metodu ile belli kisimlar ayrildi.
print(split_arr)
print("------------")

split_arr2=np.split(arr3,[0,2],axis=1) # eksen vererek split yapmak
print(split_arr2)

print("------------")

a=np.arange(25).reshape(5,5)
print(a)
print("--------------")
b=np.vsplit(a,[2,15])[2].shape # dikey olarak ayirir.
print(b)
print("---------------")
c=np.hsplit(a,[1,10])[0] #yatay olarak ayirir
print(c)
print("---------------")

d=np.argsort(a) # key kisimlari döndürür
print(d)
print("---------------")
filterr=(a>1) & (a<9) # filter mantigi kullanmak
print(filterr)
print("---------------")
filter_2=np.all((a>=4) & (a<17)) # all metodu
print(filter_2)
print("---------------")
filter_3=np.any((a>=4) | (a<17)) # any metodu
print(filter_3)
print("---------------")
summ=np.sum(a,axis=0) #sum metodu axis=0 ile dikey toplam yapilir
print(summ)
print("---------------")
summ2=np.sum(a,axis=1) #axis=1 yatay toplam yapıilir
print(summ2)
print("---------------")
product_1=np.prod(a,axis=0) #prod metodu
print(product_1)
print("---------------")
product_2=np.prod(a,axis=1) #yatay carpim
print(product_2)
print("---------------")

x=np.arange(10).reshape(2,5)
y=x.copy() #copy metodu,önceki listeyi degistirmez!
y[0][2]=23
print(y)
print(x)
print("---------------")
z=x.view() #view metodu, önceki listeyi degistirir!
z[1][3]=11
print(z)
print(x)


# In[ ]:




