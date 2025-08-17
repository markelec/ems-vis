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
            [ "terminal1_bus:d0:x+30", 250],
            "split",
            [ "terminal2_bus:u0:x-30", 250]
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
        "from": "terminal6_bus:d0",
        "to": "terminal7_bus:u0",
        "point": [
            [ "terminal6_bus:d0:x+30", 250],
            "split",
            [ "terminal7_bus:u0:x-30", 250]
        ],
        "color": "red",
        "text_color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "terminal6_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal6_bus:d0",
                    "direction": "up_left"
                }
            }
        ]
        
    }
}

avr3_json = {
    "type": "avr",
    "id": "avr3",
    "data": {
        "name": "AVR 3",
        "from": "terminal11_bus:d0",
        "to": "terminal12_bus:u0",
        "point": [
            [ "terminal11_bus:d0:x+30", 250],
            "split",
            [ "terminal12_bus:u0:x-30", 250]
        ],
        "color": "red",
        "text_color": "red",
        "linescale": 1.0,
        "cubicle2": [
            {
                "type": "switch",
                "id": "terminal12_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal12_bus:d0",
                    "direction": "up_right"
                }
            }
        ]
        
    }
}
