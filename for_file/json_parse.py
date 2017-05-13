import json


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
    d = parse_file('for_file/test.json')
    print d
    write_file('for_file/tt1.json', d)
