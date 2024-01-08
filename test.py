import subprocess
import sys

# subprocess.run("dir", shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
p = subprocess.Popen('az', shell=True, stdout=sys.stdout, stderr=sys.stderr)
p.communicate()