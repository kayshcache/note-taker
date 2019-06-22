import os, json
from textandfile_handler import *

def test_file_was_created():
    test_filename = 'test.file'
    # with open(test_filename, 'w') as new_file:
    #     new_file.write('Empty file')
    text_to_file('Empty file', test_filename)

    assert file_was_created('test.file') == True
    os.remove(test_filename)

def test_file_to_text():
    TEST_FILE_NAME = 'tester.txt'
    TEST_FILE_CONTENT = 'Testing, testing 1 2 3' 
    with open(TEST_FILE_NAME, 'w+') as temp_file:
        temp_file.write(TEST_FILE_CONTENT)

    assert file_to_text(TEST_FILE_NAME) == TEST_FILE_CONTENT
    os.remove(TEST_FILE_NAME)

def test_file_to_dict():
    TEST_JSON_FILENAME = 'tester.json'
    TEST_JSON = "{'settings': {'test': True, 'fake': False}}"

    with open(TEST_JSON_FILENAME, 'w') as temp:
        json.dump(TEST_JSON, temp)

    assert file_to_dict(TEST_JSON_FILENAME) == TEST_JSON
    os.remove(TEST_JSON_FILENAME)

def test_dict_to_file():
    TEST_FILENAME = 'tester.json'
    TEST_DICT = "{'settings': {'test': True, 'fake': False}}" 
    dict_to_file(TEST_DICT, TEST_FILENAME)
    assert file_was_created(TEST_FILENAME) == True
    assert file_to_dict(TEST_FILENAME) == TEST_DICT
    os.remove(TEST_FILENAME)

def test_dict_to_json():
    FILENAME = 'tester.json'
    TEST_JSON = "{'settings': {'test': True, 'fake': False}}"

    dict_to_json(TEST_JSON, FILENAME)
    with open(FILENAME, 'r') as temp_json:
        TEST_DICTIONARY = json.load(temp_json)
    
    assert TEST_DICTIONARY == TEST_JSON
    os.remove(FILENAME)