
from ..SHRVTChecker_run_powershell_command import run_powershell_command

def SHRVChecker_get_system_slat_stu(error_class) -> dict:
    try:
        SecondLevelAddressTranslationExtensions_stu : dict = run_powershell_command(error_class , ["wmic", "cpu", "get", "SecondLevelAddressTranslationExtensions"])
        
        if (not isinstance(SecondLevelAddressTranslationExtensions_stu , dict)) or str(list(SecondLevelAddressTranslationExtensions_stu.keys())[0]).lower() != 'secondleveladdresstranslationextensions':
            raise error_class(f"SHRVTChecker [ERROR.5003.0] an invalid parameter was output")

        return SecondLevelAddressTranslationExtensions_stu
    except Exception as e:
        raise error_class(f"SHRVTChecker [ERROR.5003] unable to get second level address translation extensions status. | {str(e)}")


        