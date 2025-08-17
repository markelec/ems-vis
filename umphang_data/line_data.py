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

recloser1_line_json = {
    "type": "line",
    "id": "recloser1_line",
    "data": {
        "name": "22 KV Recloser 1",
        "from": "terminal2_bus:u0",
        "to": "terminal3_bus:d0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "recloser1",
                "data": {
                    "color": "red",
                    "scale": 5.0,
                    "offset": [0, 20],
                    "attach": "terminal2_bus:u0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "swtch1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal3_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

section1_line_json = {
    "type": "line",
    "id": "section1_line",
    "data": {
        "name": "22 KV Section 1",
        "from": "terminal3_bus:d0",
        "to": "terminal4_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        
    }
}

section2_line_json = {
    "type": "line",
    "id": "section2_line",
    "data": {
        "name": "22 KV Section 2",
        "from": "terminal4_bus:d0",
        "to": "terminal5_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "switch",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal4_bus:u0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "switch1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal5_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

section3_line_json = {
    "type": "line",
    "id": "section3_line",
    "data": {
        "name": "22 KV Section 3",
        "from": "terminal5_bus:d0",
        "to": "terminal6_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        
    }
}

recloser2_line_json = {
    "type": "line",
    "id": "recloser2_line",
    "data": {
        "name": "22 KV Recloser 2",
        "from": "terminal7_bus:d0",
        "to": "terminal8_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "recloser",
                "id": "recloser2",
                "data": {
                    "color": "red",
                    "scale": 5.0,
                    "offset": [0, 20],
                    "attach": "terminal7_bus:d0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "swtch1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal8_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

section4_line_json = {
    "type": "line",
    "id": "section4_line",
    "data": {
        "name": "22 KV Section 4",
        "from": "terminal8_bus:d0",
        "to": "terminal9_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        
    }
}

section5_line_json = {
    "type": "line",
    "id": "section5_line",
    "data": {
        "name": "22 KV Section 5",
        "from": "terminal9_bus:d0",
        "to": "terminal10_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "switch",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal9_bus:u0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "switch1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal10_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

recloser3_line_json = {
    "type": "line",
    "id": "recloser3_line",
    "data": {
        "name": "22 KV Recloser 3",
        "from": "terminal10_bus:d0",
        "to": "terminal11_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "switch3",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "terminal10_bus:d0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "recloser",
                "id": "recloser3",
                "data": {
                    "color": "red",
                    "scale": 5.0,
                    "offset": [0, 20],
                    "attach": "terminal11_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

section6_line_json = {
    "type": "line",
    "id": "section6_line",
    "data": {
        "name": "22 KV Section 6",
        "from": "terminal12_bus:d0",
        "to": "terminal13_bus:u0",
        "point": [
            
        ],
        "color": "red",
        "linescale": 1.0,
        
    }
}

maesot_feeder_line_json = {
    "type": "line",
    "id": "maesot_feeder_line",
    "data": {
        "name": "22 KV Maesot Feeder",
        "from": "maesot_bus:d0",
        "to": "terminal12_bus:d0",
        "point": [
            ["maesot_bus:d0:x", "terminal12_bus:d0:y"],
           
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "switch_ms1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "maesot_bus:d0",
                    "direction": "up_left"
                }
            }
        ]
        
    }
}