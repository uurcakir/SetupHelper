# coding:utf-8
import requests
import subprocess
import os


def soda():
    print("...İNDİRİLİYOR (11.4 MB)...")
    url = 'https://download14-desktop.sodapdf.com/download.ashx?productcode=sodapdf$configId=C0FA62E2-7699-4276-8772-B3972CECFF73$params=lang=en&qti=c08025d1-1981-5977-ec9c-fae91f0c6f83_2024-05-18&mkey6=c08025d1-1981-5977-ec9c-fae91f0c6f83_2024-05-18&uid=1015462&cmp=none&wid=8043&mkey1=sodapdf.com/pdf-creator/&partner=servicepages_2021&$thx=https://paygw.sodapdf.com/redirect/install/soda-pdf-desktop-14/$custlog=http://selfserve.upclick.com/index.aspx$support=https://paygw.sodapdf.com/redirect/support/soda-pdf-desktop-14/$uninstall=https://paygw.sodapdf.com/redirect/uninstall/soda-pdf-desktop-14/&_gl=1*75tl17*_gcl_au*Nzk0NzM1NzQ4LjE3MTYwNjI3Mjc.'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'SodaPDFDesktop14.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def foxit():
    print("...İNDİRİLİYOR (114 MB)...")
    url = 'https://www.foxit.com/downloads/latest.html?product=Foxit-Reader&platform=Windows&version=&package_type=&language=English&distID='  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'FoxitPDFReader202421_enu_Setup_Prom.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
