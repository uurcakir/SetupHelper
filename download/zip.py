# coding:utf-8
import requests
import subprocess
import os


def winrar():
    print("...İNDİRİLİYOR 3.8 MB)...")
    url = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-700.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'winrar-x64-700.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def seven_zip():
    print("...İNDİRİLİYOR (1.5 KB)...")
    url = 'https://7-zip.org/a/7z2404-x64.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                '7z2404-x64.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def winzip():
    print("...İNDİRİLİYOR (2.8 MB)...")
    url = 'https://download.winzip.com/gl/nkln/winzip28-downwz.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'winzip28-downwz.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def peazip():
    print("...İNDİRİLİYOR (9.1 MB)...")
    url = 'https://github.com/peazip/PeaZip/releases/download/9.8.0/peazip-9.8.0.WIN64.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'peazip-9.8.0.WIN64.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def bandizip():
    print("...İNDİRİLİYOR (6.9 MB)...")
    url = 'https://www.bandisoft.com/bandizip/dl.php?web'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'BANDIZIP-SETUP-STD-X64.EXE')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
