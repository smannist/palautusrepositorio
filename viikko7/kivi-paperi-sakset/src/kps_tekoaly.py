from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmainen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
