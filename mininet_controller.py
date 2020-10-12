try:
   import netmiko
   from netmiko import ConnectHandler
   import regex as re
   from mininet_ip import *
except:
   print("install required modules")


ip=ip_leased()
#print(ip)

user={'device_type': 'linux',
   'ip': ip,
   'password': 'mininet',
   'username': 'mininet',
    'secret':'mininet'}

def controller_config():
   controller='sudo ovs-vsctl set bridge s1 protocols=OpenFlow13'+'\n'+'sudo ovs-vsctl set-controller s1 tcp:10.20.30.2:6633'

   connect2=netmiko.ConnectHandler(**user)
   connect2.enable()
   cont=connect2.send_command_timing(controller)
   if 'Password:' in cont:
      cont+=connect2.send_command_timing('mininet')
   print(cont)
   connect2.disconnect()
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

if __name__=='__main__':
   controller_config()
   controller_connectivity()

