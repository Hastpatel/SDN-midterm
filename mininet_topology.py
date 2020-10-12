try:
   import netmiko
   from netmiko import ConnectHandler
   import regex as re
   from mininet_ip import *
   import time
except:
   print("install required modules")

ip=ip_leased()
#print(ip)

user={'device_type': 'linux',
   'ip': ip,
   'password': 'mininet',
   'username': 'mininet',
    'secret':'mininet'}
#print(user)

connect_main=netmiko.ConnectHandler(**user)
connect_main.enable()

def mininet_init():
   mini='sudo mn'
   mininet=connect_main.send_command_timing(mini)
   if 'Password:' in mininet:
      mininet+=connect_main.send_command_timing('mininet')
   print(mininet)
   return

def controller_config():
   mininet2=connect_main.send_command_timing('sh ovs-vsctl set bridge s1 protocols=OpenFlow13'+'\n'+'sh ovs-vsctl set-controller s1 tcp:10.20.30.2:6633')
   print(mininet2)
   return

def pingall():
   mininet3=connect_main.send_command_timing('pingall')
   #print(mininet3)
   return

def controller_connectivity():
   show='sudo ovs-vsctl show'
   connect3=netmiko.ConnectHandler(**user)
   connect3.enable()
   see=connect3.send_command_timing(show)
   if 'Password:' in see:
      see+=connect3.send_command_timing('mininet')
   print(see)
   connect3.disconnect()
   return

def flows():
   flow=connect_main.send_command_timing('sh ovs-ofctl dump-flows s1 --protocols=OpenFlow13 | grep actions=CONTROLLER')
   print(flow)
   print(flow.split('n_packets='))
   f=flow.split('n_packets=')[1]
   r=r"^(\d+)"
   p=re.findall(r,f)
   print(p)
   return p

if __name__=='__main__':
   mininet_init()
   controller_config()
   controller_connectivity()
   pingall()
   flows()
