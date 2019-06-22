import json, os
'''
Written by the team at CSB2019
contains function which takes text and appends it to a file
'''

def file_was_created(filename):
    '''
    Checks if a file was created.
    '''
    return os.path.exists(filename)

def file_to_text(filename):
    '''
    Returns text from a file named `filename`.
    '''
    with open(filename, 'r') as text:
        return text.read()

def text_to_file(text, filename):
    '''
    Takes text and appends it to a file\n
    ARGS:\n
    `text: The text to append to file`\n 
    `filename: The name of the file to append text to`
    '''
    with open(filename, 'a+') as file:
        file.write(text + '\n')

# JSON and files

def file_to_dict(filename):
    '''
    uses `file_to_text` to load json as string
    then converts string to a dictinary
    '''
#     return file_to_text(filename)
    with open(filename) as file:
        return json.loads(file.read())

def dict_to_file(dict_obj, filename):
    '''
    Takes a `dict` of type `dict` and a `filename` of type `string`,
    converts dictionary to json-string then,
    uses `text_to_file` to write json-string to file
    '''
    # 1. Convert dict to string
    # 2. Store dict-string in file (That ends in .JSON)
    text_to_file(json.dumps(dict_obj), filename)

def dict_to_json(dict_obj, filename):
    with open(filename, 'w') as temp:
        json.dump(dict_obj, temp)


# output = dict_to_json({'settings': {'test': True, 'fake': False}}, 'file.json')
# print(output)