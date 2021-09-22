bakiye=1000
islem=None
def paraYatirmak(bakiye):
    ypara=int(input("Lütfen yatırmak istediğiniz miktarı giriniz :"))
    bakiye+=ypara
    print("Bakiyeniz : " , bakiye)
def paraCekmek(bakiye):
    cpara=int(input("Lütfen çekmek istediğiniz miktarı giriniz : "))
    if cpara<=bakiye:
        print("Kalan Bakiyeniz:" , bakiye)
    else:
        print("Bakiyenizden fazla para çekemezsiniz")
def krediCekmek():
    a=int(input("Lütfen çekmek istediğiniz miktarı giriniz :"))
    print("Başarıyla kredi çektiniz")

while (islem!="Q"):
    islem = str(input("Lütfen yapmak istediğiniz işlemi seçiniz \n1-Para Yatırmak\n2-Para Çekmek\n3-Kredi Çekmek\nÇıkmak için büyük Q yazınız\n"))
    islem.upper()
    if islem == "1":
        paraYatirmak(bakiye)
    elif islem == "2":
        paraCekmek(bakiye)
    elif islem == "3":
        krediCekmek()
