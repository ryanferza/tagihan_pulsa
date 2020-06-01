import csv

def discount(jumlah_tagihan):
    if jumlah_tagihan >= 250000:
        return jumlah_tagihan - 25000,25000
    elif jumlah_tagihan >= 100000:
        return jumlah_tagihan - 10000,10000
    else:
        return jumlah_tagihan, 0

    #mulai program
input_data = True
nama_file = "tagihan2.csv"
data = []
nama = input("Nama : ")
no_telp = input("No. Telepon: ")

while input_data:
    answer = input("Apakah anda ingin menginput data pulsa dan kuota anda (data per minggu)? (y/n) ")
    if answer != "y":

        break
