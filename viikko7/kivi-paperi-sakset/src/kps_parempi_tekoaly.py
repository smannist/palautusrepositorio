from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    tekoaly_paranneltu = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmainen_siirto):
        tokan_siirto = self.tekoaly_paranneltu.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
