'''
Flatten a nested dictionary

initial_dictionary {‘geeks’: {‘Geeks’: {‘for’: 7}}, ‘Geeks’: {‘for’: {‘geeks’: 4, ‘for’: 1}}, ‘for’: {‘geeks’: {‘Geeks’: 3}}}
final_dictionary {‘Geeks_for_for’: 1, ‘geeks_Geeks_for’: 7, ‘for_geeks_Geeks’: 3, ‘Geeks_for_geeks’: 4}
'''