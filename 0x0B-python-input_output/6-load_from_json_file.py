#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

import json

def load_from_json_file(filename):
    """
    loads to a jason file
    
    """
    with open(filename, 'r') as file:
        return json.load(f)
