import sys,Res_rc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow
import webbrowser
import sqlite3
import Mail
import Kullanici
import Rastgele_kod
import locale
import time
import datetime
import Admin
import Aktif_araba
import Arabalar
an = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')


bilgi=[]
fiyat_bilgi=[]
araba_bil=[]
class Giris_ekrani(QMainWindow):


    def __init__(self):
        super(Giris_ekrani, self).__init__()
        loadUi("Giris-ekran.ui",self)
        self.Sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Giris_buton.clicked.connect(self.giris_ekran)
        self.Sifre_unuttum.clicked.connect(self.sifre)
        self.Kayit_olmak.clicked.connect(self.kayit)
        self.Cikis_buton.clicked.connect(self.cikis)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))




    def giris_ekran(self):

        adi = self.Kullanici_adi.text()
        par = self.Sifre.text()



        baglanti = sqlite3.connect("Kiralama.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Select * From Sistem where kullanici_adi = ? and sifre = ?", (adi, par))
        data=self.cursor.fetchall()

        if len(data) == 0:
            self.Geri_bildirim.setText("Şifre veye kullanıcı adı yanlış")
        else:
            self.Geri_bildirim.setText("HOŞGELDİN!"+adi)
            bilgi.append(adi)
            git = kisi_ekran()
            widget.addWidget(git)
            widget.setCurrentIndex(widget.currentIndex() + 1)




    def cikis(self):
        app.exit(app.exec())

    def kayit(self):
        git = kayit_ekran()
        widget.addWidget(git)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def sifre(self):
        login = Sifre_sorgu()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Sifre_sorgu(QWidget):
    def __init__(self):
        super(Sifre_sorgu, self).__init__()
        loadUi("Sifremi-unuttum_python.ui",self)
        self.Giris_buton.clicked.connect(self.sifre_sorgu)
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Geri_donus.clicked.connect(self.geri)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))

    def geri(self):
        login = Giris_ekrani()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def sifre_sorgu(self):
        mail = self.Kullanici_adi.text()
        Mail.MAIL().kullanici_sifre_istek(mail)

    def cikis(self):
        app.exit(app.exec())


class kayit_ekran(QWidget):
    def __init__(self):
        super(kayit_ekran, self).__init__()
        loadUi("kayit_ekran.ui",self)
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Geri_donus.clicked.connect(self.geri)
        self.Giris_buton.clicked.connect(self.kayit)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
    def kayit(self):

        adi = self.isim.text()
        if len(adi) == 0:
            self.Geri_bildirim.setText("Lütfen geçerli bir isim giriniz.")
        else:
            soyisim = self.soyisim.text()
            if len(soyisim) == 0:
                self.Geri_bildirim.setText("Lütfen geçerli bir soyisim giriniz.")
            else:
                kullanici_adi = self.kullanici_adi.text()
                if kullanici_adi == "":
                    self.Geri_bildirim.setText("Lütfen geçerli bir kullanıcı adı giriniz.")
                else:
                    kullanici_aadi = Kullanici.Data().kullanici_adi(kullanici_adi)
                    if kullanici_aadi:
                        self.Geri_bildirim.setText("Zaten böyle bir kullanıcı mavcut...")
                    else:
                        mail = self.mail.text()
                        mail_kontrol = mail.find("@")
                        if mail == "" or mail_kontrol == -1:
                            self.Geri_bildirim.setText("Lütfen geçerli bir mail giriniz.")
                        else:
                            kullanici_mail = Kullanici.Data().kullanici_mail(mail)
                            if kullanici_mail:
                                self.Geri_bildirim.setText("Böyle bir mail zaten mevcut...")
                            else:
                                sifre = self.sifre.text()
                                if len(sifre) <= 5:
                                    self.Geri_bildirim.setText("Şifreniz en az 6 haneli olmalıdır.")
                                else:
                                    dogum_tarih = self.dogum_tarih.text()
                                    if len(dogum_tarih) == 0:
                                        self.Geri_bildirim.setText("Lütfen geçerli bir doğum tarihi giriniz.")
                                    else:
                                        bu_gun = datetime.datetime.strftime(an, '%d %m %Y')

                                        date_format = "%d %m %Y"
                                        dogumtarih = datetime.datetime.strptime(dogum_tarih, date_format)
                                        bugun = datetime.datetime.strptime(bu_gun, date_format)
                                        fark = bugun - dogumtarih
                                        if 6574 > fark.days:
                                            self.Geri_bildirim.setText("Yaşınız 18'den küçük kayıt olamazsınız...")
                                        else:
                                            ehliyet_tarih = self.ehliyet_tarih.text()
                                            if len(ehliyet_tarih) == 0:
                                                self.Geri_bildirim.setText("Lütfen geçerli bir ehliyet tarihi giriniz.")
                                            else:
                                                git = bilgilendirme()
                                                widget.addWidget(git)
                                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                                Kullanici.Data().yeni_kullanici(adi, soyisim, kullanici_adi, mail,
                                                                                     sifre, dogum_tarih, ehliyet_tarih)
                                                Rastgele_kod.Rastgele().kod_kontrol(mail)


    def cikis(self):
        app.exit(app.exec())

    def geri(self):
        login = Giris_ekrani()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class mail_dogrulama(QWidget):
    def __init__(self):
        super(mail_dogrulama, self).__init__()
        loadUi("mail_dogrulama.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Geri_donus.clicked.connect(self.geri)
        self.Giris_buton.clicked.connect(self.mail_dogru)


    def geri(self):
        login = Giris_ekrani()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cikis(self):
        app.exit(app.exec())

    def mail_dogru(self):
        mail_verfy = self.mail_dogrulama.text()
        mail = self.mail_adres.text()
        mail_kontrol = mail.find("@")
        if mail == "" or mail_kontrol == -1:
            self.Geri_bildirim.setText("Mail alanı boş bırakılamaz.")
        else:
            if mail_verfy == "":
                self.Geri_bildirim.setText("Kod alanı boş bırakılamaz.")
            else:
                dogrulama = Rastgele_kod.Rastgele().kod_sorgu(mail_verfy)
                if dogrulama == 2:
                    self.Geri_bildirim.setText("Lütfen geçerli bir kod giriniz.")
                else:
                    self.Geri_bildirim.setText("Mail doğrulandı.")
                    time.sleep(2)
                    Mail.MAIL().Yeni_kullanici_mesaj(mail)
                    time.sleep(2)
                    app.exit(app.exec())


class bilgilendirme(QWidget):
    def __init__(self):
        super(bilgilendirme, self).__init__()
        loadUi("bilgilendirme.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.mail_dogru)
        self.Geri_bildirim.setText("Kayıdınız başarıyla gerçekleşti !")
        self.Geri_bildirim_2.setText("Mail doğrulamak için tamam'ı tıklayınız.")

    def mail_dogru(self):
        git = mail_dogrulama()
        widget.addWidget(git)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cikis(self):
        app.exit(app.exec())


class bilgilendirme2(QWidget):
    def __init__(self):
        super(bilgilendirme2, self).__init__()
        loadUi("bilgilendirme.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.cikis)
        fiyat = fiyat_bilgi[0]
        self.Geri_bildirim.setText("Ekstra ödeyeceğiniz miktar:{}TL".format(fiyat))
        self.Geri_bildirim_2.setText("Ödeme yapmak için yönlendiriliyorsunuz.")



    def cikis(self):
        app.exit(app.exec())


class bilgilendirme3(QWidget):
    def __init__(self):
        super(bilgilendirme3, self).__init__()
        loadUi("bilgilendirme.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.ekran1)
        self.Geri_bildirim.setText("Üzerinize kayıtlı araba bulamadık")


    def ekran1(self):
        git = kisi_ekran()
        widget.addWidget(git)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cikis(self):
        app.exit(app.exec())


class bilgilendirme4(QWidget):
    def __init__(self):
        super(bilgilendirme4, self).__init__()
        loadUi("bilgilendirme.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.cikis)
        self.Geri_bildirim.setText("Araba kullanırken emniyet kemeri takmayı\nUNUTMAYIN..!\nToplam ücretiniz:{}TL".format(araba_fiyat[-1]))




    def cikis(self):
        app.exit(app.exec())


class kisi_ekran(QWidget):
    def __init__(self):
        super(kisi_ekran, self).__init__()
        loadUi("kisi_bilgi.ui",self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.araba_kiralama)
        self.Giris_buton_2.clicked.connect(self.bilgi)
        mesaj = bilgi[0]
        self.Geri_bildirim.setText(mesaj.upper())

    def araba_kiralama(self):
        git = araba_satis()
        widget.addWidget(git)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def bilgi(self):
        gelen = bilgi[0]
        kisi = Kullanici.Data().kullanici_cekme(gelen)
        sorgu = Aktif_araba.Aktif_araba().kisi_araba_sorgu(kisi.kullanici_adi)

        if sorgu==1:
            git = bilgilendirme3()
            widget.addWidget(git)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            git = araba_bilgi()
            widget.addWidget(git)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def cikis(self):
        app.exit(app.exec())


class araba_bilgi(QWidget):
    def __init__(self):
        super(araba_bilgi, self).__init__()
        loadUi("araba-teslim.ui",self)
        self.Cikis_buton.clicked.connect(self.cikis)
        self.onay_buton.clicked.connect(self.islemler)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        gelen = bilgi[0]
        kisi = Kullanici.Data().kullanici_cekme(gelen)
        sorgu = Aktif_araba.Aktif_araba().kisi_araba_sorgu(kisi.kullanici_adi)
        kisi_isim = kisi.isim
        self.bilgilendirme.setText("Sayın {} teslim etmek istediğiniz araba".format(kisi_isim.upper()))
        self.model.setText("Arabanın modeli:{}".format(sorgu.model))
        self.plaka.setText("Arabanın plakası:{}".format(sorgu.plaka))
        self.akilometre.setText("Arabayı aldığınızda ki kilometresi:{}".format(sorgu.Aldigi_kilometre))
        self.teslimtarih.setText("Arabayı teslim etme tarhiniz:{}".format(sorgu.Teslim_tarih))


    def islemler(self):
        gelen = bilgi[0]
        kisi = Kullanici.Data().kullanici_cekme(gelen)
        sorgu = Aktif_araba.Aktif_araba().kisi_araba_sorgu(kisi.kullanici_adi)
        araba = Arabalar.Data().araba_sorgu(sorgu.plaka)
        bu_gun = datetime.datetime.strftime(an, '%d %m %Y')

        date_format = "%d %m %Y"
        a = datetime.datetime.strptime(sorgu.Teslim_tarih, date_format)
        b = datetime.datetime.strptime(bu_gun, date_format)
        kilometre_bilgi = self.gkilometre.text()
        fark = b - a
        fiyat = fark.days * araba.ucret
        fiyat_bilgi.append(fiyat)
        if fiyat >0:
            git = bilgilendirme2()
            widget.addWidget(git)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            app.exit(app.exec())
        Arabalar.Data().araba_kilometre_guncelleme(kilometre_bilgi, sorgu.plaka)
        Admin.Admin().araba_kilometre_guncelleme(kilometre_bilgi, bu_gun, sorgu.araba_id)
        time.sleep(2)
        Aktif_araba.Aktif_araba().araba_cikar(sorgu.araba_id)



    def cikis(self):
        app.exit(app.exec())



class araba_satis(QWidget):
    def __init__(self):
        super(araba_satis, self).__init__()
        loadUi("araba-kiralama.ui", self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.c180.clicked.connect(self.araba1)
        self.megan.clicked.connect(self.araba2)
        self.era.clicked.connect(self.araba3)
        self.Cikis_buton.clicked.connect(self.cikis)





    def araba1(self):
        kullanici_adi = bilgi[0]
        user = Kullanici.Data().kullanici_cekme(kullanici_adi)
        bu_gun = datetime.datetime.strftime(an, '%d %m %Y')

        date_format = "%d %m %Y"
        a = datetime.datetime.strptime(user.ehliyet_tarih, date_format)
        b = datetime.datetime.strptime(bu_gun, date_format)
        fark = b - a
        araba_varmi = Arabalar.Data().araba_sorgu("38CAN001")
        araba_aktif = Aktif_araba.Aktif_araba().araba_sorgu("38CAN001")
        if araba_aktif:
            self.Geri_bildirim.setText("Araba kullanımda.")
        else:
            if araba_varmi.kullanim_gun >= fark.days :
                self.Geri_bildirim.setText("Yeterli bir ehliyete sahip değilsiniz.")
            else:
                araba = "Merdeces"
                araba2="38CAN001"
                araba_bil.append(araba)
                araba_bil.append(araba2)
                git = araba_onaylama()
                widget.addWidget(git)
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def araba2(self):
        kullanici_adi = bilgi[0]
        user = Kullanici.Data().kullanici_cekme(kullanici_adi)
        bu_gun = datetime.datetime.strftime(an, '%d %m %Y')

        date_format = "%d %m %Y"
        a = datetime.datetime.strptime(user.ehliyet_tarih, date_format)
        b = datetime.datetime.strptime(bu_gun, date_format)
        fark = b - a
        araba_varmi = Arabalar.Data().araba_sorgu("38CAN002")
        araba_aktif = Aktif_araba.Aktif_araba().araba_sorgu("38CAN002")
        if araba_aktif:
            self.Geri_bildirim.setText("Araba kullanımda.")
        else:
            if araba_varmi.kullanim_gun >= fark.days:
                self.Geri_bildirim.setText("Yeterli bir ehliyete sahip değilsiniz.")
            else:
                araba="Renault"
                araba2="38CAN002"
                araba_bil.append(araba)
                araba_bil.append(araba2)
                git = araba_onaylama()
                widget.addWidget(git)
                widget.setCurrentIndex(widget.currentIndex() + 1)



    def araba3(self):
        kullanici_adi = bilgi[0]
        user = Kullanici.Data().kullanici_cekme(kullanici_adi)
        bu_gun = datetime.datetime.strftime(an, '%d %m %Y')

        date_format = "%d %m %Y"
        a = datetime.datetime.strptime(user.ehliyet_tarih, date_format)
        b = datetime.datetime.strptime(bu_gun, date_format)
        fark = b - a
        araba_varmi = Arabalar.Data().araba_sorgu("38CAN003")
        araba_aktif = Aktif_araba.Aktif_araba().araba_sorgu("38CAN003")
        if araba_aktif:
            self.Geri_bildirim.setText("Araba kullanımda.")
        else:

            if araba_varmi.kullanim_gun >= fark.days:
                self.Geri_bildirim.setText("Yeterli bir ehliyete sahip değilsiniz.")
            else:
                araba ='Hyundai'
                araba2='38CAN003'
                araba_bil.append(araba)
                araba_bil.append(araba2)
                git = araba_onaylama()
                widget.addWidget(git)
                widget.setCurrentIndex(widget.currentIndex() + 1)






    def cikis(self):
        app.exit(app.exec())

kisigun=[]
kisiindirim=[]
araba_fiyat=[]
class araba_onaylama(QWidget):
    def __init__(self):

        super(araba_onaylama, self).__init__()
        loadUi("araba-onay.ui", self)
        self.instagram.clicked.connect(lambda: webbrowser.open('https://twitter.com/muratcaneravsar'))
        self.Cikis_buton.clicked.connect(self.cikis)
        self.Giris_buton.clicked.connect(self.hesap)
        self.Giris_buton.clicked.connect(self.gunebak)

        arac = araba_bil
        self.kisi_bilgi.setText("Sevgili {}".format(bilgi[0].upper()))
        self.araba_bilgilendirme.setText("Kiralamak istediğiniz aracın\nModeli:{} Plakası:{}".format(arac[0],arac[1]))


    def hesap(self):
        gun = self.kiralamagn.text()
        kisigun.append(gun)
        indirim = self.indirim_kodu.text()
        if len(indirim) == 0:
            pass
        else:
            kisiindirim.append(indirim)

    def gunebak(self):
        kod = Rastgele_kod.Rastgele().random_char()
        user = Kullanici.Data().kullanici_cekme(bilgi[0])
        gun = kisigun[-1]
        Gun = int(gun)
        girilenkod = kisiindirim[-1]
        arac = araba_bil
        araba = Arabalar.Data().araba_sorgu(arac[1])

        if girilenkod == "Devam":
            araba_ucret = Gun * araba.ucret
            araba_fiyat.append(araba_ucret)
            bugun = datetime.datetime.today()
            ileri = datetime.timedelta(days=Gun)
            teslim_ileri = bugun + ileri
            teslim_tarih = teslim_ileri.strftime('%d %m %Y')
            Rastgele_kod.KOD().indirim_kodu_kayit(kod)
            Aktif_araba.Aktif_araba().araba_ekle(araba.model, araba.plaka, araba.kilometre, bugun.strftime('%c'),
                                                 teslim_tarih, user.kullanici_adi, kod)
            Admin.Admin().user_sales(araba.model, araba.plaka, araba.kilometre, 0, bugun.strftime('%c'),
                                     teslim_tarih, 0, user.kullanici_adi, kod)
            time.sleep(2)
            git = bilgilendirme4()
            widget.addWidget(git)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            girilenkod1=girilenkod
            kod_sorgu = Rastgele_kod.KOD().indirim_kod_sorgu(girilenkod1)
            if kod_sorgu == 2:
                self.geri_bildirim.setText("Bu kod zaten kullanılmış.")
            else:
                if kod_sorgu == 3 :
                    self.geri_bildirim.setText("Lütfen geçerli bir kod giriniz.")
                else:
                    if kod_sorgu == 1:
                        araba_ucret = Gun * araba.ucret
                        Rastgele_kod.KOD().kod_giris(girilenkod1)
                        araba_toplam = araba_ucret - araba_ucret * (20 / 100)
                        araba_fiyat.append(araba_toplam)
                        bugun = datetime.datetime.today()
                        ileri = datetime.timedelta(days=Gun)
                        teslim_ileri = bugun + ileri
                        teslim_tarih = teslim_ileri.strftime('%d %m %Y')
                        Rastgele_kod.KOD().indirim_kodu_kayit(kod)
                        Aktif_araba.Aktif_araba().araba_ekle(araba.model, araba.plaka, araba.kilometre, bugun.strftime('%c'),
                                                             teslim_tarih, user.kullanici_adi, kod)
                        Admin.Admin().user_sales(araba.model, araba.plaka, araba.kilometre, 0, bugun.strftime('%c'),
                                                 teslim_tarih, 0, user.kullanici_adi, kod)
                        time.sleep(2)
                        git = bilgilendirme4()
                        widget.addWidget(git)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
    def cikis(self):
        app.exit(app.exec())




app = QApplication(sys.argv)
welcome = Giris_ekrani()
widget = QtWidgets.QStackedWidget()
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")