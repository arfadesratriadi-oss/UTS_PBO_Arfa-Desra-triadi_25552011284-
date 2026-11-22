# ==========================================================
# File   : rekening.py
# Isi    : Superclass Rekening
# ==========================================================

class Rekening:
    """Superclass: merepresentasikan rekening bank secara umum."""

    # Constructor berparameter
    def __init__(self, no_rekening, nama_pemilik, saldo):
        # Atribut private (Encapsulation)
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    # ---------- Getter ----------
    def get_no_rekening(self):
        return self.__no_rekening

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    # ---------- Setter (dengan validasi) ----------
    def set_nama_pemilik(self, nama):
        if nama.strip():
            self.__nama_pemilik = nama

    # ---------- Method tambahan ----------
    def get_saldo_minimum(self):
        """Batas terendah saldo setelah penarikan. Dioverride subclass."""
        return 0

    def get_jenis(self):
        """Dioverride subclass (Polymorphism)."""
        return "Rekening"

    def setor(self, jumlah):
        """Menambah saldo. Return True jika berhasil."""
        if jumlah > 0:
            self.__saldo += jumlah
            return True
        return False

    def tarik(self, jumlah):
        """Mengurangi saldo selama tidak melewati batas minimum."""
        if jumlah > 0 and self.__saldo - jumlah >= self.get_saldo_minimum():
            self.__saldo -= jumlah
            return True
        return False

    def cek_status(self):
        """Status rekening berdasarkan saldo."""
        if self.__saldo < 0:
            return "OVERDRAFT"
        elif self.__saldo < 50000:
            return "SALDO RENDAH"
        return "AKTIF"

    def info(self):
        return (f"[{self.__no_rekening}] {self.__nama_pemilik} | Jenis: {self.get_jenis()} | "
                f"Saldo: Rp{self.__saldo:,} | Status: {self.cek_status()}")