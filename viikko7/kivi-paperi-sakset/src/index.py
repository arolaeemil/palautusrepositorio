from kivipaperisakset import *


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            KiviPaperiSakset.luo_kaksinpeli()

        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            KiviPaperiSakset.luo_tekoalypeli()

        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            KiviPaperiSakset.luo_vaikeatekoalypeli()

        else:
            break


if __name__ == "__main__":
    main()
