# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS VT CHECKER
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

import os
from colorama import init
init()

from .utils.api.SHRVChecker_get_virtualization_firmware_stu import SHRVChecker_get_virtualization_firmware_stu
from .utils.api.SHRVChecker_get_system_dep_stu import SHRVChecker_get_system_dep_stu

print('\033[1mWelcome to use SHRVTChecker - VT info checker\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_VTChecker\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRVTCheckerException(BaseException):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message

def SHRVTChecker_get_vt_info() -> dict:
    # VirtualizationFirmware
    try:
        VirtualizationFirmware_stu : dict = SHRVChecker_get_virtualization_firmware_stu(SHRVTCheckerException)
        DataExecutionPrevention_stu : dict = SHRVChecker_get_system_dep_stu(SHRVTCheckerException)

        return {'VirtualizationFirmware' : VirtualizationFirmware_stu ,
                'DataExecutionPrevention_stu' : DataExecutionPrevention_stu}

    except Exception as e:
        raise SHRVTCheckerException(f"SHRVTCheckerException [ERROR.5000] unable to get VirtualizationFirmwareEnabled info. | {str(e)}")
