# -*- coding: utf-8 -*-
"""

@author: idris ibrahim erten
"""
#substring
#substring : mesajın bir kısmını almak demektir.
#aşağıda değişkene bağlı bir mesaj verdik, o mesajın şimdi
#sadece ihtiyacımız olan kısmını alacağız.
#örneğin istiyoruz ki 0'dan 7. harfe kadar ver.
#neden 0'dan dedik çünkü başlangıçta ilk yazılanı sahil değildir.
#demekte. O yüzden bizde 0 dahil de ğil diyip 1.den dahildir 7'ye kadar dedik.

#substring örneği:
mesaj = "Merhaba dünya"
print(mesaj[0:7])

#mesela "aba dü" lazım bize,
mesaj = "Merhaba dünya"
print(mesaj[4:10])

#yani anlayacağınız kelimenin harflerini sayarak belirtmemiz gerekiyor.