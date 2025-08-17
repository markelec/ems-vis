GRID_SIZE_X = 100
GRID_SIZE_Y = 100

text_main_bus = {
    "type": "text",
    "id": "main_bus_label",
    "data": {
        "text": "22 KV UMPHANG",
        "position": [950, 390],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "center",
        "offset": [0, 0],
        "rotation": 0
    }
}

text_maesot_bus = {
    "type": "text",
    "id": "maesot_bus_label",
    "data": {
        "text": "22 KV MAESOT",
        "position": [17*GRID_SIZE_X, "maesot_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [-10, 0],
        "rotation": 0
    }
}

text_bess_ac_bus = {
    "type": "text",
    "id": "bess_ac_bus_label",
    "data": {
        "text": "22 KV BESS",
        "position": [0.5*GRID_SIZE_X, "bess_ac_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "bottommid",  # Bottom middle of text aligns with the position
        "offset": [0, -10],
        "rotation": 0
    }
}

text_diesel_bus = {
    "type": "text",
    "id": "diesel_bus_label",
    "data": {
        "text": "22 KV DIESEL GEN.",
        "position": [12*GRID_SIZE_X, "diesel_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, -10],
        "rotation": 0
    }
}

text_load1_bus = {
    "type": "text",
    "id": "load1_bus_label",
    "data": {
        "text": "PALATHA",
        "position": ["umphang_bus:d7:x", 640],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_load2_bus = {
    "type": "text",
    "id": "load2_bus_label",
    "data": {
        "text": "KIO HANG",
        "position": ["umphang_bus:d8:x", 640],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_load3_bus = {
    "type": "text",
    "id": "load3_bus_label",
    "data": {
        "text": "NONG LUANG-MAE CHAN",
        "position": ["umphang_bus:d9:x", 640],
        "font": {
            "family": "Helvetica",
            "size": 8,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_load4_bus = {
    "type": "text",
    "id": "load4_bus_label",
    "data": {
        "text": "YAMO",
        "position": ["umphang_bus:d10:x", 640],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_battery1_bus = {
    "type": "text",
    "id": "battery1_bus_label",
    "data": {
        "text": "BATTERY #1",
        "position": ["bess_dc_bus:d1:x", 1020],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "topmid",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": 0
    }
}

text_battery2_bus = {
    "type": "text",
    "id": "battery2_bus_label",
    "data": {
        "text": "BATTERY #2",
        "position": ["bess_dc_bus:d2:x", 1020],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "topmid",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": 0
    }
}

text_battery3_bus = {
    "type": "text",
    "id": "battery3_bus_label",
    "data": {
        "text": "BATTERY #3",
        "position": ["bess_dc_bus:d3:x", 1020],
        "font": {
            "family": "Helvetica",
            "size": 12,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "topmid",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": 0
    }
}

text_diesel1_bus = {
    "type": "text",
    "id": "diesel1_bus_label",
    "data": {
        "text": "DIESEL #1",
        "position": ["diesel_bus:d0:x", 1000],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_diesel2_bus = {
    "type": "text",
    "id": "diesel2_bus_label",
    "data": {
        "text": "DIESEL #2",
        "position": ["diesel_bus:d1:x", 1000],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_diesel3_bus = {
    "type": "text",
    "id": "diesel3_bus_label",
    "data": {
        "text": "DIESEL #3",
        "position": ["diesel_bus:d2:x", 1000],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_diesel4_bus = {
    "type": "text",
    "id": "diesel4_bus_label",
    "data": {
        "text": "DIESEL #4",
        "position": ["diesel_bus:d3:x", 1000],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_diesel5_bus = {
    "type": "text",
    "id": "diesel5_bus_label",
    "data": {
        "text": "DIESEL #5",
        "position": ["diesel_bus:d4:x", 1000],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "midright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": -90
    }
}

text_avr1_bus = {
    "type": "text",
    "id": "avr1_bus_label",
    "data": {
        "text": "WA BEY THA",
        "position": ["terminal2_bus:u0:x", "terminal2_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "bottommid",  # Bottom middle of text aligns with the position
        "offset": [0, -30],
        "rotation": 0
    }
}

text_avr2_bus = {
    "type": "text",
    "id": "avr2_bus_label",
    "data": {
        "text": "UMPIEM",
        "position": ["terminal7_bus:u0:x", "terminal7_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 14,
            "bold": True,
            "italic": False
        },
        "color": "white",
        "anchor": "bottommid",  # Bottom middle of text aligns with the position
        "offset": [0, -30],
        "rotation": 0
    }
}

result_main_bus = {
    "type": "text",
    "id": "main_bus_result",
    "data": {
        "text": "1.025 p.u.\n22.55 kV",
        "position": [3*GRID_SIZE_X, 350],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "lightgreen",
        "anchor": "topright",
        "offset": [0, 0],
        "rotation": 0
    }
}

result_maesot_bus = {
    "type": "text",
    "id": "maesot_bus_result",
    "data": {
        "text": "1.025 p.u.\n22.55 kV",
        "position": [19*GRID_SIZE_X, GRID_SIZE_Y],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "lightgreen",
        "anchor": "bottomleft",
        "offset": [0, 0],
        "rotation": 0
    }
}

result_bess_ac_bus = {
    "type": "text",
    "id": "bess_ac_bus_result",
    "data": {
        "text": "1.025 p.u.\n22.55 kV",
        "position": [0.5*GRID_SIZE_X, "bess_ac_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "lightgreen",
        "anchor": "topright",  # Bottom middle of text aligns with the position
        "offset": [0, 0],
        "rotation": 0
    }
}

result_diesel_bus = {
    "type": "text",
    "id": "diesel_bus_result",
    "data": {
        "text": "1.025 p.u.\n22.55 kV",
        "position": [12*GRID_SIZE_X, "diesel_bus:u0:y"],
        "font": {
            "family": "Helvetica",
            "size": 16,
            "bold": True,
            "italic": False
        },
        "color": "lightgreen",
        "anchor": "topright",  # Bottom middle of text aligns with the position
        "offset": [0, 10],
        "rotation": 0
    }
}