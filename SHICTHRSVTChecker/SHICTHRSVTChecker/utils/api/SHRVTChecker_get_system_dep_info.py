
import ctypes
from ctypes import wintypes
from copy import deepcopy

PROCESSOR_FEATURE = 12

def SHRVChecker_get_system_dep_info(error_class) -> dict:
    DataExecutionPrevention_info : dict = {}
    
    class SYSTEM_INFO(ctypes.Structure):
        _fields_ = [
            ("wProcessorArchitecture", wintypes.WORD),
            ("wReserved", wintypes.WORD),
            ("dwPageSize", wintypes.DWORD),
            ("lpMinimumApplicationAddress", wintypes.LPVOID),
            ("lpMaximumApplicationAddress", wintypes.LPVOID),
            ("dwActiveProcessorMask", wintypes.LPVOID),
            ("dwNumberOfProcessors", wintypes.DWORD),
            ("dwProcessorType", wintypes.DWORD),
            ("dwAllocationGranularity", wintypes.DWORD),
            ("wProcessorLevel", wintypes.WORD),
            ("wProcessorRevision", wintypes.WORD),
        ]
    
    try:
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel32.GetSystemInfo.argtypes = [ctypes.POINTER(SYSTEM_INFO)]
        kernel32.GetSystemInfo.restype = None
        
        system_info = SYSTEM_INFO()
        kernel32.GetSystemInfo(ctypes.byref(system_info))
        
        kernel32.IsProcessorFeaturePresent.argtypes = [wintypes.DWORD]
        kernel32.IsProcessorFeaturePresent.restype = wintypes.BOOL
        
        nx_supported = kernel32.IsProcessorFeaturePresent(PROCESSOR_FEATURE)
        DataExecutionPrevention_info['NX_Support_Stu'] = deepcopy(str(bool(nx_supported)).upper())
    except Exception as e:
        raise error_class(f"SHRVTCheckerException [ERROR.5002.1] unable to get nx_supported status. | {str(e)}")
    
    try:
        kernel32.GetProcessDEPPolicy.argtypes = [
            wintypes.HANDLE, 
            ctypes.POINTER(wintypes.DWORD), 
            ctypes.POINTER(wintypes.BOOL)
        ]
        kernel32.GetProcessDEPPolicy.restype = wintypes.BOOL
        
        dep_flags = wintypes.DWORD()
        permanent = wintypes.BOOL()
        
        current_process = kernel32.GetCurrentProcess()
        success = kernel32.GetProcessDEPPolicy(
            current_process, 
            ctypes.byref(dep_flags), 
            ctypes.byref(permanent)
        )
        
        if success:
            DataExecutionPrevention_info['DEP_Policy_Flag'] = deepcopy(str(dep_flags.value).upper())
            DataExecutionPrevention_info['DEP_Permanent_Setting'] = deepcopy(str(bool(permanent.value)).upper())

            dep_policies_CPT = {
                0 : "DEP Disabled",
                1 : "DEP enabled for essential Windows programs and services",
                2 : "DEP is enabled for all programs",
                3 : "DEP is enabled for all programs , except for specific programs"
            }

            # dep_policies_CPT = {
            #     0 : "DEP禁用",
            #     1 : "DEP对基本Windows程序和服务启用",
            #     2 : "DEP对所有程序启用",
            #     3 : "DEP对所有程序启用，特定程序除外"
            # }
            
            policy_desc = dep_policies_CPT.get(dep_flags.value , "Unknown strategy")
            DataExecutionPrevention_info['DEP_Strategy'] = deepcopy(policy_desc)
    except Exception as e:
        raise error_class(f"SHRVTCheckerException [ERROR.5002.2] unable to get DEP_Strategy/DEP_Policy_Flag/DEP_Permanent_Setting status. | {str(e)}")

    return DataExecutionPrevention_info