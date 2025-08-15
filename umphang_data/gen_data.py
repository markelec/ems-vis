GRID_SIZE_X = 100
GRID_SIZE_Y = 100

gen1_json = {
    "type": "gen",
    "id": "gen1",
    "data": {
        "name": "Generator 1",
        "from": "diesel_bus:d0",
        "point": [

            ["diesel_bus:d0:x", 900]
        ],
        "color": "red",
        "text_color": "white",
        "linescale": 1.0,
        "gen_size": 80,
        "cubicle": [
            {
                "type": "switch",
                "id": "diesel_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:d0",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

gen2_json = {
    "type": "gen",
    "id": "gen2",
    "data": {
        "name": "Generator 2",
        "from": "diesel_bus:d1",
        "point": [

            ["diesel_bus:d1:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_size": 80,
        "cubicle": [
            {
                "type": "switch",
                "id": "diesel_swt2",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:d1",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

gen3_json = {
    "type": "gen",
    "id": "gen3",
    "data": {
        "name": "Generator 3",
        "from": "diesel_bus:d2",
        "point": [

            ["diesel_bus:d2:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_size": 80,
        "cubicle": [
            {
                "type": "switch",
                "id": "diesel_swt3",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:d2",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

gen4_json = {
    "type": "gen",
    "id": "gen4",
    "data": {
        "name": "Generator 4",
        "from": "diesel_bus:d3",
        "point": [

            ["diesel_bus:d3:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_size": 80,
        "cubicle": [
            {
                "type": "switch",
                "id": "diesel_swt4",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:d3",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}

gen5_json = {
    "type": "gen",
    "id": "gen5",
    "data": {
        "name": "Generator 5",
        "from": "diesel_bus:d4",
        "point": [

            ["diesel_bus:d4:x", 900]
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_size": 80,
        "cubicle": [
            {
                "type": "switch",
                "id": "diesel_swt5",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:d4",
                    "direction": "up_left"
                }
            }
        ],
        
    }
}