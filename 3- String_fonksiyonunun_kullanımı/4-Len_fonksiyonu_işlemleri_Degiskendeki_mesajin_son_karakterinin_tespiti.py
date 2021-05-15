# -*- coding: utf-8 -*-
"""

@author: idris ibrahim erten
"""

#Bu çalışmamızda ise mesela upuzuuuun bir metin var değişken içerisinde 
#sizlerinde bu değişkenin son karakterinin hangi karakter olduğuna 
#ihtiyacınız var o zaman ne yaparız.

#len fonksiyonuna başvuruyoruz. substringte nasıldı sistem lütfen substringi
#oturtmadan buraya gelmeyiniz. karakterleri biliyoduk. şunla şu aralığı 
#diyorduk. Bunda ise yeni bir değişken açarak içerisinde uzunluğu bul 
#bulunan uzunluktan 1 karakter çıkar. Kalanı yaz.

#örneğimiz:
mesaj = "idrisibrahimerten"
yeniMesaj = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj)

#gördüğünüz üzere son karakteri çıktı olarak yazdık.