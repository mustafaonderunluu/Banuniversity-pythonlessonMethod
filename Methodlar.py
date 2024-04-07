# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:17:30 2024

@author: lenovo
"""

#Methodlar

def selamlama():
    print("merhaba")
    
selamlama()

type(selamlama) #Function
type(selamlama()) #NoneType

def selamlama2(isim):
    print("Merhaba",isim)
    
selamlama2("Onder")
selamlama2() #Hatalı

def toplama(a,b,c):
    print("Toplam : ",a+b+c)
    
toplama(10, 20, 30)
toplama(30,52,15)
toplama(30,52,15,15) #Hatalı
toplama(150, 85)#◘hatalı

#Return

def toplama2(a,b,c):
    return(a+b+c)

toplama2(10, 5, 6)

def UcKatı(sayi):
    return(sayi*3)

UcKatı(50)

#Def Parametre

def selamlama3(isim="isimsiz"):
    print("Merhaba",isim)
    
selamlama3("Önder")



def BilgileriGetir(ad="Bilgi Yok",
                   soyad="Bilgi Yok",
                   no="Bilgi Yok"):
    print(ad,soyad,no)
    
BilgileriGetir()

BilgileriGetir("Önder", "Ünlü",152)
BilgileriGetir(152,"Önder") #Veri Kayması
BilgileriGetir("ünlü","Önder") 

#Parametreler

def toplama3(*Parametreler):
    toplam=0
    print("Parametreler: ",Parametreler)
    for i in Parametreler:
        toplam +=i
    return toplam


toplama3(15,25,78,-625,45,24,12,857,254)

#Yerel ve Glabol Değişkenler

a=10
def fonksiyon():
    a=20
    print("Fonksiyonun içindeki değer",a)
fonksiyon()
print("Fonksiyonun dışındaki değer: ",a)

a = 10
def fonksiyon():
    global a
    a=20
    print("Fonksiyonun içindeki değer",a)
fonksiyon()
print("Fonksiyonun dışındaki değer: ",a)


#List Comprehension

list=[1,2,3,4,5]
list2 = []
for i in list:
    list2.append(i)
print(list2)

list3=[i for i in list] #ekleme
print(list3)

list4=[i*3 for i in list] #3 katını alma
print(list4)
     
list5=[(1,2),(3,5),(5,6)]

list6=[i*j for i,j in list5] #Çarpma

m = "YBS"
list7 =[i for i in m]

m = "YBS"
list7 =[i*5 for i in m]

#Lambda

Uckatı2= lambda x : x*3
Uckatı2(5)

toplam4= lambda x,y,z : x+y+z
toplam4(5,9,8)

#Asal mı ?
while True: #Döngüye sokulacak (kullanıcıdan sayı isteyip)
    def AsalMi(sayi):
     if sayi==1:
        return False
    
     elif (sayi==2):
        return True
     else:
        for i in range(2,sayi):
            if(sayi % i ==0):
                return False
            return True
AsalMi(113)
AsalMi(154)
AsalMi(142)

#Tam Bölenler

def TamBolen(sayi):
    tambolenler = []
    for i in range(2, sayi+1):
        if sayi % i == 0:
            tambolenler.append(i)
    print("Tam Bölenler :",tambolenler)
 
TamBolen(158)







    

    