class IGKapszula:
    def __init__(self, azonosito):
        self.azonosito = azonosito
        self.nev = ''
        self.perc = 0
        self.karbantartas = False

    def allapot(self):
        if self.karbantartas:
            return 'Karbantartás'
        if self.nev:
            return 'Foglalt'
        return 'Szabad'

    def foglal(self, nev, perc):
        if self.karbantartas:
            return False, 'A kapszula karbantartás alatt áll.'
        if self.nev:
            return False, 'A kapszula már foglalt.'
        self.nev = nev
        self.perc = perc
        return True, 'Sikeres foglalás.'

    def lemond(self):
        if not self.nev:
            return False, 'Nincs lemondható foglalás.'
        self.nev = ''
        self.perc = 0
        return True, 'A foglalást töröltük.'


def ig_foglalas(nev, perc_szoveg, kapszula):
    nev = nev.strip()
    if not nev:
        return False, 'Add meg a foglaló nevét!'
    try:
        perc = int(perc_szoveg)
    except ValueError:
        return False, 'A foglalási időnek számnak kell lennie.'
    if perc not in (30, 60, 90):
        return False, 'Csak 30, 60 vagy 90 perc választható.'
    return kapszula.foglal(nev, perc)
