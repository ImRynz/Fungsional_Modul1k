# Sistem penilaian mahasiswa

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return 0.4 * uts + 0.6 * uas

# Fungsi untuk menghitung semua nilai akhir
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai["UTS"], nilai["UAS"])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        "Rifki": {"UTS": 75, "UAS": 85},
        "Pebri": {"UTS": 50, "UAS": 80},
        "Ajrul": {"UTS": 90, "UAS": 65}
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa) # Menghitung nilai akhir semua mahasiswa

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
