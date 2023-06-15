#!/usr/bin/env python
import socket, time
import getpass
import hashlib
from Crypto.Cipher import AES

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return
   
def Tcp_Write(D):
	D = (str(D) + "\n")
	s.send(D.encode())
	return 
   
def Tcp_Read( ):
	a = ' '
	b = ''
	#import pdb
	#pdb.set_trace()
	while a != '\n':
		a = s.recv(1).decode()
		b = b + str(a)
	return b
def Tcp_Close( ):
   s.close()
   return 

def PasswordCreate():
    user_in = getpass.getpass()
    password = hashlib.md5()
    password.update(user_in.encode("utf-8"))
    return password.hexdigest()

def main():
	Tcp_connect('0.0.0.0', 17098)
	
	option = (input("Enter 1 for login, 0 registration: "))
	#print(option)
	Tcp_Write(option)
	
	#print username, password

	#type_process = Tcp_Read()
	if(option == '0'):
		print (Tcp_Read())
		username = input("Enter your login username: ")
		password = PasswordCreate()
		Tcp_Write(username)
		#print Tcp_Read()
		Tcp_Write(password)
		#print Tcp_Read()
	elif(option == '1'):
		print (Tcp_Read())
		
		username = input("Enter your login username: ")
		password = PasswordCreate()		
		print(password)
		Tcp_Write(username)
		#print Tcp_Read()
		Tcp_Write(password)
		
		existence = Tcp_Read()
		existence = existence.strip('\n')

		false = "0"
		if(existence == false):
			print("Username does not exist")			
		else:
			random_token = Tcp_Read()
			random_token = random_token.strip('\n')
			obj = AES.new(random_token.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
			ciphertext = obj.encrypt(password.encode())
			Tcp_Write(ciphertext)
			auth_stat = Tcp_Read()
			auth_stat = auth_stat.strip('\n')
			#print auth_stat
			if(auth_stat == "Wrong Password"):
				print ("Error, Cannot Log in!")
			else:
				print("Logged In!")	
	print ("Closing Connection")	
	Tcp_Close()
	

if __name__ == '__main__':
	while(True):
		print("--- New connection ---")
		main()
