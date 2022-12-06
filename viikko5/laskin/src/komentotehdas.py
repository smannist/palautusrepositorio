
class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.plus(int(self.lue_syote()))

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovelluslogiikka.miinus(int(self.lue_syote()))

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka  = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()