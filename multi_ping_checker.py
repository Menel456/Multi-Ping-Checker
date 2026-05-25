import os

print("Welcome to Multi Ping Checker!")

host1 = input("Type IP or website name: ") 
host2 = input("Type IP or website name: ") 
host3 = input("Type IP or website name: ")

hosts = [host1, host2, host3]

for host in hosts:
  print("\n")
  os.system("ping -c 2 " + host) 
  print("\n")
