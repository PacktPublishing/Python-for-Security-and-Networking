import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "import time; time.sleep(10)"], timeout=5)

