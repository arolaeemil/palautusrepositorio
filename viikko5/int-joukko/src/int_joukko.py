KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        vastaavat_alkiot = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                vastaavat_alkiot += 1

        if vastaavat_alkiot > 0:
            return True
        else:
            return False

    def lisaa(self, n):
        ei_ole = 0

        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def alusta_operaatio(a,b):
        return IntJoukko(), a.to_int_list(), b.to_int_list()

    @staticmethod
    def yhdiste(a,b):
        yhdiste_joukko, joukko1, joukko2 = IntJoukko.alusta_operaatio(a,b)

        for i in range(0, len(joukko1)):
            yhdiste_joukko.lisaa(joukko1[i])

        for i in range(0, len(joukko2)):
            yhdiste_joukko.lisaa(joukko2[i])

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko, joukko1, joukko2 = IntJoukko.alusta_operaatio(a,b)

        for i in range(0, len(joukko1)):
            for j in range(0, len(joukko2)):
                if joukko1[i] == joukko2[j]:
                    leikkaus_joukko.lisaa(joukko2[j])

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko, joukko1, joukko2 = IntJoukko.alusta_operaatio(a,b)

        for i in range(0, len(joukko1)):
            erotus_joukko.lisaa(joukko1[i])

        for i in range(0, len(joukko2)):
            erotus_joukko.poista(joukko2[i])

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i]) + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1]) + "}"
            return tuotos
