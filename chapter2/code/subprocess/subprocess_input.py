import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "import sys; print(sys.stdin.read())"], input=b"python"
)
