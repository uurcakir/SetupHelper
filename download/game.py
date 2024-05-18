# coding:utf-8
import requests
import subprocess
import os


def steam():
    print("...İNDİRİLİYOR (2.3 MB)...")
    url = 'https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'SteamSetup.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def epic():
    print("...İNDİRİLİYOR (176 MB)...")
    url = 'https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'EpicInstaller-15.17.1.msi')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
