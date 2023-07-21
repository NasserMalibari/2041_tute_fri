
import subprocess


p1 = subprocess.run(["wget", "-O-", "-q", "https://wwwewrwerewrwev.unsw.edu.au"],text=True, capture_output=True)

p1.check_returncode()
# print(p1.stdout)
# print(p1.returncode)
# alternatively:
# p2 = subprocess.run("wget -O- -q", shell=True)