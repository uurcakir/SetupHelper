# coding:utf-8
from download import chat, pdf, game, browsers, zip, music, edit, speedTest, coding
import sys
from colorama import Fore

print(Fore.RED, '--------------- UĞUR ÇAKIR | ugrakir@outlook.com.tr ---------------')
print(Fore.BLUE,
      "*** Setup Helper'a hoşgeldiniz. İndirmek istediğiniz programı aşağıdaki kategorilerden seçebilirsiniz. ***")


def tarayicilar():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW)
        print("1 - Brave\n2 - Opera\n3 - Mozilla Firefox\n4 - Google Chrome\n5 - Tor\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            browsers.brave()
        elif secim.strip().lower() == '2':
            browsers.opera()
        elif secim.strip().lower() == '3':
            browsers.mozilla_firefox()
        elif secim.strip().lower() == '4':
            browsers.google_chrome()
        elif secim.strip().lower() == '5':
            browsers.tor()
        else:
            return secim.strip().lower()


def zip_rar():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW)
        print("1 - WinRAR\n2 - 7Zip\n3 - WinZip\n4 - PeaZip\n5 - BandiZip\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            zip.winrar()
        elif secim.strip().lower() == '2':
            zip.seven_zip()
        elif secim.strip().lower() == '3':
            zip.winzip()
        elif secim.strip().lower() == '4':
            zip.peazip()
        elif secim.strip().lower() == '5':
            zip.bandizip()
        else:
            return secim.strip().lower()


def oyun():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW, "1 - Steam\n2 - Epic Games Launcher\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            game.steam()
        elif secim.strip().lower() == '2':
            game.epic()
        else:
            return secim.strip().lower()


def sohbet():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW, "1 - Whatsapp\n2 - Discord\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            chat.whatsapp()
        elif secim.strip().lower() == '2':
            chat.discord()
        else:
            return secim.strip().lower()


def pdfokuyucu():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW, "1 - Soda PDF\n2 - Foxit Reader\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            pdf.soda()
        elif secim.strip().lower() == '2':
            pdf.foxit()
        else:
            return secim.strip().lower()


def muzik():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW, "1 - Spotify\n2 - VLC Player\n3 - Audacity\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            music.spotify()
        elif secim.strip().lower() == '2':
            music.vlc(),
        elif secim.strip().lower() == '3':
            music.audacity()
        else:
            return secim.strip().lower()


def video():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW, "1 - Capcut\n2 - Gimp\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            edit.capcut()
        elif secim.strip().lower() == '2':
            edit.gimp()
        else:
            return secim.strip().lower()


def code():
    while True:
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !\n")
        print(Fore.MAGENTA, "! KATEGORİ SEÇİMİNE DÖNMEK İÇİN 'K' YAZIN !")
        print(Fore.YELLOW,
              "1 - VSCode\n2 - Eclipse\n3 - Netbeans\n4 - PyCharm Community Edition\n5 - IntelliJ Community Edition\n"
              "6 - MySQL\n7 - MySQL Workbench\n8 -JavaJDK 22\n9 - Python 3.12\n10 - Notepad ++\n")
        secim = input('SEÇİM : ')
        if secim.strip().lower() == '1':
            coding.vscode()
        elif secim.strip().lower() == '2':
            coding.eclipse()
        elif secim.strip().lower() == '3':
            coding.netbeans()
        elif secim.strip().lower() == '4':
            coding.pycharm_communityEd()
        elif secim.strip().lower() == '5':
            coding.intellij_communityEd()
        elif secim.strip().lower() == '6':
            coding.mysql()
        elif secim.strip().lower() == '7':
            coding.mysql_workbench()
        elif secim.strip().lower() == '8':
            coding.javajdk()
        elif secim.strip().lower() == '9':
            coding.python()
        elif secim.strip().lower() == '10':
            coding.notepad()
        else:
            return secim.strip().lower()


def run():
    while True:
        print(Fore.WHITE, '--Kategoriler--')
        print(Fore.CYAN, "! ÇIKIŞ YAPMAK İÇİN 'Ç' YAZIN !")
        print(Fore.RED, "!! İNTERNET HIZINIZI TEST ETMEK İÇİN 'T' YAZIN !!\n", Fore.GREEN,
              "\n1 - Tarayıcılar\n2 - .rar/.zip\n3 - "
              "PDF Okuyucular\n4 - Oyun Platformları\n5 - Sosyal\n6 - Müzik-Ses\n7 - Video-Fotoğraf Düzenleme\n8 - "
              "Coding\n", Fore.YELLOW)

        kategori = input('SEÇİM : ')

        if kategori.strip().lower() == 't':
            speedTest.test()
        elif kategori.strip().lower() == 'ç':
            sys.exit()
        elif kategori.strip().lower() == '1':
            if tarayicilar() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '2':
            if zip_rar() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '3':
            if pdfokuyucu() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '4':
            if oyun() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '5':
            if sohbet() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '6':
            if muzik() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '7':
            if video() == 'ç':
                sys.exit()
            else:
                run()
        elif kategori.strip().lower() == '8':
            if code() == 'ç':
                sys.exit()
            else:
                run()


run()
