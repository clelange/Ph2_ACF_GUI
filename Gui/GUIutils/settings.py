# November 19 2021:  Edited by Matt Joyce.  Added information for Purdue database to DBNames and DBServerIP

import os
from collections import defaultdict
#from Gui.siteSettings import *
#import InnerTrackerTests.TestSequences as TestSequences

# List of expert users
ExpertUserList = [
    "mjoyce",
    "cmsfpix_phase2_user",
    "localexpert",
]


"""
if os.path.isfile(os.environ.get('GUI_dir')+"/fc7_ip_address.txt"):
	IPfile = open(os.environ.get('GUI_dir')+"/fc7_ip_address.txt")
	iplines = IPfile.readlines()
	for line in iplines:
		if line.startswith("#"):
			continue
		firmwareName = line.strip().split()[0]
		ip_address = line.strip().split()[1]
		if len(ip_address.split('.')) != 4:
			raise ValueError('{} is not valid ip address'.format(ip_address))
		FirmwareList[firmwareName] = ip_address

else:

	FirmwareList =  {
	'fc7.board.1'			 :  '192.168.1.80',
	'fc7.board.2'			 :  '127.0.0.1',#'192.168.1.81',
	}

"""
"""
DBServerIP = {
	'Central-remote'		 :  '0.0.0.0',
	'local'					 :  '127.0.0.1',
	'OSU-remote'			 :  '128.146.38.1',
	'Purdue-remote'			 :  'cmsfpixdb.physics.purdue.edu',
}


# Note: First element of list will be shown as default value
DBNames = {
	'All'					 :  ['phase2pixel_test', 'DBName2', 'DBName3'],
	'Central-remote'		 :  ['phase2pixel_test', 'DBName2', 'DBName3'],
	'local'					 :  ['SampleDB','phase2pixel_test'],
	'OSU-remote'			 :  ['SampleDB','phase2pixel_test'],
	'Purdue-remote'			 :  ['cmsfpix_phase2'],
}
"""

# Set the IT_uTDC_firmware for test
FPGAConfigList = {
    "fc7.board.1": "IT-uDTC_L12-KSU-3xQUAD_L8-KSU2xQUAD_x1G28",
    "fc7.board.2": "IT-uDTC_L12-KSU-3xQUAD_L8-KSU2xQUAD_x1G28",
}

ModuleType = {
    1: "SCC",
    2: "TFPX RD53A Quad",
    3: "TEPX RD53A Quad",
    4: "TBPX RD53A Quad",
    5: "CROC SCC",
    6: "TFPX CROC 1x2",
    7: "TEPX CROC 1x2",
    8: "TBPX CROC 1x2",
    9: "TFPX CROC Quad",
    10: "TEPX CROC Quad",
    11: "TBPX CROC Quad",
}

firmware_image = {
    "SCC": {
        "Dev": "SCC_ELE_RD53A_v4-9.bit",
        "v4-13": "SCC_ELE_RD53A_v4-6.bit",
        "v4-14": "SCC_ELE_RD53A_v4-6.bit",
    },
    "TFPX RD53A Quad": {
        "Dev": "QUAD_ELE_RD53A_v4-9.bit",
        "v4-13": "QUAD_ELE_RD53A_v4-6.bit",
        "v4-14": "QUAD_ELE_RD53A_v4-6.bit",
    },
    "TEPX RD53A Quad": {
        "Dev": "QUAD_ELE_RD53A_v4-9.bit",
        "v4-13": "QUAD_ELE_RD53A_v4-6.bit",
        "v4-14": "QUAD_ELE_RD53A_v4-6.bit",
    },
    "TBPX RD53A Quad": {
        "Dev": "QUAD_ELE_RD53A_v4-9.bit",
        "v4-13": "QUAD_ELE_RD53A_v4-6.bit",
        "v4-14": "QUAD_ELE_RD53A_v4-6.bit",
    },
    "CROC SCC": {
        "Dev": "SCC_ELE_CROC_v4-9.bit",
        "v4-13": "SCC_ELE_CROC_v4-6.bit",
        "v4-14": "SCC_ELE_CROC_v4-6.bit",
    },
    "TFPX CROC 1x2": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
    "TFPX CROC Quad": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
    "TEPX CROC 1x2": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
    "TEPX CROC Quad": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
    "TBPX CROC 1x2": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
    "TBPX CROC Quad": {
        "Dev": "QUAD_ELE_CROC_v4-9.bit",
        "v4-13": "QUAD_ELE_CROC_v4-6.bit",
        "v4-14": "QUAD_ELE_CROC_v4-6.bit",
    },
}

ModuleLaneMap = {
    "TFPX RD53A Quad": {"0": "4", "1": "2", "2": "7", "3": "5"},
    "TEPX RD53A Quad": {"0": "0", "1": "1", "2": "2", "3": "3"},
    "TBPX RD53A Quad": {"0": "4", "1": "5", "2": "6", "3": "7"},
    "SCC": {"0": "0"},
    "CROC SCC": {"0": "15"},
    "TFPX CROC 1x2": {"0": "12", "2": "13"},
    "TEPX CROC 1x2": {"0": "0", "2": "2"},
    "TBPX CROC 1x2": {"0": "0", "2": "2"},
    "TFPX CROC Quad": {"2": "12", "1": "13", "0": "14", "3": "15"},
    "TEPX CROC Quad": {"0": "0", "1": "1", "2": "2", "3": "3"},
    "TBPX CROC Quad": {"0": "0", "1": "1", "2": "2", "3": "3"},
}

ChipMap = {
    "TFPX CROC 1x2": {
        'VDDD_B': 	'13',
        'VDDA_B': 	'13',
        'VDDA_A': 	'12',
        'VDDD_A': 	'12',
        'VMUX_B': 	'13',
        'IMUX_B': 	'13',
        'VMUX_A': 	'12',
        'IMUX_A': 	'12',
        'GND_A':	'12'},
    }

BoxSize = {
    "SCC": 1,
    "TFPX RD53A Quad": 4,
    "TEPX RD53A Quad": 4,
    "TBPX RD53A Quad": 4,
    "CROC SCC": 1,
    "TFPX CROC 1x2": 2,
    "TEPX CROC 1x2": 2,
    "TBPX CROC 1x2": 2,
    "TFPX CROC Quad": 4,
    "TEPX CROC Quad": 4,
    "TBPX CROC Quad": 4,
}

optimizationTestMap = {
    'thradj':[
        'DAC_GDAC_M_LIN',
        'DAC_GDAC_L_LIN',
        'DAC_GDAC_R_LIN',
        'Vthreshold_LIN',
    ],
    'thrmin':[
        'DAC_GDAC_M_LIN'
        'DAC_GDAC_L_LIN'
        'DAC_GDAC_R_LIN'
        'Vthreshold_LIN'
    ],
    'threq':[
        'VCAL_HIGH',
    ],
    'gainopt':[
        'DAC_KRUM_CURR_LIN',
        'KRUM_CURR_LIN',
    ],
    'injdelay':[
        'TriggerConfig',
        'LATENCY_CONFIG',
        'CAL_EDGE_FINE_DELAY',
    ],
    'gendacdac':[
        'VCAL_HIGH',
        'CAL_EDGE_FINE_DELAY',
    ],
}

# Reserved for updated value for XML configuration
updatedXMLValues = defaultdict(dict)

updatedGlobalValue = defaultdict(lambda: None)
stepWiseGlobalValue = defaultdict(dict)  # key : index
