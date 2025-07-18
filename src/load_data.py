# This file helps us load the JSON file into a table

import json
import pandas as pd  # This is the pandas library

def load_transactions(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)  # Read the JSON file
    df = pd.json_normalize(data)  # Make it into a nice table
    return df
