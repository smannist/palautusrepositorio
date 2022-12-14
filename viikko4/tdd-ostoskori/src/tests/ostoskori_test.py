import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote = Tuote("Karkkipussi", 5)
        self.ostos = Ostos(self.tuote)

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

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.ostos, 1)
        self.assertAlmostEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_kaksi_kertaa_tuotteen_hinta(self):
        tuote = Tuote("Bugatti Chiron", 3500000)
        self.kori.lisaa_tuote(tuote, 1)
        self.assertAlmostEqual(self.kori.hinta(), 7000000)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertAlmostEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_tuote_on_oikea_ja_sita_on_oikea_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertAlmostEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertAlmostEqual(ostos.lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(self.ostos)
        ostokset = self.kori.ostokset()
        self.assertAlmostEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.tuote, 1)
        ostos = self.kori.ostokset()[0]
        self.assertAlmostEqual(ostos.lukumaara(), 2)
        ostokset = self.kori.ostokset()
        self.assertAlmostEqual(len(ostokset),1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_kaksi(self):
        self.kori.lisaa_tuote(self.tuote, 1)
        ostos = self.kori.ostokset()[0]
        self.assertAlmostEqual(ostos.tuotteen_nimi(), "Karkkipussi")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_yhden_tuotteen_poistaminen_kahdesta_palauttaa_oikean_tuote_maaran(self):
        self.kori.lisaa_tuote(self.tuote,1)
        self.kori.poista_tuote(self.tuote,-1)
        ostos = self.kori.ostokset()[0]
        self.assertAlmostEqual(ostos.lukumaara(), 1)
    
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_taman_jalkeen_tyhja(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.poista_tuote(self.tuote,-1)
        ostokset = self.kori.ostokset()
        self.assertAlmostEqual(len(ostokset), 0)

    def test_ostoskori_tyhjentyy_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(self.tuote)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertAlmostEqual(len(ostokset), 0)