# SilentPod – Csendkapszula-foglaló

**Hallgató:** Ipacs Gábor  
**Tantárgy:** Szkript nyelvek – Python

## A feladat leírása

A SilentPod egy három csendkapszulát kezelő, grafikus Python-bemutatóprogram. A felhasználó nevet és 30, 60 vagy 90 perces időtartamot adhat meg, majd lefoglalhat egy szabad kapszulát. A foglalás lemondható. Karbantartás alatt álló vagy már foglalt kapszula nem foglalható. A program a foglalások időtartamáról statisztikát is készít.

A foglalások **nem valós időpontokra** szólnak: a program az aktuális foglaltságot szimulálja. A foglalások és a statisztikai adatok a program bezárásakor elvesznek.

## Indítás

Python 3 szükséges. Külső csomag telepítése nem szükséges. Nyissuk meg a projektet a PyCharmban, és futtassuk a `main.py` fájlt.

## Modulok és a bennük használt függvények

- **Tanult grafikus modul:** `tkinter` és `tkinter.ttk` – `Tk()`, `StringVar()`, `Entry()`, `Combobox()`, `Button()`, `Label()`, `grid()`, `config()`, `mainloop()`.
- **Tanult üzenetablakmodul:** `tkinter.messagebox` – `showinfo()`, `showwarning()`.
- **Bemutatandó modul:** `statistics` – `mean()` (átlag), `median()` (medián), `multimode()` (leggyakoribb értékek). A három függvény a foglalási időtartamok listáján működik.
- **Saját modul:** `ig_pod.py` – `IGKapszula` osztály, `ig_foglalas()` függvény.

## Saját osztály

`IGKapszula`: egy kapszula azonosítóját, foglalóját, időtartamát és karbantartási állapotát tárolja. Metódusai: `__init__()`, `allapot()`, `foglal()`, `lemond()`.

## Saját függvények és eseménykezelés

- `ig_foglalas()` – a név és az időtartam ellenőrzése, majd a foglalás végrehajtása.
- `foglalas()` – a Foglalás gomb eseménykezelője.
- `lemondas()` – a Lemondás gomb eseménykezelője.
- `karbantartas()` – a karbantartási állapot váltása.
- `frissites()` – a kapszulák állapotának frissítése.
- `statisztika_megjelenites()` – statisztikai adatok számítása és megjelenítése.

## Kipróbálás

1. Válasszuk az 1. kapszulát, írjunk be egy nevet, majd foglaljunk 30 percre.
2. Próbáljuk ugyanazt a kapszulát ismét lefoglalni: a program figyelmeztet.
3. Mondjuk le a foglalást, majd kapcsoljuk be a karbantartást.
4. Próbáljunk karbantartás alatt foglalni: a program elutasítja.
5. Kapcsoljuk ki a karbantartást, foglaljunk több kapszulát eltérő időtartamokra, majd nyomjuk meg a Statisztika gombot.

## A projekt fájljai

- `main.py` – a grafikus felület és az eseménykezelés; `root` az alapablak, `app` a fő keret.
- `ig_pod.py` – a saját modul, saját osztály és saját függvény.
