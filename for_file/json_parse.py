import json

GOOD_FILE = 'base/dll_3529.json'
BAD_FILE = 'base/exe_839.json'


def get_all_data():
    # good_data = parse_file(GOOD_FILE)
    good_data = parse_file(GOOD_FILE)[:250]
    # bad_data = parse_file(BAD_FILE)
    bad_data = parse_file(BAD_FILE)[:250]
    return good_data, bad_data


def parse_file(file_name):
    with open(file_name) as input_file:
        result = json.load(input_file)
        input_file.close()
        return result


def write_file(file_name, data):
    with open(file_name, 'w') as output_file:
        json.dump(data, output_file)
        output_file.close()


if __name__ == '__main__':
    d = parse_file('dll_4368.json')

    result = list(i for i in d if len(i) == 224)

    print len(result)
    # print result

    write_file('dll_3529.json', result)
    pass
