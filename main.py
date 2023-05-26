from scr.utils import load_json_file, processing_for_output

file = load_json_file('/home/den/project/kurs3/operations.json')

# file = load_json_file('/home/den/project/kurs3/tests/test_file.json')
# print(file)

rezult = processing_for_output(file)


# print(rezult)