import json

with open("yuck.json") as f:
    s_json = f.read()

try:
    o_json = json.loads(s_json)
    #f_json = json.dumps(o_json, indent=3, sort_keys=False)
    filtered_data = [obj for obj in o_json[1] if obj.get('EntityType') == 'PSD_EMI']

    # Assuming the JSON data is stored in a variable called 'json_data'

    # Create an empty list to store the values of "ENT_NAM"
    ent_nam_values = []

    # Iterate over each object in the JSON data
    for obj in filtered_data:
        # Check if "Properties" key exists in the object
        if 'Properties' in obj:
            properties = obj['Properties']
            # Iterate over each property in the "Properties" list
            for prop in properties:
                # Check if "ENT_NAM" key exists in the property
                if 'ENT_NAM' in prop:
                    value = prop['ENT_NAM']
                    # Check if the value is a list
                    if isinstance(value, list):
                        # Check if the list has at least two items
                        if len(value) >= 2:
                            # Append the second item from the list
                            ent_nam_values.append(value[1])
                    else:
                        # Append the value as is if it's not a list
                        ent_nam_values.append(value)

    # Print the list of "ENT_NAM" values
    print(ent_nam_values)

    #filtered_data = [obj for obj in o_json if obj.get('EntityType', '') == 'PSD_EMI']

    #print(o_json[:5])  # Print the first 5 objects in the list
    #print(o_json)
    #print(filtered_data)

    # Print the list of keys
    #print(keys_list)

    print(len(filtered_data))

except Exception as ex:
    print(repr(ex))

#print(len(f_json))
#print(len(filtered_data))

