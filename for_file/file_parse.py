import pefile

NOS = 'NumberOfSections'


def parse_dict(dict_for_parse):
    result = list()
    for temp1 in list(dict_for_parse[i] for i in dict_for_parse.keys() if type(dict_for_parse[i]) == dict):
        result += (list(temp1[j] if type(temp1[j]) == int else 0 for j in temp1.keys()))
    return result
    # for i in dict_for_parse.keys():
    #     temp1 = dict_for_parse[i]
    #     print temp1
    #     if type(temp1) == dict:
    #         for j in temp1.keys():
    #             if type(temp1[j]) == int:
    #                 result.append(temp1[j])
    #             else:
    #                 result.append(0)
    #
    # for j in dict_for_parse[i].keys():
    #     print dict_for_parse[i][j]


def parse_file(file_path):
    result = list()
    pe = pefile.PE(file_path)
    result += parse_dict(pe.FILE_HEADER.dump_dict())
    result += parse_dict(pe.DOS_HEADER.dump_dict())
    result += parse_dict(pe.OPTIONAL_HEADER.dump_dict())
    result.append(pe.PE_TYPE)
    result.append(pe.fileno)
    result.append(int(pe.is_exe()))
    result.append(int(pe.is_dll()))
    result.append(int(pe.is_driver()))
    result += parse_dict(pe.NT_HEADERS.dump_dict())
    result += parse_dict(pe.VS_FIXEDFILEINFO.dump_dict())
    result += parse_dict(pe.VS_VERSIONINFO.dump_dict())
    return result


if __name__ == '__main__':
    file_path = 'ChromeSetup.exe'
    file_path = 'd3dx9_43.dll'
    res_lst = parse_file(file_path)
    print len(res_lst)
    print res_lst

