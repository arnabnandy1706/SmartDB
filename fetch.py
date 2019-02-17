import subprocess
import sys
import datetime


# Variables required to store the values

HOSTNAME=""
CPU=""
MEM=""
SERIAL=""
MODEL=""
STORAGE=""
NETWORKPORT=""
IP=""
OS=""


hostname = subprocess.Popen('hostname', stdout=subprocess.PIPE)
HOSTNAME = hostname.stdout.read().strip('\n')
print("Hostname: "+HOSTNAME)

cpu = subprocess.Popen('cat /proc/cpuinfo | grep processor | wc -l', stdout=subprocess.PIPE, shell=True)
CPU = cpu.stdout.read().strip('\n')
print("CPU: "+CPU)

mem = subprocess.Popen("cat /proc/meminfo | grep -w MemTotal | cut -d ':' -f2 | awk '{print $1}'", stdout=subprocess.PIPE, shell=True)
MEM = mem.stdout.read().strip('\n')
print("Memory: "+MEM)

serial = subprocess.Popen('sudo cat /sys/devices/virtual/dmi/id/product_serial', stdout=subprocess.PIPE, shell=True)
SERIAL = serial.stdout.read().split('\n')
print("Seral Number; "+SERIAL)