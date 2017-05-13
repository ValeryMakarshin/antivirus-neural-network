#!/usr/local/bin/python2
# -*- coding: utf8 -*-
from __future__ import print_function

import pefile


def find_entry_point_section(pe, eop_rva):
    for section in pe.sections:
        if section.contains_rva(eop_rva):
            return section

    return None


def main(file_path):
    print("Opening {}".format(file_path))

    try:
        pe = pefile.PE(file_path, fast_load=True)
        # AddressOfEntryPoint if guaranteed to be the first byte executed.
        eop = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        code_section = find_entry_point_section(pe, eop)
        if not code_section:
            return

        print("[+] Code section found at offset: "
              "{:#x} [size: {:#x}]".format(code_section.PointerToRawData,
                                           code_section.SizeOfRawData))

        # get first 10 bytes at entry point and dump them
        code_at_oep = code_section.get_data(eop, 10)
        print("[*] Code at EOP:\n{}".
              format(" ".join("{:02x}".format(ord(c)) for c in code_at_oep)))

    except pefile.PEFormatError as pe_err:
        print("[-] error while parsing file {}:\n\t{}".format(file_path, pe_err))


if __name__ == '__main__':
    file_path = 'for_file/ChromeSetup.exe'
    file_path = 'for_file/chkntfs.exe.mui'
    # main(file_path)
    pe = pefile.PE(file_path)
    print(pe.FILE_HEADER.dump_dict())
    print(pe.DOS_HEADER.dump_dict())
    print(pe.OPTIONAL_HEADER.dump_dict())
    print(pe.PE_TYPE)
    print(pe.RICH_HEADER)
    print(pe.fileno)
    print(pe.is_exe())
    print(pe.is_dll())
    print(pe.is_driver())
    # print(pe.merge_modified_section_data())
    print(pe.NT_HEADERS.dump_dict())
    print(pe.VS_FIXEDFILEINFO.dump_dict())
    print(pe.VS_VERSIONINFO.dump_dict())
    print(pe.show_warnings())
    print(pe.verify_checksum())
    print(pe.parse_rich_header())
    # print(pe.print_info())
    print(pe.sections)



    # print(pe.get_resources_strings())

