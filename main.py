import tkinter as tk
from tkinter import ttk, messagebox
import statistics
from ig_pod import IGKapszula, ig_foglalas

kapszulak = [IGKapszula(1), IGKapszula(2), IGKapszula(3)]
foglalasi_idok = []

root = tk.Tk()
root.title('SilentPod – Csendkapszula-foglaló')
root.geometry('620x520')
root.resizable(False, False)
app = ttk.Frame(root, padding=18)
app.pack(fill='both', expand=True)

ttk.Label(app, text='SilentPod', font=('Arial', 20, 'bold')).grid(row=0, column=0, columnspan=3, pady=(0, 4))
ttk.Label(app, text='Három csendkapszula foglalása – bemutató alkalmazás').grid(row=1, column=0, columnspan=3, pady=(0, 18))

allapot_cimkek = []
for i in range(3):
    ttk.Label(app, text=f'{i + 1}. kapszula', font=('Arial', 11, 'bold')).grid(row=2, column=i, padx=25)
    cimke = ttk.Label(app, text='Szabad')
    cimke.grid(row=3, column=i, pady=(4, 15))
    allapot_cimkek.append(cimke)

ttk.Label(app, text='Kapszula:').grid(row=4, column=0, sticky='e', pady=6)
kapszula_valasztas = tk.StringVar(value='1')
ttk.Combobox(app, textvariable=kapszula_valasztas, values=['1', '2', '3'], state='readonly', width=20).grid(row=4, column=1, sticky='w')

ttk.Label(app, text='Név:').grid(row=5, column=0, sticky='e', pady=6)
nev_valtozo = tk.StringVar()
ttk.Entry(app, textvariable=nev_valtozo, width=23).grid(row=5, column=1, sticky='w')

ttk.Label(app, text='Időtartam (perc):').grid(row=6, column=0, sticky='e', pady=6)
perc_valtozo = tk.StringVar(value='30')
ttk.Combobox(app, textvariable=perc_valtozo, values=['30', '60', '90'], state='readonly', width=20).grid(row=6, column=1, sticky='w')

naplo = tk.StringVar(value='A rendszer készen áll.')
statisztika = tk.StringVar(value='Még nem történt foglalás.')


def kivalasztott_kapszula():
    return kapszulak[int(kapszula_valasztas.get()) - 1]


def frissites():
    for i in range(3):
        kapszula = kapszulak[i]
        szoveg = kapszula.allapot()
        if kapszula.nev:
            szoveg += f' – {kapszula.nev} ({kapszula.perc} perc)'
        allapot_cimkek[i].config(text=szoveg)


def foglalas():
    kapszula = kivalasztott_kapszula()
    siker, uzenet = ig_foglalas(nev_valtozo.get(), perc_valtozo.get(), kapszula)
    if siker:
        foglalasi_idok.append(kapszula.perc)
        naplo.set(f'{kapszula.azonosito}. kapszula: {uzenet}')
        frissites()
        messagebox.showinfo('Foglalás', uzenet)
    else:
        messagebox.showwarning('Nem sikerült', uzenet)


def lemondas():
    kapszula = kivalasztott_kapszula()
    siker, uzenet = kapszula.lemond()
    if siker:
        naplo.set(f'{kapszula.azonosito}. kapszula: {uzenet}')
        frissites()
        messagebox.showinfo('Lemondás', uzenet)
    else:
        messagebox.showwarning('Nem sikerült', uzenet)


def karbantartas():
    kapszula = kivalasztott_kapszula()
    if kapszula.nev:
        messagebox.showwarning('Karbantartás', 'Foglalt kapszula nem állítható karbantartásra.')
        return
    kapszula.karbantartas = not kapszula.karbantartas
    naplo.set(f'{kapszula.azonosito}. kapszula: {kapszula.allapot()}')
    frissites()


def statisztika_megjelenites():
    if not foglalasi_idok:
        messagebox.showinfo('Statisztika', 'Még nincs foglalási adat.')
        return
    atlag = statistics.mean(foglalasi_idok)
    median = statistics.median(foglalasi_idok)
    leggyakoribb = statistics.multimode(foglalasi_idok)
    szoveg = (f'Foglalások száma: {len(foglalasi_idok)}\n'
              f'Átlagos időtartam: {atlag:.1f} perc\n'
              f'Medián időtartam: {median:.1f} perc\n'
              f'Leggyakoribb időtartam(ok): {", ".join(str(x) for x in leggyakoribb)} perc')
    statisztika.set(szoveg.replace('\n', ' | '))
    messagebox.showinfo('Foglalási statisztika', szoveg)


ttk.Button(app, text='Foglalás', command=foglalas).grid(row=7, column=0, pady=(20, 12), padx=5)
ttk.Button(app, text='Lemondás', command=lemondas).grid(row=7, column=1, pady=(20, 12), padx=5)
ttk.Button(app, text='Karbantartás be/ki', command=karbantartas).grid(row=7, column=2, pady=(20, 12), padx=5)
ttk.Button(app, text='Statisztika', command=statisztika_megjelenites).grid(row=8, column=1, pady=8)
ttk.Label(app, text='Utolsó művelet:', font=('Arial', 10, 'bold')).grid(row=9, column=0, columnspan=3, pady=(16, 4))
ttk.Label(app, textvariable=naplo).grid(row=10, column=0, columnspan=3)
ttk.Label(app, text='A foglalások csak a program futása alatt maradnak meg.', foreground='gray').grid(row=11, column=0, columnspan=3, pady=(20, 0))

frissites()
root.mainloop()
