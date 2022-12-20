from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def main():

    komento = {
        "a": KPSPelaajaVsPelaaja(),
        "b": KPSTekoaly(),
        "c": KPSParempiTekoaly()
    }

    while True:

        tulosta_menu()

        vastaus = input()

        if vastaus not in komento:
            break
        else:
            komento[vastaus].pelaa()

def tulosta_menu():
    print("Valitse pelataanko"
          "\n (a) Ihmistä vastaan"
          "\n (b) Tekoälyä vastaan"
          "\n (c) Parannettua tekoälyä vastaan"
          "\nMuilla valinnoilla lopetetaan"
        )



if __name__ == "__main__":
    main()
