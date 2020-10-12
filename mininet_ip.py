try:
   import netmiko
   from netmiko import ConnectHandler
   import regex as re
except:
   print("install required modules")
user={'device_type': 'cisco_ios',
   'ip': '192.168.100.1',
   'password': 'lab123',
   'username': 'lab'}

def ip_leased():
   a='sh ip dhcp bind'
   connect=netmiko.ConnectHandler(**user)
   connect.enable()
   aa=connect.send_command(a)
   #print(aa)
   ip=re.findall( r'[0-9]+(?:\.[0-9]+){3}',aa)
   #print(ip)
   return ip[0]

if __name__=='__main__':
   print(ip_leased())
