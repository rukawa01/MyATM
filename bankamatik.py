

ömerHesap = {
    "sifre": "123456",
    "ad": "ömer",
    "hesapNo": "123456",
    "bakiye": 3000,
    "ekBakiye": 2000,
    "borc": 6000
}
ahmetHesap = {
    "sifre": "456789",
    "ad": "ahmet",
    "hesapNo": "789456",
    "bakiye": 5000,
    "ekBakiye": 3000,
    "borc": 0
}

hesaplar = [ömerHesap, ahmetHesap]


def islem():
    islem = input(
        "Para çekmek istiyorum 'c'\nPara yatırmak istiyorum 'y'\nPara Babası olmak istiyorum (Nah Olursun)\nBorcumu ödemek istiyorum 'b'")
    return islem


def paraCek(hesap):
    print(f"Merhaba {hesap['ad']} Ne yapmak istiyorsunuz")

    print("Ne kadar çekmek istiyorsunuz")

    bakiyeTalep = int(input("Bakiyeyi giriniz"))
    if bakiyeTalep < hesap["bakiye"]:
        hesap["bakiye"] = hesap["bakiye"] - bakiyeTalep
       # hesap["bakiye"].append(hesap["bakiye"])
        print(f"Yeni Bakiyeniz : {hesap['bakiye']}")
    elif bakiyeTalep < hesap["bakiye"] + hesap["ekBakiye"]:
        hesap["ekBakiye"] = hesap["bakiye"]+hesap["ekBakiye"] - bakiyeTalep
       # hesap["EKBakiye"].append(hesap["ekBakiye"])
        print(
            f"Bakiyeniz sıfırlanmıştır Ek Hesaptaki bakiyeniz {hesap['ekBakiye']} ")
    else:
        print("Bakiyenizde o kadar paranız mevcut değil")


def paraYatir(hesap):
    yatrılanPara = int(input("Ne kadar yatırmak istiyorsunuz"))
    hesap["bakiye"] = hesap["bakiye"]+yatrılanPara
   # hesap["bakiye"].append(hesap["bakiye"])
    print(f"Yeni Bakiyeniz : {hesap['bakiye']}")


def borcOde(hesap):
    print(f"Hesabınızdaki Borç bilgisi : {hesap['borc']}")
    if hesap["borc"] < hesap["bakiye"] + hesap["ekBakiye"]:
        ode = int(input("Ne kadarını ödemek istiyorsunuz"))

    if hesap["borc"] < hesap["bakiye"]:
        hesap["bakiye"] = hesap["bakiye"] - ode
        # Bunarın hiçbiri çalışmıyor hesap güncellenmiyor diğer döngüye girdiğinde
        # videoda güncelleniyor izle
      #  hesap["bakiye"].append(hesap["bakiye"])
        print(f"Borcunuz ödenmiştir\nYeni Bakiyeniz : {hesap['bakiye']}")
    elif hesap["borc"] < hesap["bakiye"] + hesap["ekBakiye"]:
        hesap["ekBakiye"] = hesap["bakiye"] + hesap["ekBakiye"] - ode
      #  hesap["EkBakiye"].append(hesap["ekBakiye"])
        print(
            f"Bakiyeniz sıfırlanmıştır ve Borcunuz ödenmiştir\nYeni Ek Bakiyeniz : {hesap['ekBakiye']}")
    else:
        print("Hesabınızda yeteri kadar para bulunmamaktadır")
        isim = input("Dilerseniz 'y' ye basarak para yatırabilirisiniz")
        if isim == 'y':
            paraYatir(ömerHesap)
            borcOde(ömerHesap)


def hesapAdiDondurucu():
    hesapGecerleMi = False
    anlikHesap = ""
    hesapAdi = input("Hesap adınıı eksiksiz giriniz : ")
    for i in hesaplar:
        if hesapAdi == i["ad"]:
            hesapGecerleMi = True
            anlikHesap = i

    if hesapGecerleMi == True:
        while True:
            InputSifre = input("Şifreyi giriniz : ")
            if InputSifre == anlikHesap["sifre"]:
                return anlikHesap
                break
            else:
                print(
                    "Şifrenizi Eksik yada Hatalı tuşlama yaptınız\nBaşlangıç Ekranına Yönlendiriliyorsunuz")

    else:
        print(
            "Böyle bir kullanıcı bulunamadı\nBaşlangıç Ekranına Yönlendiriliyorsunuz")
        hesapAdiDondurucu()


hesap = hesapAdiDondurucu()
while True:

    isleminDegeri = islem()
    if isleminDegeri == "y":
        paraYatir(hesap)
        cevap = input("Başka bir işlem yapmak ister misiniz 'e'/'h'")
        if cevap == 'e':
            continue
        else:
            break

    elif isleminDegeri == "c":

        paraCek(hesap)
        cevap = input("Başka bir işlem yapmak ister misiniz 'e'/'h'")
        if cevap == 'e':
            continue
        else:
            break
    elif isleminDegeri == "b":

        borcOde(hesap)
        cevap = input("Başka bir işlem yapmak ister misiniz 'e'/'h'")
        if cevap == 'e':
            continue
        else:
            break
    else:
        print(
            "Eksik yada Hatalı tuşlama yaptınız\nBaşlangıç Ekranına Yönlendiriliyorsunuz")
