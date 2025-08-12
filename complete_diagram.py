from diagram_data import (
    bus1_json, bus2_json, line_json, line_json2, 
    load_json, gen_json, trafo_json, inv_json, 
    bess_json, text_json1, text_json2
)

# Complete diagram dictionary
diagram_dict = {
    "buses": [
        bus1_json,
        bus2_json
    ],
    "lines": [
        line_json,
        line_json2
    ],
    "loads": [
        load_json
    ],
    "generators": [
        gen_json
    ],
    "transformers": [
        # Add transformer elements here if you have them
    ],
    "inverters": [
        inv_json
    ],
    "svg_elements": [
        bess_json
    ],
    "two_terminal_elements": [
        trafo_json
    ],
    "texts": [
        text_json1,
        text_json2
    ]
}