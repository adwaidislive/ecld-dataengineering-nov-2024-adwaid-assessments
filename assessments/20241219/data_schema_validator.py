import json
import pandas as pd

schema = json.load(open("sample_schema.json"))



def column_details(schema):
    t = len(schema['tables']) # No of tables in the schema
    table_name = []
    columns = []
    for i in range(t):
        table_name.append(schema['tables'][i]['name'])
        n = len(schema['tables'][i]['columns']) # No of columns in the table

        print(f'{schema['tables'][i]['name']} table and their column specifications {schema['tables'][i]['columns']}') # mapping of table names to their column specifications
        for j in range(n):
            columns.insert(i,(schema['tables'][i]['columns'][j]['name']))

    return f'{table_name} and {columns}'


def filter_column(columns):
    return list(filter(lambda x: x, columns))



def validation(schema,data,column_details):

    val_errors = pd.DataFrame({'Error_severity':[],'Table_Name' : [], 'Column_Name': [] , 'Error_Type ' : []})
    t = len(schema['tables']) # No of tables in the schema
    l = len(schema['tables'][i]['columns']) # No of columns in the table


    # Iterating through tables
    for i in range(t):
        table_name = schema['tables'][i]['name']

        for i in range(l): # Iterating through columns
            if (column_details==(schema['tables'][table_no]['columns'][i]['name'])): # Checking the name of column which we want to validate
                n = i 
    
        # Iterating through datas to validate data
        for i in range(len(data)):

            # Checking Data Type
            if (type(data.iloc[i])!=schema['tables'][table_no]['columns'][n]['type']):
                new_row = pd.DataFrame({'Error_severity':['High'],
                                        'Table_Name' : [table_name], 
                                        'Column_Name': [schema['tables'][table_no]['columns'][i]['name']] , 
                                        'Error_Type ' : ['Data Type']})
                val_errors = pd.concat([val_errors,new_row], ignore_index=True)

            
            # Checking Values
            if ((data.iloc[i]) in schema['tables'][table_no]['columns'][n]['validation']):
                new_row = pd.DataFrame({'Error_severity':['Medium'],
                                        'Table_Name' : [table_name], 
                                        'Column_Name': [schema['tables'][table_no]['columns'][i]['name']] , 
                                        'Error_Type ' : ['Values']})
                val_errors = pd.concat([val_errors,new_row], ignore_index=True)
    

    return val_errors
            

def val_error_sort(val_errors, column_name='Error_severity'):
    return val_errors.sort_values(by=column_name, ascending=True)
                

