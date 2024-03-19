# def pdf_original(k: int, rnd_list: list):
#     """
#     Получает кривую плотности распределения вероятности
#     :param k: количечиво интервалов разбиения гистограммы
#     :param rnd_list: случайный процесс
#     :return: pandas.DataFrame
#     """
#     pdf_x = []  # Координаты по оси абсцисс
#     pdf_y = []  # Координаты по оси ординат
#     n = len(rnd_list)  # количество элементов в рассматриваемой выборке
#     h = (max(rnd_list) - min(rnd_list)) / k  # ширина одного интервала
#     a = min(rnd_list)  # минимальное значение в рассматриваемой выборке
#     for i in range(0, k):  # проход по интервалам
#         count = 0
#         for j in rnd_list:  # подсчет количества вхождений значений из выборки в данный интервал
#             if (a + i * h) < j < (a + (i * h) + h):
#                 count = count + 1
#         pdf_x.append(a + i * h + h / 2)  # координата по оси абсцисс полученной кривой плотности распределения
#         # вероятности
#         pdf_y.append(count / (n * h))  # координата по оси ординат полученной кривой плотности распределения
#         # вероятности
#     d = {'x': pdf_x, 'y': pdf_y}
#     plt.plot(pdf_x, pdf_y, c ="red")
#     return pd.DataFrame(d)
plt.plot(grid, sps.norm.pdf(grid), colo
