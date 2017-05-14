#!/usr/local/bin/python2
# -*- coding: utf8 -*-

import pefile
import os
from json_parse import *

STEP_FLAG = 20
STEP_FILES = 200
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


def parse_dir(dir_path):
    result = []
    for d, dirs, files in os.walk(dir_path):
        for f in files:
            result.append(str(d + f))
    return result


def steps(index, result):
    if index % STEP_FLAG == 0:
        print index
    if index % STEP_FILES == 0:
        write_file('base/exe_files_{}.json'.format(index), result)
        return []
    else:
        return result

if __name__ == '__main__':
    file_path = 'ChromeSetup.exe'
    file_path = 'd3dx9_43.dll'
    file_path = 'for_file/BRPTUNI2.DLL'

    # res_lst = parse_file(file_path)
    # print len(res_lst)
    # print res_lst

    base = parse_dir('/home/hodzi/diplom/dll/')
    index = 0
    result = []
    for file_base in base:
        try:
            print file_base
            result.append(parse_file(file_base))
            index += 1
            result = steps(index, result)
        except:
            print 'ERROR', file_base


