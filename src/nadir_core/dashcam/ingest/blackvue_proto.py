from __future__ import annotations
from typing import Dict, List
import re

def parse_vod_line_0(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='0'
    return out

BLACKVUE_ENDPOINTS_0 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_1(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='1'
    return out

BLACKVUE_ENDPOINTS_1 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_2(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='2'
    return out

BLACKVUE_ENDPOINTS_2 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_3(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='3'
    return out

BLACKVUE_ENDPOINTS_3 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_4(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='4'
    return out

BLACKVUE_ENDPOINTS_4 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_5(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='5'
    return out

BLACKVUE_ENDPOINTS_5 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_6(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='6'
    return out

BLACKVUE_ENDPOINTS_6 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_7(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='7'
    return out

BLACKVUE_ENDPOINTS_7 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_8(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='8'
    return out

BLACKVUE_ENDPOINTS_8 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_9(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='9'
    return out

BLACKVUE_ENDPOINTS_9 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_10(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='10'
    return out

BLACKVUE_ENDPOINTS_10 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_11(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='11'
    return out

BLACKVUE_ENDPOINTS_11 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_12(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='12'
    return out

BLACKVUE_ENDPOINTS_12 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_13(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='13'
    return out

BLACKVUE_ENDPOINTS_13 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_14(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='14'
    return out

BLACKVUE_ENDPOINTS_14 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_15(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='15'
    return out

BLACKVUE_ENDPOINTS_15 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_16(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='16'
    return out

BLACKVUE_ENDPOINTS_16 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_17(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='17'
    return out

BLACKVUE_ENDPOINTS_17 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_18(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='18'
    return out

BLACKVUE_ENDPOINTS_18 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_19(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='19'
    return out

BLACKVUE_ENDPOINTS_19 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_20(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='20'
    return out

BLACKVUE_ENDPOINTS_20 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_21(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='21'
    return out

BLACKVUE_ENDPOINTS_21 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_22(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='22'
    return out

BLACKVUE_ENDPOINTS_22 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_23(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='23'
    return out

BLACKVUE_ENDPOINTS_23 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_24(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='24'
    return out

BLACKVUE_ENDPOINTS_24 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_25(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='25'
    return out

BLACKVUE_ENDPOINTS_25 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_26(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='26'
    return out

BLACKVUE_ENDPOINTS_26 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_27(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='27'
    return out

BLACKVUE_ENDPOINTS_27 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_28(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='28'
    return out

BLACKVUE_ENDPOINTS_28 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_29(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='29'
    return out

BLACKVUE_ENDPOINTS_29 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_30(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='30'
    return out

BLACKVUE_ENDPOINTS_30 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_31(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='31'
    return out

BLACKVUE_ENDPOINTS_31 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_32(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='32'
    return out

BLACKVUE_ENDPOINTS_32 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_33(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='33'
    return out

BLACKVUE_ENDPOINTS_33 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_34(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='34'
    return out

BLACKVUE_ENDPOINTS_34 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_35(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='35'
    return out

BLACKVUE_ENDPOINTS_35 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_36(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='36'
    return out

BLACKVUE_ENDPOINTS_36 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_37(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='37'
    return out

BLACKVUE_ENDPOINTS_37 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_38(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='38'
    return out

BLACKVUE_ENDPOINTS_38 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_39(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='39'
    return out

BLACKVUE_ENDPOINTS_39 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_40(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='40'
    return out

BLACKVUE_ENDPOINTS_40 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_41(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='41'
    return out

BLACKVUE_ENDPOINTS_41 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_42(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='42'
    return out

BLACKVUE_ENDPOINTS_42 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_43(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='43'
    return out

BLACKVUE_ENDPOINTS_43 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_44(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='44'
    return out

BLACKVUE_ENDPOINTS_44 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_45(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='45'
    return out

BLACKVUE_ENDPOINTS_45 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_46(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='46'
    return out

BLACKVUE_ENDPOINTS_46 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_47(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='47'
    return out

BLACKVUE_ENDPOINTS_47 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_48(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='48'
    return out

BLACKVUE_ENDPOINTS_48 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_49(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='49'
    return out

BLACKVUE_ENDPOINTS_49 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_50(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='50'
    return out

BLACKVUE_ENDPOINTS_50 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_51(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='51'
    return out

BLACKVUE_ENDPOINTS_51 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_52(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='52'
    return out

BLACKVUE_ENDPOINTS_52 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_53(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='53'
    return out

BLACKVUE_ENDPOINTS_53 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_54(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='54'
    return out

BLACKVUE_ENDPOINTS_54 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_55(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='55'
    return out

BLACKVUE_ENDPOINTS_55 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_56(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='56'
    return out

BLACKVUE_ENDPOINTS_56 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_57(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='57'
    return out

BLACKVUE_ENDPOINTS_57 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_58(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='58'
    return out

BLACKVUE_ENDPOINTS_58 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_59(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='59'
    return out

BLACKVUE_ENDPOINTS_59 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_60(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='60'
    return out

BLACKVUE_ENDPOINTS_60 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_61(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='61'
    return out

BLACKVUE_ENDPOINTS_61 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_62(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='62'
    return out

BLACKVUE_ENDPOINTS_62 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_63(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='63'
    return out

BLACKVUE_ENDPOINTS_63 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_64(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='64'
    return out

BLACKVUE_ENDPOINTS_64 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_65(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='65'
    return out

BLACKVUE_ENDPOINTS_65 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_66(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='66'
    return out

BLACKVUE_ENDPOINTS_66 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_67(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='67'
    return out

BLACKVUE_ENDPOINTS_67 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_68(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='68'
    return out

BLACKVUE_ENDPOINTS_68 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_69(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='69'
    return out

BLACKVUE_ENDPOINTS_69 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_70(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='70'
    return out

BLACKVUE_ENDPOINTS_70 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_71(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='71'
    return out

BLACKVUE_ENDPOINTS_71 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_72(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='72'
    return out

BLACKVUE_ENDPOINTS_72 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_73(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='73'
    return out

BLACKVUE_ENDPOINTS_73 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_74(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='74'
    return out

BLACKVUE_ENDPOINTS_74 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_75(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='75'
    return out

BLACKVUE_ENDPOINTS_75 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_76(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='76'
    return out

BLACKVUE_ENDPOINTS_76 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_77(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='77'
    return out

BLACKVUE_ENDPOINTS_77 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_78(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='78'
    return out

BLACKVUE_ENDPOINTS_78 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

def parse_vod_line_79(line: str) -> Dict[str,str]:
    # BlackVue vod listing lines often look like n:/Record/...,s:size
    out={}
    for part in line.strip().split(','):
        if ':' in part:
            k,v=part.split(':',1); out[k.strip()]=v.strip()
    out['variant']='79'
    return out

BLACKVUE_ENDPOINTS_79 = {'live':'/blackvue_live.cgi','vod':'/blackvue_vod.cgi','cfg':'/Config/config.ini','ver':'/Config/version.bin'}

