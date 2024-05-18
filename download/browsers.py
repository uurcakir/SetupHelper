# coding:utf-8
import requests
import subprocess
import os


def brave():
    print("...İNDİRİLİYOR (1.5 KB)...")
    url = 'https://laptop-updates.brave.com/latest/winx64'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'brave_setup.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)

    # İndirilen dosyayı çalıştır
    # if os.path.exists(indirme_yolu):
    #     subprocess.call(indirme_yolu)
    #     print('Brave kurulumu başlatıldı.')
    # else:
    #     print('Brave kurulum dosyası bulunamadı.')


def google_chrome():
    print("...İNDİRİLİYOR (116 MB)...")
    url = 'https://dl.google.com/chrome/install/GoogleChromeStandaloneEnterprise64.msi'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'ChromeSetup.msi')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def mozilla_firefox():
    print("...İNDİRİLİYOR (342 KB)...")
    url = 'https://download.mozilla.org/?product=firefox-stub&os=win&lang=tr&attribution_code=c291cmNlPWR1Y2tkdWNrZ28uY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmY2xpZW50X2lkPShub3Qgc2V0KSZjbGllbnRfaWRfZ2E0PShub3Qgc2V0KSZzZXNzaW9uX2lkPShub3Qgc2V0KSZkbHNvdXJjZT1tb3pvcmc.&attribution_sig=afaa4f5081848d5678b67c0316306aaa663696f606963fb889fb8fe2dcc378fb'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'Firefox Installer.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def opera():
    print("...İNDİRİLİYOR (5.2 MB)...")
    url = 'https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=duckduckgo&utm_medium=ose&utm_campaign=(none)&http_referrer=https%3A%2F%2Fduckduckgo.com%2F&utm_site=opera_com&&utm_lastpage=opera.com/'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'OperaSetup.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)


def tor():
    print("...İNDİRİLİYOR (100 MB)...")
    url = 'https://www.torproject.org/dist/torbrowser/13.0.15/tor-browser-windows-x86_64-portable-13.0.15.exe'  # indirme linki
    indirme_yolu = os.path.join(os.path.expanduser('~'), 'Desktop',
                                'tor-browser-windows-x86_64-portable-13.0.15.exe')  # Masaüstüne kaydedilecek dosyanın yolu

    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        with open(indirme_yolu, 'wb') as f:
            f.write(response.content)
        print('Kurulum dosyası başarıyla indirildi ve masaüstüne kaydedildi.')
    else:
        print('Kurulum dosyası indirilemedi. Hata kodu:', response.status_code)
