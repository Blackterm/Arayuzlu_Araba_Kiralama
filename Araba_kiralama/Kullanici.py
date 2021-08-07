import sqlite3
import locale
import datetime
an = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')


class KULLANICI():
    def __init__(self, isim, soyisim, kullanici_adi,mail, sifre, dogum_tarih, ehliyet_tarih):
        self.isim = isim
        self.soyisim = soyisim
        self.kullanici_adi = kullanici_adi
        self.mail = mail
        self.sifre = sifre
        self.dogum_tarih = dogum_tarih
        self.ehliyet_tarih = ehliyet_tarih


class Data():

    def __init__(self):
        self.connection()

    def connection(self):
        self.baglanti = sqlite3.connect("Kiralama.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists Sistem (isim TEXT,soyisim TEXT,kullanici_adi TEXT,mail TEXT,sifre TEXT,dogum_tarih TEXT,ehliyet_tarih TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def uye_giris(self, kullanici):
        self.cursor.execute("Insert into Sistem Values(?,?,?,?,?,?,?)",
                            (kullanici.isim, kullanici.soyisim,kullanici.kullanici_adi, kullanici.mail, kullanici.sifre, kullanici.dogum_tarih, kullanici.ehliyet_tarih))
        self.baglanti.commit()

    def kullanici_cekme(self, kullanici_adi):
        self.cursor.execute("Select * From Sistem where kullanici_adi = ? ", (kullanici_adi,))
        user = self.cursor.fetchone()
        user1 = KULLANICI(isim=user[0],soyisim=user[1],kullanici_adi=user[2],mail=user[3],sifre=user[4],
                          dogum_tarih=user[5],ehliyet_tarih=user[6])
        return user1
    def kullanici_adi(self, kullanici_adi):
        self.cursor.execute("Select * From Sistem where kullanici_adi= ?", (kullanici_adi,))
        user = self.cursor.fetchone()
        return user

    def kullanici_mail(self, mail):
        self.cursor.execute("Select * From Sistem where mail= ?", (mail,))
        user = self.cursor.fetchone()
        return user

    def yeni_kullanici(self,isim,soyisim,kullanici_adi,mail,sifre,dogum_tarih,ehliyet_tarih):

        yeni_kullanici = KULLANICI(isim,soyisim,kullanici_adi,mail,sifre,dogum_tarih,ehliyet_tarih)
        Data().uye_giris(yeni_kullanici)



    def kullanici_giris(self):
        giris_hakki = 2
        while True:
            kullanici_adi = input("Kullanıcı adınız:")
            kullanici_sifre = input("Şifreniz:")
            self.cursor.execute("Select * From Sistem where kullanici_adi= ? and sifre = ?", (kullanici_adi, kullanici_sifre))
            user = self.cursor.fetchone()
            if user:
                if user[2] == "admin":
                    return 1
                else:
                    user1 = KULLANICI(isim=user[0],soyisim=user[1],kullanici_adi=user[2],mail=user[3],sifre=user[4],
                          dogum_tarih=user[5],ehliyet_tarih=user[6])
                    return user1
            elif giris_hakki == 0:
                return 2
            else:
                print("Mailiniz ve şifreniz yanlış:")
                giris_hakki -= 1
