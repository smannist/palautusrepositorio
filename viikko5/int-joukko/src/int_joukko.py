KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu_lukujonoon(self, alkio):
        if alkio in self.lukujono:
            return True

        return False

    def lisaa_alkio(self, alkio):
        alkio_kuuluu_lukujonoon = self.kuuluu_lukujonoon(alkio)

        if not alkio_kuuluu_lukujonoon:
            self.lukujono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            self.kasvata_kokoa()
            return True

        return False

    def kasvata_kokoa(self):
        if self.alkioiden_lkm % len(self.lukujono) == 0:
            vanha_lukujono = self.lukujono
            self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.uusi_lukujono(vanha_lukujono, self.lukujono)

    def poista(self, alkio):
        if alkio in self.lukujono:
            poistettava_alkio = self.lukujono.index(alkio)
            self.lukujono[poistettava_alkio] = 0

            self.siirra_alkioita(poistettava_alkio)

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def siirra_alkioita(self, poistettava_alkio):
        for j in range(poistettava_alkio, self.alkioiden_lkm - 1):
                siirrettava = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = siirrettava

    def uusi_lukujono(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def koko(self):
        return self.alkioiden_lkm

    def luo_lukujono(self):
        lukujono = [0] * self.alkioiden_lkm

        for i in range(0, len(lukujono)):
            lukujono[i] = self.lukujono[i]

        return lukujono

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.luo_lukujono()
        b_taulu = b.luo_lukujono()

        for i in range(0, len(a_taulu)):
            yhdiste_joukko.lisaa_alkio(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_joukko.lisaa_alkio(b_taulu[i])

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_taulu = a.luo_lukujono()
        b_taulu = b.luo_lukujono()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_joukko.lisaa_alkio(b_taulu[j])

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.luo_lukujono()
        b_taulu = b.luo_lukujono()

        for i in range(0, len(a_taulu)):
            erotus_joukko.lisaa_alkio(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_joukko.poista(b_taulu[i])

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i]) + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
