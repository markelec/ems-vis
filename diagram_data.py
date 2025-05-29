# Bus 1 (Horizontal)
bus1_json = {
    "type": "bus",
    "id": "bus1",
    "data": {
        "name": "Bus 1",
        "direction": "horizontal",
        "position": [100, 200],
        "length": 300,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 3
        },
        "downport": {
            "margin": 0.1,
            "number": 2
        }
    }
}

# Bus 2 (Vertical)
bus2_json = {
    "type": "bus",
    "id": "bus2",
    "data": {
        "name": "Bus 2",
        "direction": "vertical",
        "position": [400, 300],
        "length": 200,
        "widthscale": 1.2,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 2
        },
        "downport": {
            "margin": 0.1,
            "number": 3
        }
    }
}

# Line connecting bus1:u1 → bus2:d0 with bends and cubicles
line_json = {
    "type": "line",
    "id": "line1",
    "data": {
        "name": "Line 1",
        "from": "bus1:d1",
        "to": "bus2:u1",
        "point": [
            [250, 400],  # intermediate bend
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "breaker",
                "id": "brk1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus1:d1"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "brk2",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus2:u1"
                }
            }
        ]
    }
}
