
# Sistem Pembatas Beban Jembatan dengan Gate Otomatis

def baca_data():
    # ABSTRAKSI: batas jembatan dan berat tiap kendaraan
    w_maks = float(input("Beban maksimum jembatan W_maks (kg): "))
    n = int(input("Jumlah kendaraan n: "))

    berat = []  # ARRAY: berat semua kendaraan
    for i in range(n):  # PENGULANGAN : input berat tiap kendaraan
        w = float(input(f"Beban kendaraan {i + 1} (kg): "))
        berat.append(w)

    return w_maks, berat



def cek_kendaraan(w, total, w_maks):
    # tiga kemungkinan
    if w > w_maks:
        return "TOLAK"   # terlalu berat kapan pun
    elif total + w <= w_maks:
        return "LOLOS"   # masih muat di gelombang ini
    else:
        return "TAHAN"   # tidak muat, tunggu gelombang berikutnya



def proses_gelombang(antrian, berat, w_maks):
    total = 0
    lolos = 0
    ditolak = 0
    tertahan = []  # ARRAY: kendaraan yang ditahan

    # setiap kendaraan diproses dengan langkah yang sama:
    # ambil berat -> cek -> atur gate -> catat
    for i in antrian:
        w = berat[i]
        hasil = cek_kendaraan(w, total, w_maks)

        if hasil == "LOLOS":
            total += w
            lolos += 1
            gate = "BUKA"
        elif hasil == "TOLAK":
            ditolak += 1
            gate = "TUTUP"
        else:
            tertahan.append(i)
            gate = "TUTUP"

        print(f"  Kendaraan {i + 1} ({w} kg): {hasil}, gate {gate}, total {total} kg")

    return tertahan, lolos, ditolak



def tampilkan_hasil(lolos, ditolak, gelombang):
    print("\n=== HASIL ===")
    print("Kendaraan lolos   :", lolos)
    print("Kendaraan ditolak :", ditolak)
    print("Jumlah gelombang  :", gelombang)



def main():
    w_maks, berat = baca_data()

    antrian = list(range(len(berat)))  # ARRAY: nomor urut kendaraan dalam antrian
    total_lolos = 0
    total_ditolak = 0
    gelombang = 0

    #  PENGULANGAN : ulangi gelombang sampai antrian kosong
    while len(antrian) > 0:
        gelombang += 1
        print(f"\n=== Gelombang {gelombang} ===")
        antrian, lolos, ditolak = proses_gelombang(antrian, berat, w_maks)
        total_lolos += lolos
        total_ditolak += ditolak

    tampilkan_hasil(total_lolos, total_ditolak, gelombang)


main()