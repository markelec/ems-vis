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

# Mae Sot 22kV Incoming Line
mae_sot_line_json = {
    "type": "line",
    "id": "mae_sot_line",
    "data": {
        "name": "22 KV MAE SOT 5 - UMPHANG",
        "from": "umphang_bus:u0",
        "to": "terminal1_bus:d0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "mae_sot_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:u0"
                }
            }
        ]
    }
}

bess_tr_json = {
    "type": "trafo",
    "id": "bess_tr",
    "data": {
        "name": "22 / 0.4 KV BESS TR",
        "from": "umphang_bus:d1",
        "to": "bess_ac_bus:u2",
        "point": [
            [ "umphang_bus:d1:x", 425],
            "split",
            ["bess_ac_bus:u2:x", 525]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "umphang_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:d1",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:u2",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv1_json = {
    "type": "inverter",
    "id": "bess_inv1",
    "data": {
        "name": "BESS Inverter 1",
        "from": "bess_ac_bus:d0",
        "to": "bess_dc_bus:u0",
        "point": [
            [ "bess_ac_bus:d0:x", 675],
            "split",
            ["bess_dc_bus:u0:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv2_json = {
    "type": "inverter",
    "id": "bess_inv2",
    "data": {
        "name": "BESS Inverter 2",
        "from": "bess_ac_bus:d1",
        "to": "bess_dc_bus:u1",
        "point": [
            [ "bess_ac_bus:d1:x", 675],
            "split",
            ["bess_dc_bus:u1:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d1",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u1",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv3_json = {
    "type": "inverter",
    "id": "bess_inv3",
    "data": {
        "name": "BESS Inverter 3",
        "from": "bess_ac_bus:d2",
        "to": "bess_dc_bus:u2",
        "point": [
            [ "bess_ac_bus:d2:x", 675],
            "split",
            ["bess_dc_bus:u2:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d2",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u2",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv4_json = {
    "type": "inverter",
    "id": "bess_inv4",
    "data": {
        "name": "BESS Inverter 4",
        "from": "bess_ac_bus:d3",
        "to": "bess_dc_bus:u3",
        "point": [
            [ "bess_ac_bus:d3:x", 675],
            "split",
            ["bess_dc_bus:u3:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d3",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u3",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv5_json = {
    "type": "inverter",
    "id": "bess_inv5",
    "data": {
        "name": "BESS Inverter 5",
        "from": "bess_ac_bus:d4",
        "to": "bess_dc_bus:u4",
        "point": [
            [ "bess_ac_bus:d4:x", 675],
            "split",
            ["bess_dc_bus:u4:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d4",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u4",
                    "direction": "up_right"
                }
            }
        ]
    }
}

# BESS Connection Line
bess_connection_json = {
    "type": "line",
    "id": "bess_connection",
    "data": {
        "name": "BESS Connection",
        "from": "main_bus:d0",
        "to": "bess_bus:u1",
        "point": [
            ["main_bus:d0:x", "bess_bus:u1:y"]
        ],
        "color": "black",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "bess_main_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d0"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "recloser",
                "id": "bess_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_bus:u1"
                }
            }
        ]
    }
}

# BESS Systems
bess1_json = {
    "type": "bess",
    "id": "bess1",
    "data": {
        "name": "BESS Unit 1",
        "from": "bess_bus:d0",
        "point": [
            ["bess_bus:d0:x", 750]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 32,
        "cubicle": [
            {
                "type": "inv_conv",
                "id": "bess1_conv",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_bus:d0"
                }
            }
        ]
    }
}

bess2_json = {
    "type": "bess",
    "id": "bess2",
    "data": {
        "name": "BESS Unit 2", 
        "from": "bess_bus:d1",
        "point": [
            ["bess_bus:d1:x", 750]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 32,
        "cubicle": [
            {
                "type": "inv_conv",
                "id": "bess2_conv",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_bus:d1"
                }
            }
        ]
    }
}

bess3_json = {
    "type": "bess",
    "id": "bess3",
    "data": {
        "name": "BESS Unit 3",
        "from": "bess_bus:d2",
        "point": [
            ["bess_bus:d2:x", 750]
        ],
        "color": "red", 
        "linescale": 1.0,
        "bess_size": 32,
        "cubicle": [
            {
                "type": "inv_conv",
                "id": "bess3_conv",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_bus:d2"
                }
            }
        ]
    }
}

# Diesel Generators
gen1_json = {
    "type": "gen",
    "id": "gen1",
    "data": {
        "name": "Generator 1",
        "from": "diesel_bus:u0",
        "point": [
            ["diesel_bus:u0:x", 650]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_radius": 20,
        "cubicle": [
            {
                "type": "breaker",
                "id": "gen1_brk",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "diesel_bus:u0"
                }
            }
        ]
    }
}

gen2_json = {
    "type": "gen",
    "id": "gen2", 
    "data": {
        "name": "Generator 2",
        "from": "diesel_bus:u1",
        "point": [
            ["diesel_bus:u1:x", 650]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_radius": 20,
        "cubicle": [
            {
                "type": "breaker",
                "id": "gen2_brk",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "diesel_bus:u1"
                }
            }
        ]
    }
}

gen3_json = {
    "type": "gen",
    "id": "gen3",
    "data": {
        "name": "Generator 3",
        "from": "diesel_bus:u2",
        "point": [
            ["diesel_bus:u2:x", 650]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_radius": 20,
        "cubicle": [
            {
                "type": "breaker",
                "id": "gen3_brk",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "diesel_bus:u2"
                }
            }
        ]
    }
}

gen4_json = {
    "type": "gen",
    "id": "gen4",
    "data": {
        "name": "Generator 4",
        "from": "diesel_bus:u3",
        "point": [
            ["diesel_bus:u3:x", 650]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_radius": 20,
        "cubicle": [
            {
                "type": "breaker",
                "id": "gen4_brk",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "diesel_bus:u3"
                }
            }
        ]
    }
}

# Diesel Bus Connection to Main Bus
diesel_connection_json = {
    "type": "line",
    "id": "diesel_connection",
    "data": {
        "name": "Diesel Bus Connection",
        "from": "main_bus:d7",
        "to": "diesel_bus:d2",
        "point": [
            ["main_bus:d7:x", 650],
            [1300, 650],
            [1300, "diesel_bus:d2:y"]
        ],
        "color": "black",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "diesel_main_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d7"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "recloser",
                "id": "diesel_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "diesel_bus:d2"
                }
            }
        ]
    }
}

# Distribution Transformers
trafo1_json = {
    "type": "trafo",
    "id": "trafo1",
    "data": {
        "name": "22/0.4 kV TR PALATHA",
        "from": "main_bus:d1",
        "point": [
            ["main_bus:d1:x", 500],
            "split",
            ["main_bus:d1:x", 580]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "trafo1_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d1"
                }
            }
        ]
    }
}

trafo2_json = {
    "type": "trafo",
    "id": "trafo2",
    "data": {
        "name": "22/0.4 kV TR KIO HANG",
        "from": "main_bus:d2",
        "point": [
            ["main_bus:d2:x", 500],
            "split",
            ["main_bus:d2:x", 580]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "trafo2_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d2"
                }
            }
        ]
    }
}

trafo3_json = {
    "type": "trafo",
    "id": "trafo3",
    "data": {
        "name": "22/0.4 kV TR NONG LUANG - MAE CHAN",
        "from": "main_bus:d3",
        "point": [
            ["main_bus:d3:x", 500],
            "split",
            ["main_bus:d3:x", 580]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "trafo3_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d3"
                }
            }
        ]
    }
}

trafo4_json = {
    "type": "trafo",
    "id": "trafo4",
    "data": {
        "name": "22/0.4 kV TR YAMO",
        "from": "main_bus:d4",
        "point": [
            ["main_bus:d4:x", 500],
            "split",
            ["main_bus:d4:x", 580]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "trafo4_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d4"
                }
            }
        ]
    }
}

trafo5_json = {
    "type": "trafo",
    "id": "trafo5",
    "data": {
        "name": "22/0.4 kV TR",
        "from": "main_bus:d6",
        "point": [
            ["main_bus:d6:x", 500],
            "split",
            ["main_bus:d6:x", 580]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "trafo5_rcl",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "main_bus:d6"
                }
            }
        ]
    }
}

# Bus Section Switch
section_switch_json = {
    "type": "line",
    "id": "section_switch",
    "data": {
        "name": "Bus Section",
        "from": "main_bus:u5",
        "to": "main_bus:u6",
        "point": [
            ["main_bus:u5:x", "main_bus:u5:y"],
            ["main_bus:u6:x", "main_bus:u6:y"]
        ],
        "color": "black",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "section_sw",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, -20],
                    "attach": "main_bus:u5"
                }
            }
        ]
    }
}

# Text labels
text_main_bus = {
    "type": "text",
    "id": "main_bus_label",
    "data": {
        "text": "22 KV UMPHANG",
        "position": [950, 390],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_bess_label = {
    "type": "text",
    "id": "bess_label",
    "data": {
        "text": "BESS",
        "position": [120, 580],
        "font": {
            "family": "Helvetica",
            "size": 20,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_diesel_label = {
    "type": "text",
    "id": "diesel_label",
    "data": {
        "text": "DIESEL GENERATOR",
        "position": [1300, 830],
        "font": {
            "family": "Helvetica",
            "size": 20,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_mae_sot_label = {
    "type": "text",
    "id": "mae_sot_label",
    "data": {
        "text": "22 KV MAE SOT 5",
        "position": [1780, 70],
        "font": {
            "family": "Helvetica",
            "size": 18,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

# Load labels for feeders
text_palatha = {
    "type": "text",
    "id": "palatha_label",
    "data": {
        "text": "PALATHA",
        "position": [820, 614],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_kio_hang = {
    "type": "text",
    "id": "kio_hang_label",
    "data": {
        "text": "KIO HANG",
        "position": [1000, 612],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_nong_luang = {
    "type": "text",
    "id": "nong_luang_label",
    "data": {
        "text": "NONG LUANG - MAE CHAN",
        "position": [1205, 616],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_yamo = {
    "type": "text",
    "id": "yamo_label",
    "data": {
        "text": "YAMO",
        "position": [1406, 618],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "black",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}