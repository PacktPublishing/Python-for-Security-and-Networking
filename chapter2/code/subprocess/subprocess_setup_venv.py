import subprocess
from pathlib import Path

VENV_NAME = '.venv'
REQUIREMENTS = 'requirements.txt'
process = subprocess.run(['which', 'python3'], capture_output=True, text=True)
if process.returncode != 0:
    raise OSError('Sorry python3 is not installed')
python_process = process.stdout.strip()
print(f'Python found in: {python_process}')

process = subprocess.run('echo "$SHELL"', shell=True, capture_output=True, text=True)
shell_bin = process.stdout.split('/')[-1]
create_venv = subprocess.run([python_process, '-m', 'venv', VENV_NAME], check=True)
if create_venv.returncode == 0:
    print(f'Your venv {VENV_NAME} has been created')
else:
    print(f'Your venv {VENV_NAME} has not been created')
    
pip_process = f'{VENV_NAME}/bin/pip3'
if Path(REQUIREMENTS).exists():
    print(f'Requirements file "{REQUIREMENTS}" found')
    print('Installing requirements')
    subprocess.run([pip_process, 'install', '-r', REQUIREMENTS])
    
print('Process completed! Now activate your environment with "source .venv/bin/activate"')
