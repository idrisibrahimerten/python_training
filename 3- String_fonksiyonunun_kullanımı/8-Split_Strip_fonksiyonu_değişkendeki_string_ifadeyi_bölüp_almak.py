# -*- coding: utf-8 -*-
"""

@author: idris ibrahim erten
"""
#Split ve Strip 
#split bölmek, strip şerit anlamına gelmekte.
#burada öğrenmemiz gereken şeridi böl.
#aşağıdaki örneğimizde şeridimize bilgiler verip
# ';' ile böleceğiz ve çıktıda böldüğümüz kısımdan veri isteyeceğiz.

bilgi = "     i.ibrahim;erten;istanbul-üni;istanbul ".strip()
print(bilgi.split())
print("Adı = " + bilgi.split(";")[0])

#gördüğünüz üzere önce tüm bilgiler yazıldı sonra istediğim kısmı verdi.
#"[0]" hangi kısmı istiyorsanız sayısını yazmalısınız.
#NOT!
#PYTHON'da veri başlangıcı 0'dan başlar. 