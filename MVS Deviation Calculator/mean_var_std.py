import numpy as np

def numpy_to_list(calc, x):

    
    calc = {k:[x(y) for y in v] for k,v in calc.items()} #k -> key, v -> value, y -> item from value array

    return calc

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    tmp = np.copy(list)
    tmp = tmp.reshape(3,3)

    calculations = {
                    'mean': [],
                    'variance': [],
                    'standard deviation': [],
                    'max': [],
                    'min': [],
                    'sum': []
                    }


    calculations['mean'] = [tmp.mean(axis=0), tmp.mean(axis=1), tmp.flatten().mean()]
    calculations['variance'] = [tmp.var(axis=0), tmp.var(axis=1), tmp.flatten().var()]
    calculations['standard deviation'] = [tmp.std(axis=0), tmp.std(axis=1), tmp.flatten().std()]
    calculations['max'] = [tmp.max(axis=0), tmp.max(axis=1), tmp.flatten().max()]
    calculations['min'] = [tmp.min(axis=0), tmp.min(axis=1), tmp.flatten().min()]
    calculations['sum'] = [tmp.sum(axis=0), tmp.sum(axis=1), tmp.flatten().sum()]

    x = lambda v: v.tolist() # numpy array to list

    calculations = numpy_to_list(calculations, x)

    return calculations