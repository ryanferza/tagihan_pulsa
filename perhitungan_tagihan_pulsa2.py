import csv

#bagian penentuan potongan harga
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

while input_data: #iterasi data
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
    totalkuota2 = 0.005*totalkuota1
    totalpulsatlp = 70*menit_tlp_sama + 100*menit_tlp_lain
    pulsasms = 50*total_sms
    totalpulsa = pulsasms + totalpulsatlp
    total_tagihan = totalkuota2 + totalpulsa
    
    #penambahan data ke dalam list
    data.append([minggu,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan])

print("--------------------------------------------------------------------------------")
#tabel pada program
print('Minggu ke-\t Total tagihan pulsa (Rp)\t Total tagihan kuota (Rp)\t Tagihan/minggu (Rp)')

for i in range(0,len(data)):
    print(data[i][0],'\t',data[i][4], '\t\t',data[i][7], '\t\t',data[i][8])
    i += 1

print("--------------------------------------------------------------------------------")

list_tagihan = [data[i][8] for i in range(len(data))]
jumlah_tagihan = 0
for row in data:
    jumlah_tagihan += row[8]

jml_minggu = len(data)
tagihan_akhir,potongan = discount(jumlah_tagihan)
#akhir
print("Jumlah tagihan", nama, "dengan No. telepon", no_telp, "selama", jml_minggu ,"minggu adalah sebesar Rp.", jumlah_tagihan)
print("Anda mendapatkan potongan sebesar", potongan, "maka jumlah akhir tagihan anda adalah", tagihan_akhir)
input("Keluar program (ketik apapun) ")

#export ke csv
with open(nama_file, 'w') as outf:
    header = ['Minggu ke-','Jumlah SMS','Menit telepon ke sesama operator','Menit telepon ke operator lain','Total pulsa (Rp)','Kuota sosmed (kb)','Kuota lainnya (kb)','Tagihan kuota terpakai (Rp)','Tagihan/minggu (Rp)']
    writer = csv.DictWriter(outf, fieldnames=header)
    writer.writeheader()
    
    for row in data:
        minggu,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan = row
        writer.writerow({'Minggu ke-': minggu,
                         'Jumlah SMS': total_sms,
                         'Menit telepon ke sesama operator': menit_tlp_sama,
                         'Menit telepon ke operator lain': menit_tlp_lain,
                         'Total pulsa (Rp)': totalpulsa,
                         'Kuota sosmed (kb)': total_kuota_sosmed,
                         'Kuota lainnya (kb)': total_kuota_lainnya,
                         'Tagihan kuota terpakai (Rp)': totalkuota2,
                         'Tagihan/minggu (Rp)': total_tagihan
                        })
