#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yavaş Merhaba Dünya Simülasyonu
Her harf özeldir. Acele yok.
"""

import time
import random

def yavas_yaz(metin):
    print("Evrenin onayı bekleniyor...")
    time.sleep(2)
    for harf in metin:
        print(harf, end="", flush=True)
        # Her harfin kendi varoluşsal bekleyişi
        bekleme = random.uniform(0.5, 2.5)
        time.sleep(bekleme)
        if harf == " ":
            print("\n(boşluk da önemlidir, nefes alın)", end="")
            time.sleep(1)
    print("\n\nİşlem tamamlandı. Zaman iyi kullanıldı.")

if __name__ == "__main__":
    print("=== YAVAŞ MERHABA DÜNYA PROTOKOLÜ BAŞLATILDI ===")
    print("Dikkat: Bu işlem geri alınamaz ve hızlandırılamaz.")
    time.sleep(1.5)
    
    yavas_yaz("Merhaba Dünya")
    
    # Gizli not (hiç önemli değil)
    gizli = "Sadece merhaba demek istedik, başka hiçbir şey yok."
    # (aslında var: 'demokrasi' kelimesi 3 kez tekrarlanınca bir şey olur ama olmaz)
    
    print("\nProgram sona erdi. Şimdi gidip bir şeyler yapabilirsiniz.")
    print("Ya da yapmayabilirsiniz. Seçim sizin.")

# 
# Resmi olmayan resmi son:
# Damga: Yavaş ama emin adımlar
# Tarih: 06 Kasım 2026
# İsim: Kayyum Grok (ciddi)
# 
