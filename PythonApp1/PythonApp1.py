
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#https://www.stat.ee/pressiteade-2019-111
#https://www.stat.ee/pressiteade-2019-104

#Формирование данных и построение диаграммы
x = np.arange(-8, 4, 0.5)  # x - массив np.array
y1 = x**2 + 4*x - 5
y2 = [9] * len(x)

plt.subplots()
plt.title("y = abs(x**2 + 4*x - 5)")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.tick_params(axis="x", direction="in",length=25, width=5,color="red",labelsize=14, labelrotation=20)
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.xticks(np.arange(-8, 4, 1))
plt.grid(True)# Отображение сетки на координатной плоскости




plt.plot(x,y1 ,'--r',linewidth=5,label="Парабола")# График красного цвета
plt.plot(x,y2,'-.g',marker="*",label="Прямая линия")


plt.legend()
plt.text(-7, 24.5, "На диаграмме 2 графика:\nпарабола и линия экстремума")

plt.annotate(r"Экстремум функции = $\frac{-b}{2a} = \frac{-4}{2} = -2$",
                xy=(-2, 9), xytext=(-5, 15),
                arrowprops=dict(facecolor="black", shrink=0.05))

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран
data = [
        ["Питание", 484.7],
        ["Одежда", 691.6],
        ["Учеба", 221.2],
        ["Прочие", 59.4],
        ["Доходы от продажи имущества", 26.7],
        ["Безвозмездные поступления", 75.5]
    ]
values = [x[1] for x in data]
labels = [x[0] for x in data]
plt.pie(values,labels=labels,autopct="%.1f%%", radius=1)
plt.show()
#----------------------------------------
title = "Kinokülastused, 2008‒2018"

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.canvas.set_window_title(title)
fig.suptitle(title +
                 "https://www.stat.ee/pressiteade-2019-127")
    # Настройки диаграммы и осей
ax1.set_xlabel("Aastad")
ax1.set_ylabel("100 elaniku kohta arv")
ax2.set_xlabel("100 elaniku kohta arv")
ax2.set_ylabel("Aastad")

    # https://www.yuripetrov.ru/edu/python/ch_12_01.html#module-matplotlib
data = [
    [2008, 127],
    [2009, 128],
    [2010, 158],
    [2011, 175],
    [2012, 186],
    [2013, 194],
    [2014, 198],
    [2015, 235],
    [2016, 250],
    [2017, 267],
    [2018, 275]
]
size = [x[1] for x in data]
nums = [x + 1 for x in range(len(size))]
tick_label = [x[0] for x in data]

ax1.bar(nums, size, tick_label=tick_label, width=0.5, color="#a500ff")
ax2.barh(nums, size, tick_label=tick_label, height=0.7, color="#ffa500")

plt.show()
title = "Распределение сумм кредитов"

fig, ax = plt.subplots()
fig.canvas.set_window_title(title)

    # Настройки диаграммы и осей
ax.set_title(title)
ax.set_xlabel("Сумма")
ax.set_ylabel("Количество")

    # Суммы кредитов, взятых в банке
data = [40000, 120000, 90000, 160000, 290000, 250000,
            90000, 260000, 170000, 11000, 500000, 250000]

bins_to_be = 3  # Количество интервалов разбиения
n, bins, patches = ax.hist(data, bins=bins_to_be,
                               color="brown", edgecolor="black")

    # Вывод итоговых данных в легенду
res = ""
for i in range(bins_to_be):
    res += "Группа №{}, {:.0f} чел., от {:.2f} руб.\n". \
            format(i+1, n[i], bins[i])

ax.legend([res.strip()])
plt.show()

y_data=[400,60,100,155]
x_data=["cats","dogs","birds","points"]
colors=["r","b","y","g"]
ax = plt.subplots()
plt.scatter(x_data, y_data, s = y_data, color = colors, alpha = 0.75)
plt.show()









