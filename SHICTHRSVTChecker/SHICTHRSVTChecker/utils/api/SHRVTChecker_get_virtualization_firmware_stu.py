
from ..SHRVTChecker_run_powershell_command import run_powershell_command

def SHRVChecker_get_virtualization_firmware_stu(error_class) -> dict:
    try:
        VirtualizationFirmware_stu : dict = run_powershell_command(error_class , ["wmic", "cpu", "get", "VirtualizationFirmwareEnabled"])
        
        if (not isinstance(VirtualizationFirmware_stu , dict)) or str(list(VirtualizationFirmware_stu.keys())[0]).lower() != 'virtualizationfirmwareenabled':
            raise error_class(f"SHRVTCheckerException [ERROR.5001.0] an invalid parameter was output")
            
        return VirtualizationFirmware_stu
    except Exception as e:
        raise error_class(f"SHRVTCheckerException [ERROR.5001] unable to get virtualization firmware status. | {str(e)}")
