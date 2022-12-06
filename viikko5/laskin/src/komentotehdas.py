
class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.edellinen_arvo = sovelluslogiikka.tulos

    def suorita(self):
        self.edellinen_arvo = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.plus(int(self.lue_syote()))
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.edellinen_arvo = sovelluslogiikka.tulos

    def suorita(self):
        self.edellinen_arvo = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.miinus(int(self.lue_syote()))
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka  = sovelluslogiikka
        self.edellinen_arvo = sovelluslogiikka.tulos

    def suorita(self):
        self.edellinen_arvo = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa()

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)
