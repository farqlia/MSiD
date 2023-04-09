"""Zadanie z kreślenia wykresów."""
import matplotlib.pyplot as plt
import numpy as np

# chcemy zapisać dwa wykresy ułożone w jednym wierszu i dwóch kolumnach
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))


# wykres pierwszy
# x to dziedzina: 50 próbek z zakresu [-3, 3] wygenerowanych liniowo
# y to exp(-x^2)
# y_err to szum pochodzący z rozkładu normalnego o zadanych parametrach
# uzupelnij 1 linie
x = np.linspace(-3, 3, 50)
y = np.exp(-(x ** 2))  # to dać do uzupełnienia
y_err = np.random.normal(loc=np.mean(y), scale=0.1, size=len(y))

# plotujemy x, y oraz obszar szumu wokół funkcji
# uzupelnij 1 linie
ax[0].plot(x, y, marker='.', markersize='10', 
           label='$exp(-x^2)$')
ax[0].fill_between(x, y - y_err, y + y_err, alpha=0.2, label="+/- szum")

# dodajemy oznaczenia osi i legendę na górze po lewej stronie
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].legend(loc="upper left")


# wykres drugi
# definiujemy dziedzinę (x) oraz funkcje do wykreślenia (y_1, y_2)
x = np.arange(start=-50.0, stop=50.0, step=0.1)
y_1 = np.cos(x / 3.0)
y_2 = np.sin(x)

# kreślimy obie funkcje
ax[1].plot(x, y_1, label="cos(x/3)")
# uzupelnij 1 linie
ax[1].plot(x, y_2, label="sin(x)")

# ustawiamy skalę osi x na symetryczną-logarytmiczną oraz dodajemy siatkę w
# tle kreślonych krzywych
# uzupelnij 2 linie
ax[1].set_xscale('symlog')
ax[1].grid(True)

# dodajemy oznaczenia osi i legendę na dole po prawej stronie
ax[1].set_xlabel("x")
ax[1].set_ylabel("y")
# uzupelnij 1 linie
ax[1].legend(loc='lower right')

# dodajemy tytuł
plt.suptitle("Funkcje wygenerowane w 'numpy' i wykreślone w 'matplotlib'")
plt.savefig("wykres.png")
