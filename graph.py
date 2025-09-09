import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

SHAPES = ['yo', 'g^', 'c*', '']

COLORS = ['']

def plot_graph(data_list : list[dict]):
    mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта 
    # Создаем фигуру
    plt.figure(figsize=(10,10))

    # Подписываем оси и график
    #plt.title(r"Это название  графика  $y = x^3$ - да, можно использовать LaTeX:")
    plt.ylabel(r"$U$, мВ")
    plt.xlabel(r"$I$, мА")
    plt.xlim(0, 0.3)
    plt.ylim(0, 2)

    # Добавляем данные

    for i in range(len(data_list)):
        j = data_list[i]
        x = np.linspace(-50,500,50)
        y = j['rt']['k']* x + j['rt']['b']
        plt.plot(x,y, 'black')
        print(j['rt']['k'], j['rt']['b'])
        plt.plot(j['xarray'][0], j['yarray'][0], SHAPES[i], label=j['label'], markersize=10, alpha = 0.78)
        plt.errorbar(j['xarray'][0], j['yarray'][0], yerr=j['std_y'], xerr=j['std_x'], fmt='.', color = 'm', ecolor = 'red', elinewidth=2)   

    

    # Еще данные

    # Данные с ошибками
    # Можно рисовать ошибки
    

    # Активируем сетку
    #plt.grid(b=True, which='major', axis='both', alpha=1)
    #plt.grid(b=True, which='minor', axis='both', alpha=0.5)

    # Активируем легенду графика
    plt.legend()
    # Внимание, запускаете вашу программу как сценарий, то что бы показать график
    # Используйте эту команду
    #plt.show()
    # Сохраняем изображение в текущую директорию
    plt.savefig('export/r2.png')