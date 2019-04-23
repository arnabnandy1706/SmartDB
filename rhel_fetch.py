import subprocess
import sys
import datetime
import requests


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
NETPORT=""
FS=""


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

netport = subprocess.Popen("route -n | grep -Ev 'Destination|Kernel' | awk '{print $8}'", stdout=subprocess.PIPE, shell=True)
NETPORT = netport.stdout.read()
print("Interfaces: \n" +NETPORT)
fb = open("/tmp/netport.txt", "w")
fb.write(NETPORT)
fb.close()
fb = open("/tmp/netport.txt", "r")
networkPort = {}
netDetails = []
INETS = fb.readlines()
for inets in INETS:
  netDetails = []

  commandInet = "ifconfig " + inets.strip('\n') + " | grep -w inet | awk '{print $2}'"
  ipaddr = subprocess.Popen(commandInet, stdout=subprocess.PIPE, shell=True)
  IpAddr = ipaddr.stdout.read().split('\n')[0]
  netDetails.append(IpAddr)

  commandEther = "ifconfig " + inets.strip('\n') + " | grep -w ether | awk '{print $2}'"
  macaddr = subprocess.Popen(commandEther, stdout=subprocess.PIPE, shell=True)
  MacAddr = macaddr.stdout.read().split('\n')[0]
  netDetails.append(MacAddr)

  networkPort[inets.strip('\n')] = netDetails

fb.close()
print(networkPort)


fs = subprocess.Popen("df -k | grep -Ev 'shm|tmpfs|boot|cgroup|Filesystem' | awk '{print $6}'", stdout=subprocess.PIPE, shell=True)
filesystem = fs.stdout.read()
print("FileSystems: \n" +filesystem)
fb = open("/tmp/fs.txt", "w")
fb.write(filesystem)
fb.close()
fb = open("/tmp/fs.txt", "r")
Storage = {}
FS = fb.readlines()
for filesys in FS:
  fsDetails = []

  commandTotal = "df -kH " + filesys.strip('\n') + "| tail -1 | awk '{print $4}'"
  total = subprocess.Popen(commandTotal, stdout=subprocess.PIPE, shell=True)
  fsTotal = total.stdout.read().split('\n')[0]
  fsDetails.append(fsTotal)

  commandAvail = "df -kH " + filesys.strip('\n') + "| tail -1 | awk '{print $2}'"
  avail = subprocess.Popen(commandAvail, stdout=subprocess.PIPE, shell=True)
  fsAvail = avail.stdout.read().split('\n')[0]
  fsDetails.append(fsAvail)

  Storage[filesys.strip('\n')] = fsDetails

fb.close()
print(Storage)



fileBuff = open("/tmp/details.txt","w")

fileBuff.write("HOSTNAME="+HOSTNAME+"\n")
fileBuff.write("CPU="+CPU+"\n")
fileBuff.write("MEM="+MEM+"\n")
fileBuff.write("SERIAL="+SERIAL+"\n")
fileBuff.write("MODEL="+MODEL+"\n")
fileBuff.write("IP="+IP+"\n")
fileBuff.write("OS="+OS+"\n")
fileBuff.write("NETWORKPORTS="+str(networkPort)+"\n")
fileBuff.write("STORAGE="+str(Storage)+"\n")
fileBuff.close()

'''
data = {'hostname':HOSTNAME, 
        'cpu':CPU, 
        'mem':MEM,
	'serial':SERIAL,
	'model':MODEL,
	'ip':IP,
	'os':OS,
	'networkport':NETWORKPORTS, 
        'storage':STORAGE} 
API_ENDPOINT = "https://blockchain.com/createentry"
r = requests.post(url = API_ENDPOINT, data = data)
'''
