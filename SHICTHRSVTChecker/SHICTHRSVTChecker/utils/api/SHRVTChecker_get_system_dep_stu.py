
from ..SHRVTChecker_run_powershell_command import run_powershell_command

def SHRVChecker_get_system_dep_stu(error_class) -> dict:
    try:
        DataExecutionPrevention_stu : dict = run_powershell_command(error_class , ["wmic", "os", "get", "DataExecutionPrevention_Available"])
        
        if (not isinstance(DataExecutionPrevention_stu , dict)) or str(list(DataExecutionPrevention_stu.keys())[0]).lower() != 'dataexecutionprevention_available':
            raise error_class(f"SHRVTCheckerException [ERROR.5002.0] an invalid parameter was output")

        return DataExecutionPrevention_stu
    except Exception as e:
        raise error_class(f"SHRVTCheckerException [ERROR.5002] unable to get data execution prevention status. | {str(e)}")


        