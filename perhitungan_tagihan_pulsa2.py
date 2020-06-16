import csv
from datetime import datetime


print("===========================================================================")
print("             SELAMAT DATANG DI PROGRAM TAGIHAN PULSA             ")
print("Program ini bertujuan untuk menghitung tagihan pulsa perminggu dengan menginput minggu yang berurutan dimulai dari minggu pertama (1)!")
print("===========================================================================")

#menu ke (1) untuk menginput data jika pelanggan belum pernah menginput
def inputdata():
    
    print("-inputlah data-data anda-")
    #bagian penentuan potongan harga
    def discount(jumlah_tagihan):
        if jumlah_tagihan >= 250000:
            return jumlah_tagihan - 25000,25000
        elif jumlah_tagihan >= 100000:
            return jumlah_tagihan - 10000,10000
        else:
            return jumlah_tagihan, 0

    #mulai penginputan data untuk menjadi list
    data = []
    nama = input("Nama : ")
    no_telp = input("No. Telepon: ")
    nama_file = datetime.now().strftime(f'{nama}_{no_telp}_%m.csv')
    count = 0
    input_data = True

    #iterasi penginputan data tiap minggu
    while input_data: 
        answer = input("Apakah anda ingin menginput data pulsa dan kuota anda (data per minggu)? (y/n) ")
        if answer != "y":
            break #keluar dari iterasi/while
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
        count += 1 #count akan bertambah satu setiap penginputan
        #penambahan data ke dalam list
        data.append([count,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan])

    print("--------------------------------------------------------------------------------")
    #cetak tabel tagihan tiap minggu pada program
    print('Minggu ke-\t Total tagihan pulsa (Rp)\t Total tagihan kuota (Rp)\t Tagihan/minggu (Rp)')

    for i in range(0,len(data)):
        print(data[i][0],'\t''\t', data[i][4], '\t''\t''\t', data[i][7],'\t''\t''\t', data[i][8])
        i += 1

    print("--------------------------------------------------------------------------------")
    #perhitungan total tagihan dari seluruh minggu
    jumlah_tagihan = 0
    for row in data:
        jumlah_tagihan += row[8]

    jml_minggu = len(data)
    tagihan_akhir,potongan = discount(jumlah_tagihan)
    print("Jumlah tagihan", nama, "dengan No. telepon", no_telp, "selama", jml_minggu ,"minggu adalah sebesar Rp.", jumlah_tagihan)
    print("Anda mendapatkan potongan sebesar", potongan, "maka jumlah akhir tagihan anda adalah", tagihan_akhir)
    input("Keluar program (ketik apapun) ")

    #export list ke bentuk csv
    with open(nama_file, 'w') as outf:
        header = ['Minggu ke-','Jumlah SMS','Menit telepon ke sesama operator','Menit telepon ke operator lain','Total pulsa (Rp)','Kuota sosmed (kb)','Kuota lainnya (kb)','Tagihan kuota terpakai (Rp)','Tagihan/minggu (Rp)']
        writer = csv.DictWriter(outf, fieldnames=header)
        writer.writeheader()
    
        for row in data:
            count,total_sms,menit_tlp_sama,menit_tlp_lain,totalpulsa,total_kuota_sosmed,total_kuota_lainnya,totalkuota2,total_tagihan = row
            writer.writerow({'Minggu ke-': count,
                            'Jumlah SMS': total_sms,
                            'Menit telepon ke sesama operator': menit_tlp_sama,
                            'Menit telepon ke operator lain': menit_tlp_lain,
                            'Total pulsa (Rp)': totalpulsa,
                            'Kuota sosmed (kb)': total_kuota_sosmed,
                            'Kuota lainnya (kb)': total_kuota_lainnya,
                            'Tagihan kuota terpakai (Rp)': totalkuota2,
                            'Tagihan/minggu (Rp)': total_tagihan
                            })
            
#menu ke (2) untuk mengecek data yang sudah pernah diinput
def cekdata():

    
#menu utama
def menu():
    
    
#menu keluar
def keluar():

