GRID_SIZE_X = 100
GRID_SIZE_Y = 100

load1_json = {
    "type": "load",
    "id": "load1",
    "data": {
        "name": "Load 1",
        "from": "umphang_bus:d7",
        "point": [

            ["umphang_bus:d7:x", 600]
        ],
        "color": "red",
        "linescale": 1.0,
        "load_size": 40,
        "cubicle": [
            {
                "type": "switch",
                "id": "umphang_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:d7",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

load2_json = {
    "type": "load",
    "id": "load2",
    "data": {
        "name": "Load 2",
        "from": "umphang_bus:d8",
        "point": [

            ["umphang_bus:d8:x", 600]
        ],
        "color": "red",
        "linescale": 1.0,
        "load_size": 40,
        "cubicle": [
            {
                "type": "switch",
                "id": "umphang_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:d8",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

load3_json = {
    "type": "load",
    "id": "load3",
    "data": {
        "name": "Load 3",
        "from": "umphang_bus:d9",
        "point": [

            ["umphang_bus:d9:x", 600]
        ],
        "color": "red",
        "linescale": 1.0,
        "load_size": 40,
        "cubicle": [
            {
                "type": "switch",
                "id": "umphang_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:d9",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

load4_json = {
    "type": "load",
    "id": "load4",
    "data": {
        "name": "Load 4",
        "from": "umphang_bus:d10",
        "point": [

            ["umphang_bus:d10:x", 600]
        ],
        "color": "red",
        "linescale": 1.0,
        "load_size": 40,
        "cubicle": [
            {
                "type": "switch",
                "id": "umphang_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "umphang_bus:d10",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}