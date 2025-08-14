from umphang_data.bus_data import (
    umphang_bus_json, maesot_bus_json, bess_ac_bus_json, bess_dc_bus_json,
    diesel_bus_json, terminal1_bus_json, terminal2_bus_json,
    terminal3_bus_json, terminal4_bus_json, terminal5_bus_json,
    terminal6_bus_json, terminal7_bus_json, terminal8_bus_json,
    terminal9_bus_json, terminal10_bus_json, terminal11_bus_json,
    terminal12_bus_json, terminal13_bus_json,
)

from umphang_data.line_data import mae_sot_line_json
from umphang_data.tr_data import bess_tr_json
from umphang_data.inv_data import (
    bess_inv1_json, bess_inv2_json, bess_inv3_json, bess_inv4_json, bess_inv5_json
)
from umphang_data.bess_data import (
    bess1_json, bess2_json, bess3_json
)

from umphang_data.load_data import load1_json, load2_json, load3_json, load4_json

# Complete diagram dictionary
diagram_dict = {
    "buses": [
        umphang_bus_json, maesot_bus_json, bess_ac_bus_json, bess_dc_bus_json,
        diesel_bus_json, terminal1_bus_json, terminal2_bus_json,
        terminal3_bus_json, terminal4_bus_json, terminal5_bus_json,
        terminal6_bus_json, terminal7_bus_json, terminal8_bus_json,
        terminal9_bus_json, terminal10_bus_json, terminal11_bus_json,
        terminal12_bus_json, terminal13_bus_json,
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
        bess1_json, bess2_json, bess3_json, load1_json, load2_json, load3_json, load4_json
    ],
    "two_terminal_elements": [
        bess_tr_json, bess_inv1_json, bess_inv2_json, bess_inv3_json, bess_inv4_json, bess_inv5_json
    ],
    "texts": [
       
    ]
}