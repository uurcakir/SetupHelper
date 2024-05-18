# coding:utf-8
import requests
import subprocess
import os


def capcut():
    print("...İNDİRİLİYOR (2.2 MB)...")
    url = 'https://lf16-capcut.faceulv.com/obj/capcutpc-packages-us/installer/capcut_capcutpc_0_1.2.6_installer.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'CapCut_7267140873131950085_installer.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def gimp():
    print("...İNDİRİLİYOR (329 MB)...")
    url = 'https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.38-setup.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'gimp-2.10.38-setup.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
