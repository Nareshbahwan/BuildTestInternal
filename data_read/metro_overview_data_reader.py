import pandas as pd
import json

def read_data():
    file_path = 'D:/Python Code/midas_360/code/Midas_code/data/metro_dashboard_complete.xlsx'
    
    excel_data = pd.ExcelFile(file_path)

    # Display sheet names to understand the structure of the file
    sheet_names = excel_data.sheet_names

    # Convert all sheets to JSON format
    data = {}
    data["header"]={
                "energy": None,
                "o_m": None,
                "train": 1,
                "station": None,
                "passenger": None,
                "Date_Range": "Last 7 days"
            }
    # Loop through each sheet and convert it to a dictionary
    for sheet in sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet)
        data[sheet] = df.to_dict(orient='records')


    out = json.dumps(data)
    data_2= json.loads(out)
    output ={"METRO_OVERVIEW":{}}
    output["METRO_OVERVIEW"]['data']=data_2
    output["METRO_OVERVIEW"]["messages"]=[]
    output["METRO_OVERVIEW"]["multiselect"]={}

    return output