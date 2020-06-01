import csv

def discount(jumlah_tagihan):
    if jumlah_tagihan >= 250000:
        return jumlah_tagihan - 25000,25000
    elif jumlah_tagihan >= 100000:
        return jumlah_tagihan - 10000,10000
    else:
        return jumlah_tagihan, 0
