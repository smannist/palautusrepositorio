from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmainen_siirto):
        return input("Toisen pelaajan siirto: ")
