# coding:utf-8

import speedtest
from colorama import Fore

st = speedtest.Speedtest()


def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def test():
    print(Fore.WHITE, 'İnternet hızınız ölçülüyor...')
    ds = st.download()
    print(Fore.RED, 'İndirme hızınız : ', humansize(ds))
    print(Fore.WHITE, 'Yükleme hızınız ölçülüyor...')
    us = st.upload()
    print(Fore.RED, 'Yükleme hızınız : ', humansize(us))
