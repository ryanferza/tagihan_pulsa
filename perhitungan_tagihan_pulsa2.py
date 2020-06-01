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
    minggu = input("Untuk minggu ke: ")
    total_sms = int(input("Jumlah SMS : "))
    menit_tlp_sama = float(input("Jumlah menit telepon anda ke sesama operator: "))
    menit_tlp_lain = float(input("Jumlah menit telepon anda ke lain operator: "))
    total_kuota_sosmed = float(input("Jumlah kuota terpakai untuk sosial media (kb): "))
    total_kuota_lainnya = float(input("Jumlah kuota terpakai untuk lainnya (kb): "))
    totalkuota1 = total_kuota_sosmed + total_kuota_lainnya
    totalkuota2 = 5*totalkuota1
    totalpulsatlp = 250*menit_tlp_sama + 500*menit_tlp_lain
    pulsasms = 150*total_sms
    totalpulsa = pulsasms + totalpulsatlp
    total_tagihan = totalkuota2 + totalpulsa
    
    data.append([minggu,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan])

print(data)

print("--------------------------------------------------------------------------------")
print('Minggu ke-\t Jumlah SMS\t Menit telepon ke sesama operator(menit)\t Menit telepon ke operaator lain(menit)\t Total pulsa (Rp)\t Kuota sosmed (kb)\t Kuota lainnya (kb)\t Tagihan kuota terpakai (Rp)\t Tagihan/minggu')

for i in range(0,len(data)):
    print(data[i][0],'\t', data[i][1], '\t',data[i][2], '\t',data[i][3], '\t',data[i][4], '\t',data[i][5], '\t',data[i][6], '\t',data[i][7], '\t',data[i][8])
    i += 1

print("--------------------------------------------------------------------------------")
