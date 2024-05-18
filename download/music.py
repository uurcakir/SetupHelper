# coding:utf-8
import requests
import subprocess
import os


def spotify():
    print("...İNDİRİLİYOR (996 KB)...")
    url = 'https://download.scdn.co/SpotifySetup.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'SpotifySetup.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def vlc():
    print("...İNDİRİLİYOR (42.4 MB)...")
    url = 'https://mirrors.netix.net/vlc/vlc/3.0.20/win64/vlc-3.0.20-win64.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'vlc-3.0.20-win64.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def audacity():
    print("...İNDİRİLİYOR (15.3 MB)...")
    url = 'https://github.com/audacity/audacity/releases/download/Audacity-3.5.1/audacity-win-3.5.1-64bit.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'audacity-win-3.5.1-64bit.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
