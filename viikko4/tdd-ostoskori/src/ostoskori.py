from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        summa = 0

        if len(self.ostoskori) == 0:
            return 0

        for ostos in self.ostoskori:
            summa += ostos.lukumaara()
        
        return summa

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0

        if (len(self.ostoskori)) == 0:
            return 0

        for ostos in self.ostoskori:
            summa += ostos.hinta()

        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote, lisaa = 0):
        ostos = Ostos(lisattava)
        ostos.muuta_lukumaaraa(lisaa)
        self.ostoskori.append(ostos)

    def poista_tuote(self, poistettava: Tuote, vahenna = 0):
        poistettava_nimi = poistettava.nimi()

        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == poistettava_nimi:
                ostos.muuta_lukumaaraa(vahenna)

            if ostos.lukumaara() == 0:
                self.ostoskori.remove(ostos)

    def tyhjenna(self):
        self.ostoskori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
