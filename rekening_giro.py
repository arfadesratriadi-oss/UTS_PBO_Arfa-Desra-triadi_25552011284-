# ==========================================================
# File   : rekening_giro.py
# Isi    : Subclass RekeningGiro (extends Rekening)
# ==========================================================
from rekening import Rekening


class RekeningGiro(Rekening):
    """Subclass: giro dengan limit overdraft dan biaya administrasi."""

    def __init__(self, no_rekening, nama_pemilik, saldo, limit_overdraft, biaya_admin):
        super().__init__(no_rekening, nama_pemilik, saldo)
        # Atribut private khusus giro
        self.__limit_overdraft = limit_overdraft
        self.__biaya_admin = biaya_admin

    def get_limit_overdraft(self):
        return self.__limit_overdraft

    def get_biaya_admin(self):
        return self.__biaya_admin

    def set_limit_overdraft(self, limit):
        if limit >= 0:
            self.__limit_overdraft = limit

    def potong_biaya_admin(self):
        """Method tambahan: memotong biaya admin bulanan dari saldo."""
        return self.tarik(self.__biaya_admin)

    def sisa_limit(self):
        """Method tambahan: sisa dana yang masih bisa ditarik (termasuk overdraft)."""
        return self.get_saldo() + self.__limit_overdraft

    # Override: giro boleh minus sampai batas limit overdraft
    def get_saldo_minimum(self):
        return -self.__limit_overdraft

    def get_jenis(self):
        return "Giro"

    def info(self):
        return (super().info() +
                f" | Limit Overdraft: Rp{self.__limit_overdraft:,} | Admin: Rp{self.__biaya_admin:,}")