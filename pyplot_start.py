from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# cria o gráfico de linha - anos no eixo x, pib no eixo y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# põe um título
plt.title("PIB Nominal")

# põe uma legenda no eixo y
plt.ylabel("Bilhões de $")

plt.show()
plt.savefig("pyplot01.png")