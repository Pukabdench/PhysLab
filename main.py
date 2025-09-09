import pandas as pd
import numpy as np 

import graph

paths = {50: 'data/l50.csv', 20:'data/l20.csv', 10:'data/l10.csv'}
sep =''

def calculate_variance(x_array: np.typing.ArrayLike):
    if x_array.shape[0] != 1:
        raise Exception('Data array for standart deviation calcuation does not consist of one row!')
    mean_x = np.nanmean(x_array)
    mean_x_sq = np.nanmean(x_array**2)
    return mean_x_sq - (mean_x ** 2)


def calculate_linear_regression_mnk(array: np.typing.ArrayLike, x_row = 0, y_row = 1) -> dict:
    if array.shape[0] != 2:
        raise Exception('Data array for linear regression calcuation does not consist of two rows (for x and y)!')
    data_array = np.vsplit(array, 2)
    x_array = data_array[x_row]
    y_array = data_array[y_row]

    n = x_array.shape[1]

    mean_x = np.nanmean(x_array)
    mean_x_sq = np.nanmean(x_array**2)
    mean_y = np.nanmean(y_array)
    mean_y_sq = np.nanmean(y_array**2)
    var_y = mean_y_sq - (mean_y ** 2)
    var_x = mean_x_sq - (mean_x ** 2)
    mean_xy = np.nanmean(x_array * y_array)

    '''
    k = mean_xy/mean_x_sq
    std_k = (mean_y_sq/mean_x_sq - k**2)/(n-1)
    return {'k': k, 'std_k' : std_k}
    '''

    k = (mean_xy - mean_x * mean_y) / var_x
    b = mean_y - k * mean_x

    var_k = ( (var_y/var_x)  - (k **2)) / (n-2)
    var_b = var_k * mean_x_sq


    return {'k' : k, 'b' : b, 'std_k' : var_k ** 0.5, 'std_b' : var_b ** 0.5, 'xa' : x_array, 'ya' : y_array}
    

def process_graph():

    data_set = []
    for l in paths.keys():
        data_frame = pd.read_csv(paths[l])

        main_array = data_frame.to_numpy()

        result = calculate_linear_regression_mnk(main_array)
        k = round(result['k'], 5)
        sk = round(result['std_k'], 5)
        data_set.append({'std_x' : 0.00375 , 'std_y' : 0.0019, 'label' : f'L = {l} см,\nR = {k}±{sk} Ом', 'xarray' : result['xa'], 'yarray' : result['ya'], 'rt' : result})
    graph.plot_graph(data_set)
    
process_graph()
'''
data_frame = pd.read_csv('')
print(calculate_variance(data_frame.to_numpy()))
'''