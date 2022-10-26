import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "raise ValueError('error')"], check=True)
