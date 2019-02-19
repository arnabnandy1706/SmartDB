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
SERIAL = serial.stdout.read().split('\n')[0]
print("Seral Number: "+ str(SERIAL))

model = subprocess.Popen('sudo cat /sys/devices/virtual/dmi/id/product_name', stdout=subprocess.PIPE, shell=True)
MODEL = model.stdout.read().split('\n')[0]
print("Model: "+ str(MODEL))

ip = subprocess.Popen('hostname -I', stdout=subprocess.PIPE, shell=True)
IP = ip.stdout.read().split('\n')[0]
print("IP(s): "+ str(IP))

os = subprocess.Popen('/bin/uname -a', stdout=subprocess.PIPE, shell=True)
OS = os.stdout.read().split('\n')[0]
print("OS: "+OS)

fileBuff = open("/tmp/details.txt","w")

fileBuff.write("HOSTNAME="+HOSTNAME+"\n")
fileBuff.write("CPU="+CPU+"\n")
fileBuff.write("MEM="+MEM+"\n")
fileBuff.write("SERIAL="+SERIAL+"\n")
fileBuff.write("MODEL="+MODEL+"\n")
fileBuff.write("IP="+IP+"\n")
fileBuff.write("OS="+OS+"\n")

fileBuff.close()
