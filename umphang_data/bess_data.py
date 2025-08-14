GRID_SIZE_X = 100
GRID_SIZE_Y = 100

bess1_json = {
    "type": "bess",
    "id": "bess1",
    "data": {
        "name": "BESS 1",
        "from": "bess_dc_bus:d1",
        "point": [

            ["bess_dc_bus:d1:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 100,
        "cubicle": [
            {
                "type": "switch",
                "id": "bess_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:d1",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

bess2_json = {
    "type": "bess",
    "id": "bess2",
    "data": {
        "name": "BESS 2",
        "from": "bess_dc_bus:d2",
        "point": [

            ["bess_dc_bus:d2:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 100,
        "cubicle": [
            {
                "type": "switch",
                "id": "bess_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:d2",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

bess3_json = {
    "type": "bess",
    "id": "bess3",
    "data": {
        "name": "BESS 3",
        "from": "bess_dc_bus:d3",
        "point": [

            ["bess_dc_bus:d3:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 100,
        "cubicle": [
            {
                "type": "switch",
                "id": "bess_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:d3",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}