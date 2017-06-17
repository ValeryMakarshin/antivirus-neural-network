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
    # for temp1 in list(dict_for_parse[i] for i in dict_for_parse.keys() if type(dict_for_parse[i]) == dict):
    #     result += (list(temp1[j] if type(temp1[j]) == int else 0 for j in temp1.keys()))
    # return result
    for i in dict_for_parse.keys():
        temp1 = dict_for_parse[i]
        print temp1
        if type(temp1) == dict:
            for j in temp1.keys():
                if type(temp1[j]) == int:
                    result.append(temp1[j])
                else:
                    result.append(0)
    return result



# функция для вытаскивания атрибутов
def parse_file(file_path):
    result_atr = list()
    pe = pefile.PE(file_path)
    result_atr += parse_dict(pe.FILE_HEADER.dump_dict())
    result_atr += parse_dict(pe.DOS_HEADER.dump_dict())
    result_atr += parse_dict(pe.OPTIONAL_HEADER.dump_dict())
    result_atr.append(pe.PE_TYPE)
    result_atr.append(pe.fileno)
    result_atr.append(int(pe.is_exe()))
    result_atr.append(int(pe.is_dll()))
    result_atr.append(int(pe.is_driver()))
    result_atr += parse_dict(pe.NT_HEADERS.dump_dict())
    result_atr += parse_dict(pe.VS_FIXEDFILEINFO.dump_dict())
    result_atr += parse_dict(pe.VS_VERSIONINFO.dump_dict())
    return result_atr

# Пример выходных данных
# [238, 4, 2, 240, 0, 4, 244, 0, 8, 248, 0, 12, 236, 332, 0, 254, 258, 18, 252, 224, 16, 2, 144, 2, 6, 0, 6, 26, 0,
# 26, 10, 0, 10, 18, 0, 18, 8, 4, 8, 4, 3, 4, 22, 0, 22, 12, 65535, 12, 24, 64, 24, 36, 0, 36, 60, 232, 60, 14, 0,
# 14, 0, 23117, 0, 38, 0, 38, 40, 0, 40, 28, 0, 28, 16, 184, 16, 20, 0, 20, 326, 33088, 70, 276, 4096, 20, 258, 9, 2,
#  298, 1, 42, 259, 0, 3, 304, 6, 48, 296, 6, 40, 332, 8192, 76, 268, 0, 12, 348, 16, 92, 336, 1048576, 80, 344, 0,
# 88, 340, 4096, 84, 328, 262144, 72, 316, 1024, 60, 324, 3, 68, 256, 267, 0, 302, 1, 46, 300, 6, 44, 292, 512, 36,
# 280, 16384, 24, 272, 9554, 16, 288, 4096, 32, 260, 8704, 4, 284, 16777216, 28, 264, 4096, 8, 312, 28672, 56, 306,
# 1, 50, 320, 51858, 64, 308, 0, 52, 267, 3, 1, 0, 0, 232, 17744, 0, 0, 63, 24, 0, 1, 36, 0, 393217, 8, 0, 498089985,
#  12, 0, 4277077181, 0, 0, 0, 40, 0, 0, 28, 0, 0, 48, 0, 498089985, 20, 0, 262148, 32, 0, 393217, 16, 0, 0, 44, 0,
# 65536, 4, 11162, 52, 2, 11160, 912, 0, 11164, 0, 4]

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


# example
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


