try:
   import netmiko
   from netmiko import ConnectHandler
   import regex as re
   import time
except:
   print("install required modules")

user={'device_type': 'cisco_ios',
   'ip': '192.168.100.1',
   'password': 'lab123',
   'username': 'lab'}

user2={'device_type': 'cisco_ios',
   'ip': '192.168.200.2',
   'password': 'lab123',
   'username': 'lab'}

def router1():
   a=['router ospf 1', 'network 192.168.100.0 0.0.0.255 area 0', 'network 192.168.200.0 0.0.0.255 area 0', 'end']
   connect=netmiko.ConnectHandler(**user)
   connect.enable()
   aa=connect.send_config_set(a)
   print(aa)
   connect.disconnect()
   return

def router2():
    a='ssh -l lab 192.168.200.2'
    connect2=netmiko.ConnectHandler(**user)
    connect2.enable()
    aa=connect2.send_command_timing(a)
    if 'Password:' in aa:
      aa+=connect2.send_command_timing('lab123')
    print(aa)
    bb=connect2.send_command_timing('conf t'+'\n'+'router ospf 1'+'\n'+'network 172.16.100.0 0.0.0.255 area 0'+'\n'+'network 192.168.200.0 0.0.0.255 area 0'+'\n'+'end')
    print(bb)
    connect2.disconnect()
    return

def router3():
    a='ssh -l lab 172.16.100.1'
    connect3=netmiko.ConnectHandler(**user2)
    connect3.enable()
    aa=connect3.send_command_timing(a)
    if 'Password:' in aa:
      aa+=connect3.send_command_timing('lab123')
    print(aa)
    bb=connect3.send_command_timing('conf t'+'\n'+'router ospf 1'+'\n'+'network 172.16.100.0 0.0.0.255 area 0'+'\n'+'network 10.20.30.0 0.0.0.255 area 0'+'\n'+'end')
    print(bb)
    connect3.disconnect()
    return

if __name__=='__main__':
    router1()
    #time.sleep(120)
    router2()
    #time.sleep(120)
    router3()
