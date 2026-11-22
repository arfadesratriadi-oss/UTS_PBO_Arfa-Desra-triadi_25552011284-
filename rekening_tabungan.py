from rekening import Rekening


class RekeningTabungan(Rekening):
    """Subclass: tabungan dengan bunga dan saldo minimum yang harus mengendap."""

    def __init__(self, no_rekening, nama_pemilik, saldo, suku_bunga, saldo_endap):
        super().__init__(no_rekening, nama_pemilik, saldo)  # constructor superclass
        # Atribut private khusus tabungan
        self.__suku_bunga = suku_bunga      # persen per tahun
        self.__saldo_endap = saldo_endap    # saldo minimum yang tidak boleh ditarik

    def get_suku_bunga(self):
        return self.__suku_bunga

    def get_saldo_endap(self):
        return self.__saldo_endap

    def set_suku_bunga(self, bunga):
        if bunga >= 0:
            self.__suku_bunga = bunga

    def hitung_bunga_tahunan(self):
        """Method tambahan: estimasi bunga satu tahun dari saldo saat ini."""
        return int(self.get_saldo() * self.__suku_bunga / 100)

    def tambah_bunga(self):
        """Method tambahan: memasukkan bunga tahunan ke saldo."""
        return self.setor(self.hitung_bunga_tahunan())

    # Override: tabungan tidak boleh kurang dari saldo endap
    def get_saldo_minimum(self):
        return self.__saldo_endap

    def get_jenis(self):
        return "Tabungan"

    def info(self):
        return (super().info() +
                f" | Bunga: {self.__suku_bunga}% | Saldo Endap: Rp{self.__saldo_endap:,}")
