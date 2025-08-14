GRID_SIZE_X = 100
GRID_SIZE_Y = 100

# Main 22kV Bus (Horizontal)
umphang_bus_json = {
    "type": "bus",
    "id": "umphang_bus",
    "data": {
        "name": "22 kV UMPHANG",
        "direction": "horizontal",
        "position": [3*GRID_SIZE_X, 350],
        "length": 13*GRID_SIZE_X,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 1/26,
            "number": 12
        },
        "downport": {
            "margin": 1/26,
            "number": 12
        }
    }
}

# Main 22kV Bus (Horizontal)
maesot_bus_json = {
    "type": "bus",
    "id": "maesot_bus",
    "data": {
        "name": "22 kV MAE SOT",
        "direction": "horizontal",
        "position": [17*GRID_SIZE_X, GRID_SIZE_Y],
        "length": 2*GRID_SIZE_X,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

# BESS 22kV AC Bus (Horizontal)
bess_ac_bus_json = {
    "type": "bus",
    "id": "bess_ac_bus",
    "data": {
        "name": "BESS 22kV AC",
        "direction": "horizontal",
        "position": [0.5*GRID_SIZE_X, 600],
        "length": 6*GRID_SIZE_X*1.5,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 1/12,
            "number": 5
        },
        "downport": {
            "margin": 1/12,
            "number": 5
        }
    }
}

# BESS 22kV DC Bus (Horizontal)
bess_dc_bus_json = {
    "type": "bus",
    "id": "bess_dc_bus",
    "data": {
        "name": "BESS 22kV DC",
        "direction": "horizontal",
        "position": [0.5*GRID_SIZE_X, 850],
        "length": 6*GRID_SIZE_X*1.5,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 1/12,
            "number": 5
        },
        "downport": {
            "margin": 1/12,
            "number": 5
        }
    }
}

# Diesel Generator 22kV Bus (Horizontal)
diesel_bus_json = {
    "type": "bus",
    "id": "diesel_bus",
    "data": {
        "name": "DIESEL GENERATOR 22kV",
        "direction": "horizontal",
        "position": [12*GRID_SIZE_X, 800],
        "length": 6*GRID_SIZE_X,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 5
        },
        "downport": {
            "margin": 0.1,
            "number": 5
        }
    }
}

terminal1_bus_json = {
    "type": "bus",
    "id": "terminal1_bus",
    "data": {
        "name": "TERMINAL 1 22kV",
        "direction": "point",
        "position": [4*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal2_bus_json = {
    "type": "bus",
    "id": "terminal2_bus",
    "data": {
        "name": "TERMINAL 2 22kV",
        "direction": "point",
        "position": [5*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal3_bus_json = {
    "type": "bus",
    "id": "terminal3_bus",
    "data": {
        "name": "TERMINAL 3 22kV",
        "direction": "point",
        "position": [6*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal4_bus_json = {
    "type": "bus",
    "id": "terminal4_bus",
    "data": {
        "name": "TERMINAL 4 22kV",
        "direction": "point",
        "position": [7*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal5_bus_json = {
    "type": "bus",
    "id": "terminal5_bus",
    "data": {
        "name": "TERMINAL 5 22kV",
        "direction": "point",
        "position": [8*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal6_bus_json = {
    "type": "bus",
    "id": "terminal6_bus",
    "data": {
        "name": "TERMINAL 6 22kV",
        "direction": "point",
        "position": [9*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal7_bus_json = {
    "type": "bus",
    "id": "terminal7_bus",
    "data": {
        "name": "TERMINAL 7 22kV",
        "direction": "point",
        "position": [10*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal8_bus_json = {
    "type": "bus",
    "id": "terminal8_bus",
    "data": {
        "name": "TERMINAL 8 22kV",
        "direction": "point",
        "position": [11*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal9_bus_json = {
    "type": "bus",
    "id": "terminal9_bus",
    "data": {
        "name": "TERMINAL 9 22kV",
        "direction": "point",
        "position": [12*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal10_bus_json = {
    "type": "bus",
    "id": "terminal10_bus",
    "data": {
        "name": "TERMINAL 10 22kV",
        "direction": "point",
        "position": [13*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal11_bus_json = {
    "type": "bus",
    "id": "terminal11_bus",
    "data": {
        "name": "TERMINAL 11 22kV",
        "direction": "point",
        "position": [14*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal12_bus_json = {
    "type": "bus",
    "id": "terminal12_bus",
    "data": {
        "name": "TERMINAL 12 22kV",
        "direction": "point",
        "position": [15*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}

terminal13_bus_json = {
    "type": "bus",
    "id": "terminal13_bus",
    "data": {
        "name": "TERMINAL 13 22kV",
        "direction": "point",
        "position": [16*GRID_SIZE_X, 250],
        "length": 1,
        "widthscale": 1.0,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 1
        },
        "downport": {
            "margin": 0.1,
            "number": 1
        }
    }
}
