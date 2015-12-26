import sys
from termcolor import colored

colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[1;36m{0}\033[00m"
 
print colorred.format("Warning! Reactor meltdown. Evacuate immediately!")
print colorgrn.format("Ha-ha, just kidding!")
