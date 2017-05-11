import json


def parse_file(file_name):
    return json.load(open(file_name))


def write_file(file_name, data):
    json.dump(data, open(file_name, 'w'))


if __name__ == '__main__':
    d = parse_file('test.json')
    print d
    write_file('tt1.json', d)
