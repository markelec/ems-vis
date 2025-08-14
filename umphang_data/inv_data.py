GRID_SIZE_X = 100
GRID_SIZE_Y = 100

bess_inv1_json = {
    "type": "inverter",
    "id": "bess_inv1",
    "data": {
        "name": "BESS Inverter 1",
        "from": "bess_ac_bus:d0",
        "to": "bess_dc_bus:u0",
        "point": [
            [ "bess_ac_bus:d0:x", 675],
            "split",
            ["bess_dc_bus:u0:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d0",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u0",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv2_json = {
    "type": "inverter",
    "id": "bess_inv2",
    "data": {
        "name": "BESS Inverter 2",
        "from": "bess_ac_bus:d1",
        "to": "bess_dc_bus:u1",
        "point": [
            [ "bess_ac_bus:d1:x", 675],
            "split",
            ["bess_dc_bus:u1:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d1",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u1",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv3_json = {
    "type": "inverter",
    "id": "bess_inv3",
    "data": {
        "name": "BESS Inverter 3",
        "from": "bess_ac_bus:d2",
        "to": "bess_dc_bus:u2",
        "point": [
            [ "bess_ac_bus:d2:x", 675],
            "split",
            ["bess_dc_bus:u2:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d2",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u2",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv4_json = {
    "type": "inverter",
    "id": "bess_inv4",
    "data": {
        "name": "BESS Inverter 4",
        "from": "bess_ac_bus:d3",
        "to": "bess_dc_bus:u3",
        "point": [
            [ "bess_ac_bus:d3:x", 675],
            "split",
            ["bess_dc_bus:u3:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d3",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u3",
                    "direction": "up_right"
                }
            }
        ]
    }
}

bess_inv5_json = {
    "type": "inverter",
    "id": "bess_inv5",
    "data": {
        "name": "BESS Inverter 5",
        "from": "bess_ac_bus:d4",
        "to": "bess_dc_bus:u4",
        "point": [
            [ "bess_ac_bus:d4:x", 675],
            "split",
            ["bess_dc_bus:u4:x", 775]
        ],
        "color": "red",
        "linescale": 1.0,
        "cubicle1": [
            {
                "type": "switch",
                "id": "bess_inv_ac_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_ac_bus:d4",
                    "direction": "up_left"
                }
            }
        ],
        "cubicle2": [
            {
                "type": "switch",
                "id": "bess_inv_dc_swt1",
                "data": {
                    "color": "red",
                    "scale": 2.0,
                    "offset": [0, 20],
                    "attach": "bess_dc_bus:u4",
                    "direction": "up_right"
                }
            }
        ]
    }
}
