from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro
from transaksi import Transaksi

# Penyimpanan data sementara (in-memory)
daftar_rekening = []
daftar_transaksi = []


def input_angka(pesan):
    """Meminta input bilangan bulat; ulangi sampai valid."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("  Input harus berupa angka!")


def cari_rekening(nomor):
    """Mencari objek rekening berdasarkan nomor."""
    for r in daftar_rekening:
        if r.get_no_rekening() == nomor:
            return r
    return None


def data_awal():
    """Data contoh agar program mudah dicoba."""
    daftar_rekening.append(RekeningTabungan("1001", "Andi", 500000, 3, 50000))
    daftar_rekening.append(RekeningGiro("2001", "Sari", 1000000, 500000, 15000))


# ---------------- 1. TAMBAH DATA ----------------
def tambah_data():
    print("\n--- Tambah Data ---")
    print("1. Buka Rekening Tabungan\n2. Buka Rekening Giro\n3. Buat Transaksi")
    pilih = input("Pilih: ")
    if pilih in ("1", "2"):
        nomor = input("No rekening  : ")
        if cari_rekening(nomor):
            print("Nomor rekening sudah dipakai!")
            return
        nama = input("Nama pemilik : ")
        saldo = input_angka("Saldo awal   : ")
        if pilih == "1":
            bunga = input_angka("Suku bunga (%): ")
            endap = input_angka("Saldo endap   : ")
            daftar_rekening.append(RekeningTabungan(nomor, nama, saldo, bunga, endap))
        else:
            limit = input_angka("Limit overdraft: ")
            admin = input_angka("Biaya admin    : ")
            daftar_rekening.append(RekeningGiro(nomor, nama, saldo, limit, admin))
        print("Rekening berhasil dibuka.")
    elif pilih == "3":
        rek = cari_rekening(input("No rekening: "))
        if rek is None:
            print("Rekening tidak ditemukan.")
            return
        jenis = input("Jenis (1=Setor, 2=Tarik): ")
        jumlah = input_angka("Jumlah: ")
        trx = Transaksi(f"TRX{len(daftar_transaksi) + 1:03d}", rek,
                        "SETOR" if jenis == "1" else "TARIK", jumlah)
        trx.proses()
        daftar_transaksi.append(trx)
        print(trx.info())
        print(f"Saldo sekarang: Rp{rek.get_saldo():,}")
    else:
        print("Pilihan tidak valid.")


# ---------------- 2. TAMPILKAN DATA ----------------
def tampilkan_data():
    print("\n--- Data Rekening ---")
    if not daftar_rekening:
        print("(kosong)")
    for r in daftar_rekening:
        print(r.info())
    print("\n--- Data Transaksi ---")
    if not daftar_transaksi:
        print("(kosong)")
    for t in daftar_transaksi:
        print(t.info())


# ---------------- 3. CARI DATA ----------------
def cari_data():
    print("\n--- Cari Rekening ---")
    kata = input("Masukkan no rekening atau nama pemilik: ").lower()
    hasil = [r for r in daftar_rekening
             if kata in r.get_no_rekening().lower() or kata in r.get_nama_pemilik().lower()]
    if hasil:
        for r in hasil:
            print(r.info())
    else:
        print("Data tidak ditemukan.")


# ---------------- 4. UBAH DATA ----------------
def ubah_data():
    print("\n--- Ubah Data Rekening ---")
    rek = cari_rekening(input("No rekening yang diubah: "))
    if rek is None:
        print("Data tidak ditemukan.")
        return
    print(rek.info())
    nama = input("Nama pemilik baru (kosong = tetap): ")
    if nama:
        rek.set_nama_pemilik(nama)
    # Atribut khusus subclass diubah lewat setter masing-masing
    if isinstance(rek, RekeningTabungan):
        bunga = input("Suku bunga baru % (kosong = tetap): ")
        if bunga.isdigit():
            rek.set_suku_bunga(int(bunga))
    elif isinstance(rek, RekeningGiro):
        limit = input("Limit overdraft baru (kosong = tetap): ")
        if limit.isdigit():
            rek.set_limit_overdraft(int(limit))
    print("Data berhasil diubah.\n" + rek.info())


# ---------------- 5. CEK STATUS DATA ----------------
def cek_status():
    print("\n--- Cek Status ---")
    print("Status rekening:")
    for r in daftar_rekening:
        print(f"  {r.get_no_rekening()} - {r.get_nama_pemilik()}: {r.cek_status()}")
    print("Status transaksi:")
    for t in daftar_transaksi:
        print(f"  {t.get_id()} - {t.get_jenis()} Rp{t.get_jumlah():,}: {t.cek_status()}")


def main():
    data_awal()
    while True:
        print("\n===== BANK MINI =====")
        print("1. Tambah Data\n2. Tampilkan Data\n3. Cari Data")
        print("4. Ubah Data\n5. Cek Status Data\n6. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            cari_data()
        elif pilih == "4":
            ubah_data()
        elif pilih == "5":
            cek_status()
        elif pilih == "6":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
