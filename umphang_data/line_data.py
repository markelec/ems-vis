GRID_SIZE_X = 100
GRID_SIZE_Y = 100

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
