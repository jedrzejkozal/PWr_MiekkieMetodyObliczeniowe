import numpy as np


def get_data():
    x_data = np.array([
        [35.5,	0.0,	1.0,	0.0,	0.0,	0.0],
        [35.9,	0.0,	0.0,	1.0,	1.0,	1.0],
        [35.9,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.0,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.0,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.0,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.2,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.2,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.3,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.6,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.6,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.6,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.6,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.7,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.7,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.7,	0.0,	1.0,	0.0,	0.0,	0.0],
        [36.8,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.8,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.9,	0.0,	0.0,	1.0,	1.0,	1.0],
        [36.9,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.0,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.0,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.0,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.1,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.1,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.1,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.2,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.2,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.2,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.3,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.3,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.3,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.4,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.4,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.5,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.5,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.5,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.5,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.5,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.5,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.6,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.6,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.6,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.7,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.7,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.7,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.7,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.8,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.8,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.8,	0.0,	0.0,	1.0,	0.0,	0.0],
        [37.9,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.9,	0.0,	0.0,	1.0,	1.0,	0.0],
        [37.9,	0.0,	1.0,	0.0,	0.0,	0.0],
        [37.9,	0.0,	0.0,	1.0,	1.0,	1.0],
        [37.9,	0.0,	0.0,	1.0,	0.0,	0.0],
        [38.0,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.0,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.1,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.3,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.5,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.7,	0.0,	1.0,	1.0,	0.0,	1.0],
        [38.9,	0.0,	1.0,	1.0,	0.0,	1.0],
        [39.0,	0.0,	1.0,	1.0,	0.0,	1.0],
        [39.4,	0.0,	1.0,	1.0,	0.0,	1.0],
        [39.7,	0.0,	1.0,	1.0,	0.0,	1.0],
        [40.0,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.0,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.0,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.0,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.0,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.0,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.0,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.0,	0.0,	1.0,	1.0,	0.0,	1.0],
        [40.1,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.2,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.2,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.2,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.3,	0.0,	1.0,	1.0,	0.0,	1.0],
        [40.4,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.4,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.4,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.4,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.4,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.5,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.6,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.6,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.6,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.7,	1.0,	1.0,	1.0,	1.0,	1.0],
        [40.7,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.7,	0.0,	0.0,	0.0,	0.0,	0.0],
        [40.7,	1.0,	1.0,	0.0,	1.0,	0.0],
        [40.7,	0.0,	1.0,	1.0,	0.0,	1.0],
        [40.8,	0.0,	1.0,	1.0,	0.0,	1.0],
        [40.9,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.9,	1.0,	1.0,	1.0,	1.0,	0.0],
        [40.9,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.0,	1.0,	1.0,	1.0,	1.0,	1.0],
        [41.0,	0.0,	0.0,	0.0,	0.0,	0.0],
        [41.0,	1.0,	1.0,	0.0,	1.0,	0.0],
        [41.0,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.1,	1.0,	1.0,	1.0,	1.0,	1.0],
        [41.1,	1.0,	1.0,	1.0,	1.0,	0.0],
        [41.1,	0.0,	0.0,	0.0,	0.0,	0.0],
        [41.1,	1.0,	1.0,	0.0,	1.0,	0.0],
        [41.1,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.2,	1.0,	1.0,	1.0,	1.0,	1.0],
        [41.2,	0.0,	0.0,	0.0,	0.0,	0.0],
        [41.2,	1.0,	1.0,	0.0,	1.0,	0.0],
        [41.2,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.3,	1.0,	1.0,	1.0,	1.0,	0.0],
        [41.4,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.5,	0.0,	0.0,	0.0,	0.0,	0.0],
        [41.5,	1.0,	1.0,	0.0,	1.0,	0.0],
        [41.5,	0.0,	1.0,	1.0,	0.0,	1.0],
        [41.5,	0.0,	1.0,	1.0,	0.0,	1.0],
    ])

    y_data = np.array([
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	0.0],
        [1.0,	0.0],
        [1.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [1.0,	1.0],
        [0.0,	1.0],
        [0.0,	0.0],
        [0.0,	1.0],
        [0.0,	1.0],
        [0.0,	1.0],
    ])

    x_data = encode_fever(x_data)
    return x_data, y_data


def encode_fever(x_data):
    temperature = x_data[:, 0]
    fever = np.argwhere(temperature > 38.0)
    no_fever = np.argwhere(temperature <= 38.0)

    x_data[fever, np.zeros_like(fever)] = 1.0
    x_data[no_fever, np.zeros_like(no_fever)] = 0.0
    return x_data
