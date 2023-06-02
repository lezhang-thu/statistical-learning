import numpy as np
import math


def get_prediction(x):
    prediction = np.zeros(x.shape[0])
    prediction[x < 2.5] = 1
    prediction[x > 2.5] = -1
    return prediction


if __name__ == '__main__':
    x = np.asarray(range(10))
    #print(x)
    y = np.ones(10)
    y[3:6] = -1
    y[9] = -1
    #print(y)
    weights = np.ones(10) / 10
    print(weights)
    error = 0.3

    alpha = 1 / 2 * math.log((1 - error) / error)
    predict = get_prediction(x)
    #print('predict: {}'.format(predict))
    weights[predict == y] = weights[predict == y] * math.exp(-alpha)
    weights[predict != y] = weights[predict != y] * math.exp(alpha)
    weights = weights / weights.sum()
    print(weights)
