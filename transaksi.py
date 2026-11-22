from datetime import datetime


class Transaksi:
    """Class Association: satu Transaksi memiliki tepat satu Rekening."""

    def __init__(self, id_transaksi, rekening, jenis, jumlah):
        self.__id_transaksi = id_transaksi
        self.__rekening = rekening          # relasi ke objek Rekening
        self.__jenis = jenis                # "SETOR" atau "TARIK"
        self.__jumlah = jumlah
        self.__tanggal = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__status = "BELUM DIPROSES"

    # ---------- Getter ----------
    def get_id(self):
        return self.__id_transaksi

    def get_rekening(self):
        return self.__rekening

    def get_jenis(self):
        return self.__jenis

    def get_jumlah(self):
        return self.__jumlah

    def get_tanggal(self):
        return self.__tanggal

    # ---------- Method tambahan ----------
    def proses(self):
        """Menjalankan transaksi pada rekening terkait."""
        if self.__jenis == "SETOR":
            berhasil = self.__rekening.setor(self.__jumlah)
        else:
            berhasil = self.__rekening.tarik(self.__jumlah)
        self.__status = "BERHASIL" if berhasil else "GAGAL"
        return berhasil

    def cek_status(self):
        return self.__status

    def info(self):
        return (f"{self.__id_transaksi} | {self.__tanggal} | {self.__jenis} "
                f"Rp{self.__jumlah:,} | Rekening: {self.__rekening.get_no_rekening()} "
                f"({self.__rekening.get_nama_pemilik()}) | Status: {self.__status}")
