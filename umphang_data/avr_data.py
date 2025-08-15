GRID_SIZE_X = 100
GRID_SIZE_Y = 100

avr1_json = {
    "type": "avr",
    "id": "avr1",
    "data": {
        "name": "AVR 1",
        "from": "terminal1_bus:d0",
        "to": "terminal2_bus:u0",
        "point": [
            [ 430, 250],
            "split",
            [ 470, 250]
        ],
        "color": "red",
        "text_color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "terminal1_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal1_bus:d0",
                    "direction": "up_left"
                }
            }
        ]
        
    }
}

avr2_json = {
    "type": "avr",
    "id": "avr2",
    "data": {
        "name": "AVR 2",
        "from": "terminal5_bus:d0",
        "to": "terminal6_bus:u0",
        "point": [
            [ 830, 250],
            "split",
            [ 870, 250]
        ],
        "color": "red",
        "text_color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "terminal5_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal5_bus:d0",
                    "direction": "up_left"
                }
            }
        ]
        
    }
}
