class BankaMüsteri:
    def __init__(self, ad, soyad, sifre, bakiye, tcno):
        self.ad = ad
        self.soyad = soyad
        self.sifre = sifre
        self.bakiye = bakiye
        self.tcno = tcno

    def MüsteriKayit(self):
        self.ad = input("İsminizi giriniz: ")
        self.soyad = input("Soyadınızı giriniz: ")
        self.tcno = input("Tc kimlik numaranızı giriniz: ")
        self.sifre = input("Şifrenizi giriniz: ")
        self.bakiye = float(input("Bakiyenizi giriniz: "))  # Bakiye için float olarak kaydet
        print("Kayıt başarıyla tamamlandı")

    def BilgileriGuncelle(self):
        print("Bilgilerinizi güncellemek için aşağıdaki adımları takip edin:")
        self.ad = input("Yeni isminizi giriniz: ")
        self.soyad = input("Yeni soyadınızı giriniz: ")
        self.tcno = input("Yeni Tc kimlik numaranızı giriniz: ")
        self.sifre = input("Yeni şifrenizi giriniz: ")
        print("Bilgileriniz başarıyla güncellendi.")

    def MüşteriGiris(self):
        giris_tcno = input("Tc kimlik numaranızı giriniz: ")
        giris_sifre = input("Şifrenizi giriniz: ")
        if giris_tcno == self.tcno and giris_sifre == self.sifre:
            print("Giriş başarılı!")
            return True
        else:
            print("Hatalı Tc kimlik numarası veya şifre!")
            return False
    
    def BakiyeGuncelle(self, miktar):
        self.bakiye += miktar
        print("Bakiye güncellendi. Yeni bakiyeniz:", self.bakiye)

    def KayitSil(self, musteriler):
        tcno = input("Silmek istediğiniz müşterinin Tc kimlik numarasını giriniz: ")
        for musteri in musteriler:
            if musteri.tcno == tcno:
                musteriler.remove(musteri)
                print("Müşteri kaydı başarıyla silindi.")
                return
        print("Müşteri bulunamadı.")

def kaydet_musteriler(musteriler):
    with open("musteriler.txt", "w") as dosya:
        for musteri in musteriler:
            dosya.write(f"{musteri.ad},{musteri.soyad},{musteri.sifre},{musteri.bakiye},{musteri.tcno}\n")


def yukle_musteriler():
    musteriler = []
    try:
        with open("musteriler.txt", "r") as dosya:
            for satir in dosya:
                satir = satir.strip()
                if satir:  # Satır boş değilse devam et
                    ad, soyad, sifre, bakiye, tcno = satir.split(",")
                    try:
                        bakiye = float(bakiye)
                    except ValueError:
                        print("Hata: Geçersiz bakiye değeri. Varsayılan değer (0.0) atanacak.")
                        bakiye = 0.0  # Varsayılan bakiye değeri
                    musteri = BankaMüsteri(ad, soyad, sifre, bakiye, tcno)
                    musteriler.append(musteri)
    except FileNotFoundError:
        pass  # Dosya bulunamadığında bir şey yapma
    return musteriler


musteriler = yukle_musteriler()

while True:
    print("YunusBank'a hoşgeldiniz")
    print(""" 
1-   Yeni kayıt 
2-   Bilgileri güncelle
3-   Kayıtlı müşteri
4-   Kayıt silme
5-   Çıkış
    """)
    secilen_islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    if secilen_islem == "1":
        musteri = BankaMüsteri("", "", "", "", "")
        musteri.MüsteriKayit()
        musteriler.append(musteri)
        kaydet_musteriler(musteriler)
    elif secilen_islem == "2":
        giris_tcno = input("Tc kimlik numaranızı giriniz: ")
        giris_sifre = input("Şifrenizi giriniz: ")
        for musteri in musteriler:
            if musteri.tcno == giris_tcno and musteri.sifre == giris_sifre:
                print("Giriş başarılı! Hoş geldiniz.")
                musteri.BilgileriGuncelle()
                kaydet_musteriler(musteriler)
                break
        else:
            print("Hatalı Tc kimlik numarası veya şifre!")
    elif secilen_islem == "3":
        giris_tcno = input("Tc kimlik numaranızı giriniz: ")
        giris_sifre = input("Şifrenizi giriniz: ")
        for musteri in musteriler:
            if musteri.tcno == giris_tcno and musteri.sifre == giris_sifre:
                print("Giriş başarılı! Hoş geldiniz Sayın",musteri.ad ,musteri.soyad)
                while True:
                    print(""" 
1-   Bakiye Sorgula 
2-   Para Yatırma
3-   Para Çekme
4-   Çıkış
                    """)
                    secilen_islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
                    if secilen_islem == "1":
                        print("Mevcut bakiyeniz:", musteri.bakiye)
                    elif secilen_islem == "2":
                        miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
                        if miktar > 0:  # Negatif miktar girişini engelle
                            musteri.BakiyeGuncelle(miktar)
                            kaydet_musteriler(musteriler)
                        else:
                            print("Hatalı miktar girişi! Miktar pozitif olmalıdır.")
                    elif secilen_islem == "3":
                        miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
                        if miktar > 0 and miktar <= musteri.bakiye:  # Negatif ve bakiyeden fazla miktar girişini engelle
                            musteri.BakiyeGuncelle(-miktar)
                            kaydet_musteriler(musteriler)
                        elif miktar <= 0:
                            print("Hatalı miktar girişi! Miktar pozitif ve bakiyeden az olmalıdır.")
                        else:
                            print("Yetersiz bakiye!")
                    elif secilen_islem == "4":
                        print("Çıkış yapılıyor...")
                        break
                    else:
                        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir değer girin.")
                break
        else:
            print("Hatalı Tc kimlik numarası veya şifre!")
    elif secilen_islem == "4":
        print("Çıkış yapılıyor...")
        break
    elif secilen_islem == "4":
        giris_tcno = input("Tc kimlik numaranızı giriniz: ")
        giris_sifre = input("Şifrenizi giriniz: ")
        for musteri in musteriler:
            if musteri.tcno == giris_tcno and musteri.sifre == giris_sifre:
                print("Giriş başarılı! Hoş geldiniz ", musteri.ad,)
                musteri.KayitSil(musteriler)
                kaydet_musteriler(musteriler)
                break
        else:
            print("Hatalı Tc kimlik numarası veya şifre!")
    else:
        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir değer girin.")
