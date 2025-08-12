# Bus 1 (Horizontal)
bus1_json = {
    "type": "bus",
    "id": "bus1",
    "data": {
        "name": "Bus 1",
        "direction": "horizontal",
        "position": [200, 200],
        "length": 500,
        "widthscale": 1.5,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 3
        },
        "downport": {
            "margin": 0.1,
            "number": 7
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
        "position": [600, 500],
        "length": 200,
        "widthscale": 1.2,
        "color": "red",
        "upport": {
            "margin": 0.1,
            "number": 3
        },
        "downport": {
            "margin": 0.1,
            "number": 3
        }
    }
}

# Line connecting bus1:d0 → bus2:u1 with intermediate point and cubicles
line_json = {
    "type": "line",
    "id": "line1",
    "data": {
        "name": "Line 1",
        "from": "bus1:d0",
        "to": "bus2:u1",
        "point": [
            ["bus1:d0:x", "bus2:u1:y"]  # Intermediate point creating L-shape
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
                    "attach": "bus1:d0"
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

line_json2 = {
    "type": "line",
    "id": "line2",
    "data": {
        "name": "Line 2",
        "from": "bus1:d1",
        "to": "bus2:u0",
        "point": [
            ["bus1:d1:x", "bus2:u0:y"]  # Intermediate point creating L-shape
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "breaker",
                "id": "brk3",
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
                "id": "brk4",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus2:u0"
                }
            }
        ]
    }
}

# Load element
load_json = {
    "type": "load",
    "id": "load1",
    "data": {
        "name": "Load 1",
        "from": "bus1:d2",
        "point": [
            ["bus1:d2:x", 300]  # or any point format you support
        ],
        "color": "red",
        "linescale": 1.0,
        "tri_base": 24,
        "tri_height": 30,
        "cubicle": [
            {
                "type": "breaker",
                "id": "brk3",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus1:d2"
                }
            }
        ]
    }
}

# Generator element
gen_json = {
    "type": "gen",
    "id": "gen1",
    "data": {
        "name": "Generator 1",
        "from": "bus1:d3",
        "point": [
            ["bus1:d3:x", 300]  # You can use coordinates or references like "bus1:d3"
        ],
        "color": "red",
        "linescale": 1.0,
        "gen_radius": 20,      # Optional: radius of the generator symbol (circle)
        "cubicle": [
            {
                "type": "breaker",
                "id": "brk_gen1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus1:d3"
                }
            }
        ]
    }
}

# Transformer element
trafo_json = {
    "type": "trafo",
    "id": "trafo1",
    "data": {
        "name": "Transformer 1",
        "from": "bus1:d4",
        "to": "bus2:u2",
        "point": [
            ["bus1:d4:x", 350],         # from-side intermediate point (optional)
            # ["bus1:d4:x", 350],         # from-side end point (pf)
            "split",            # separates from-side and to-side
            ["bus1:d4:x", 420],         # to-side start point (pt)
            ["bus1:d4:x", "bus2:u2:y"]          # to-side intermediate/end point (optional)
        ],
        "color": "orange",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "breaker",
                "id": "brk_trafo1",
                "data": {
                    "color": "orange",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus1:d4"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "sw_trafo1",
                "data": {
                    "color": "orange",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus2:u2"
                }
            }
        ]
    }
}

# Inverter element
inv_json = {
    "type": "inv",
    "id": "inv1",
    "data": {
        "name": "Inverter 1",
        "from": "bus1:d5",
        "point": [
            ["bus1:d5:x", 300]
        ],
        "color": "red",
        "linescale": 1.0,
        "inv_size": 32,
        "cubicle": [
            {
                "type": "breaker",
                "id": "brk_inv1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bus1:d5"
                }
            }
        ]
    }
}

bess_json = {
    "type": "bess",
    "id": "bess1",
    "data": {
        "name": "BESS 1",
        "from": "bus1:d6",
        "point": [
            ['bus1:d6:x', 300]
        ],
        "color": "red",
        "linescale": 1.0,
        "bess_size": 32,
        "cubicle": [
            {
                "type": "recloser",
                "id": "brk_bess1",
                "data": {
                    "color": "red",
                    "scale": 3.0,
                    "offset": [0, 20],
                    "attach": "bus1:d6"
                }
            }
        ]
    }
}

# Example text elements
text_json1 = {
    "type": "text",
    "id": "bus1_label",
    "data": {
        "text": "Bus 1 - Main",
        "position": "bus1:u1",  # Position relative to bus1 upper port 1
        "font": {
            "family": "Arial",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "bottommid",  # Bottom middle of text aligns with the position
        "offset": [0, -10],     # 10 pixels above the reference point
        "rotation": 0
    }
}

text_json2 = {
    "type": "text",
    "id": "gen_label",
    "data": {
        "text": "Generator\n50 MW",
        "position": [300, 320],  # Absolute position
        "font": {
            "family": "Helvetica",
            "size": 10,
            "bold": False,
            "italic": False
        },
        "color": "yellow",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": -15  # Rotated 15 degrees counter-clockwise
    }
}
