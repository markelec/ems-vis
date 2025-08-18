GRID_SIZE_X = 100
GRID_SIZE_Y = 100

bess_tr_json = {
    "type": "trafo",
    "id": "bess_tr",
    "data": {
        "name": "22 / 0.4 KV BESS TR",
        "from": "umphang_bus:d1",
        "to": "bess_ac_bus:u2",
        "point": [
            [ "umphang_bus:d1:x", 450],
            "split",
            ["bess_ac_bus:u2:x", 550]
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

gen_tr_json = {
    "type": "trafo",
    "id": "gen_tr",
    "data": {
        "name": "22 / 0.4 KV GEN TR",
        "from": "umphang_bus:d11",
        "to": "diesel_bus:u2",
        "point": [
            [ "umphang_bus:d11:x", 525],
            "split",
            ["diesel_bus:u2:x", 625]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "umphang_swt11",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "umphang_bus:d11",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "diesel_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 30],
                    "attach": "diesel_bus:u2",
                    "direction": "up_right"
                }
            }
        ]
    }
}
