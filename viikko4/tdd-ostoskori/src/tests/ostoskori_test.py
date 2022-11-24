import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote = Tuote("Karkkipussi", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertAlmostEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuote)
        self.assertAlmostEqual(self.kori.hinta(), 5)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertAlmostEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertAlmostEqual(self.kori.hinta(),8)