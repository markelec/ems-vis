from umphang_data.bus_data import (
    umphang_bus_json, maesot_bus_json, bess_ac_bus_json, bess_dc_bus_json,
    diesel_bus_json, terminal1_bus_json, terminal2_bus_json,
    terminal3_bus_json, terminal4_bus_json, terminal5_bus_json,
    terminal6_bus_json, terminal7_bus_json, terminal8_bus_json,
    terminal9_bus_json, terminal10_bus_json, terminal11_bus_json,
    terminal12_bus_json, terminal13_bus_json
)

from umphang_data.line_data import (
    mae_sot_line_json, recloser1_line_json, 
    section1_line_json, section2_line_json, recloser2_line_json,
    section3_line_json, section4_line_json, section5_line_json,
    recloser3_line_json, section6_line_json, maesot_feeder_line_json
)
from umphang_data.tr_data import bess_tr_json, gen_tr_json
from umphang_data.inv_data import (
    bess_inv1_json, bess_inv2_json, bess_inv3_json, bess_inv4_json, bess_inv5_json
)
from umphang_data.bess_data import (
    bess1_json, bess2_json, bess3_json
)

from umphang_data.load_data import load1_json, load2_json, load3_json, load4_json

from umphang_data.gen_data import gen1_json, gen2_json, gen3_json, gen4_json, gen5_json

from umphang_data.avr_data import avr1_json, avr2_json, avr3_json

from umphang_data.text_data import (text_main_bus, text_maesot_bus, 
    text_bess_ac_bus, text_diesel_bus, 
    text_load1_bus, text_load2_bus, text_load3_bus, text_load4_bus,
    text_battery1_bus, text_battery2_bus, text_battery3_bus,
    text_diesel1_bus, text_diesel2_bus, text_diesel3_bus, text_diesel4_bus, text_diesel5_bus,
    text_avr1_bus, text_avr2_bus,
    result_main_bus, result_maesot_bus, result_bess_ac_bus, result_diesel_bus
 )
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
        mae_sot_line_json, recloser1_line_json,
        section1_line_json, section2_line_json, recloser2_line_json,
        section3_line_json, section4_line_json, section5_line_json,
        recloser3_line_json, section6_line_json, maesot_feeder_line_json
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
        bess1_json, bess2_json, bess3_json, load1_json, load2_json, load3_json, load4_json,
        gen1_json, gen2_json, gen3_json, gen4_json, gen5_json
    ],
    "two_terminal_elements": [
        bess_tr_json, gen_tr_json,
        bess_inv1_json, bess_inv2_json, bess_inv3_json, bess_inv4_json, bess_inv5_json,
        avr1_json, avr2_json, avr3_json
    ],
    "texts": [
       text_main_bus, text_maesot_bus, text_bess_ac_bus, text_diesel_bus,
       text_load1_bus, text_load2_bus, text_load3_bus, text_load4_bus,
       text_battery1_bus, text_battery2_bus, text_battery3_bus,
       text_diesel1_bus, text_diesel2_bus, text_diesel3_bus, text_diesel4_bus, text_diesel5_bus,
       text_avr1_bus, text_avr2_bus,
       result_main_bus, result_maesot_bus, result_bess_ac_bus, result_diesel_bus
    ]
}