names = {'name1':'Claus',
        'name2':'Santa',
        'name3':'James',
        'name4':'Michal',
        'name5':'bob',
        }
def dicter(dictionary):
    keys = list(dictionary.keys())
    dictionary[keys[0]], dictionary[keys[-1]] = dictionary[keys[-1]], dictionary[keys[0]]
    del dictionary[keys[1]]
    dictionary['new key'] = 'new value'
    return dictionary
print (dicter(names))