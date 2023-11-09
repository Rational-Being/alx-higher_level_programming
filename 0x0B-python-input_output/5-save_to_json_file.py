#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

import json

def save_to_json_file(my_obj, filename):
    """
    saves to a jason file
    
    """
    with open(filename, mode='w', encoding='utf-8' as file:
        return file.write(json.dumps(my_obj))
