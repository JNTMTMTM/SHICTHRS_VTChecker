
import subprocess

def run_powershell_command(error_class , command : list) -> str | None:
    result = subprocess.run(
        command ,
        capture_output = True ,
        text = True ,
        check = True
    )
    lines : list = list(filter(None , list(map(lambda x: x.strip() , result.stdout.split('\n')))))

    if len(lines) == 0:
        raise error_class(f"SHRVTCheckerException [ERROR.5000] no result output")

    print(lines)
    if str(lines[-1]).lower() != 'true' and str(lines[-1]).lower() != 'false':
        raise error_class(f"SHRVTCheckerException [ERROR.5000.1] an invalid parameter was output")

    f_result : str = ' : '.join(lines)
    return f_result
