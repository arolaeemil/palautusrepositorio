from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            # ...
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    @staticmethod
    def luo_kaksinpeli():
        KPSPelaajaVsPelaaja().pelaa()

    @staticmethod
    def luo_tekoalypeli():
        KPSTekoaly().pelaa()

    @staticmethod
    def luo_vaikeatekoalypeli():
        KPSParempiTekoaly().pelaa()

# luokka perii luokan KiviPaperiSakset
class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto

# luokka perii luokan KiviPaperiSakset
class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto

# luokka perii luokan KiviPaperiSakset
class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto