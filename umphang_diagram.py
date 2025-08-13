from umphang_diagram_data import (
    umphang_bus_json, maesot_bus_json, bess_ac_bus_json, bess_dc_bus_json,
    diesel_bus_json, terminal1_bus_json, terminal2_bus_json,
    terminal3_bus_json, terminal4_bus_json, terminal5_bus_json,
    terminal6_bus_json, terminal7_bus_json, terminal8_bus_json,
    terminal9_bus_json, terminal10_bus_json, terminal11_bus_json,
    terminal12_bus_json, terminal13_bus_json,
    mae_sot_line_json, bess_tr_json
)

# Complete diagram dictionary
diagram_dict = {
    "buses": [
        umphang_bus_json, maesot_bus_json, bess_ac_bus_json, bess_dc_bus_json,
        diesel_bus_json, terminal1_bus_json, terminal2_bus_json,
        terminal3_bus_json, terminal4_bus_json, terminal5_bus_json,
        terminal6_bus_json, terminal7_bus_json, terminal8_bus_json,
        terminal9_bus_json, terminal10_bus_json, terminal11_bus_json,
        terminal12_bus_json, terminal13_bus_json
    ],
    "lines": [
        mae_sot_line_json
    ],
    "loads": [
        
    ],
    "generators": [
       
    ],
    "transformers": [
        # Add transformer elements here if you have them
    ],
    "inverters": [
        
    ],
    "svg_elements": [
        
    ],
    "two_terminal_elements": [
        bess_tr_json
    ],
    "texts": [
       
    ]
}