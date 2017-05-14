import json

GOOD_FILE = 'base/dll_500.json'
BAD_FILE = 'base/dll_500.json'


def get_all_data():
    # good_data = parse_file(GOOD_FILE)[:250]
    good_data = parse_file(GOOD_FILE)[:250]
    bad_data = parse_file(GOOD_FILE)[250:]
    # bad_data = parse_file(BAD_FILE)
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
    d = parse_file('base/dll_4368.json')

    result = list(i for i in d if len(i) == 224)[:500]

    print len(result)
    print result

    write_file('base/dll_500.json', result)
    pass
