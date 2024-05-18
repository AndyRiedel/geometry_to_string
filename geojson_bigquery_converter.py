# -*- coding: utf-8 -*-

import json

in_filepath = r'Documents\SD8\VOTINGPRECINCT_PL.geojson'
out_filepath = r'Documents\SD8\bq_precincts.json'
with open(in_filepath, 'r') as f:
    with open(out_filepath, 'w') as wr:
        data = json.load(f)
        
        features = data['features']
        schema = None
        for obj in features:
            
            props = obj['properties']  # a dictionary
           # coords = obj['geometry']['coordinates']
           # new_coords = []
           # for i in coords[0]:
           #     new_coords.append([i[1], i[0]])
           # obj['geometry']['coordinates'] = [new_coords]
            props['geometry'] = json.dumps(obj['geometry'])  # make the geometry a string
            json.dump(props, fp=wr)
            print('', file=wr) # newline
            if schema is None:
                schema = []
                for key, value in props.items():
                    if key == 'geometry':
                        schema.append('geometry:GEOGRAPHY')
                    elif isinstance(value, str):
                        schema.append(key)
                    else:
                        schema.append('{}:{}'.format(key,
                           'int64' if isinstance(value, int) else 'float64'))
                schema = ','.join(schema)
        print('Schema: ', schema)