import subprocess
import os
from executable import Executable

def compile(executable, path):
    filename, ext = os.path.splitext(path)
    file_ = open("%s.asm" % filename, "w")
    file_.write(str(executable))
    file_.close()
    subprocess.call(["nasm", "-f", "elf64", "%s.asm" % filename, "-o", "%s.o" % filename])
    subprocess.call(["ld", "-s", "%s.o" % filename, "-o", path])
