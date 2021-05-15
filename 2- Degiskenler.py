# -*- coding: utf-8 -*-
"""

@author: İdris İbrahim ERTEN
"""

#Değişkenler
#Değişkenler değerleri saklamak için kullanılan kod bütünüdür.
#Asıl kullanma ihtiyacımı adı sabit bir değişkeni değiştirmek istediğimizde
#kodun her yerinden değiştirmemizi önler. Sadece değişkeni değiştirince
#iş çözüme kavuşur.

a = 1       #integer tam sayı değeri
b = 1.19    #float ondalıklı sayı değeri
c = 'iie'   #string yazı.

#yukarda hangi değerlerde olduğunu gösterdik.
#burada ise type değerlerini sorarak söylediklerimiz doğru mu? Test edeceğiz.
type(a)     #tip işaretlemesi
type(b)     #tip işaretlemesi
type(c)     #tip işaretlemesi

#burada ise tiplerimizin çıktısını ekrana yazmasını istiyoruz.
print("a değerimiz -> " + str(type(a)))  #tip ekrana yazsın.
print("b değerimiz -> " + str(type(b)))  #tip ekrana yazsın.
print("c değerimiz -> " + str(type(c)))  #tip ekrana yazsın.

#NOT!
#Hiç bir zaman string ve float veya bunlar integer değerle işlem yapamaz.
#eğer tipleri uygun hale getirmezseniz yani string stringle, float floatla,
#integer integer'la TypeError hatası alırsınız. 