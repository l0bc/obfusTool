#!/usr/bin/python3
import sys
import argparse


ip= res = ''
TYPE = ceross = 0
pointer = '.'
paddin=False
dotless=False
class ObfusType():
	global notationTypes
	notationTypes = {1:'zero',2:'octal',3:'hexa',4:'overflow',5:'binary',6:'dword',8: 'all'}
	quart = ceroInQuarter = 0
	def switch(self, TYPE):
		global notationTypes
		default = "Invalid obfuscation type"
		return getattr(self, TYPE, lambda: default)()
	def zero(self):
		global res,ip,ceross
		ip = ip.split(pointer)
		for i in range(len(ip)):
			if (i == 1 and ip[i] == '0' and ip[i+1] != '0'):
				res += '0.'
				continue
			if (ip[i] != '0' ):
				res += ip[i]+'.' 
			else:
				self.ceroInQuarter = i;
		res = res[:-1]
		return res
	def octal(self, melange=False):
		global pointer,ip
		result2 = list()
		ip = self.zero().split(pointer) if not(melange) else ip[self.quart]
		for i in range(len(ip)):
			j = int(ip[i]) if not(melange) else int(ip)
			result = []
			while j:
				res = j % 8
				result.insert(0,str(res))
				j = j // 8
			result.insert(0,'0') if( j == 0) else ''
			pad = 4-len(result) if (len(result)>1) else 0
			if(paddin): pad += ceross
			ceros = pad * '0'	
			result2.append(ceros+''.join(result))
			if(len(ip)<=3 and melange):break
		result2 = pointer.join(result2)
		return result2
	def hexa(self, boole=0, melange=False):
		global res,ip,dotless
		pad = ''
		if(dotless):
			ip = ip.split(pointer)if not(melange) else ip[self.quart]
		else:
			ip = self.zero().split(pointer)if not(melange) else ip[self.quart]
		if (boole):
			res = ''
			global TYPE
			for i in range(len(ip)):
				temp = hex(int(ip[i]))[2:] if not(melange) else hex(int(ip))[2:]
				if (len(temp)<2):temp = '0'+temp
				if not((len(ip)==3 and ip[i] == '0') or ip == '0'):
					res += temp  
					if(melange):break
				else:
					res += '00'
		else:
			res = ''
			for i in range(len(ip)):
				if(paddin):pad = ceross *'0'
				if (dotless):
					if (ip[i] == '0'):
						res += '00'
						continue
					formatted = hex(int(ip[i]))[2:]
					res = res + pad+formatted if (len(formatted)==2) else res +pad+'0'+formatted
				elif not(melange):
					res += '0x'+pad+hex(int(ip[i]))[2:]+'.'
				else:
					res ='0x'+pad+hex(int(ip))[2:]+'.'
					break
		if (dotless):
			res = '0x'+pad+res 
		elif (boole):
			res = '0x'+pad+res 
		else:
			res = res[:-1]
		return res
	def dword(self, melange=0):
		res = self.hexa(boole=True) 
		return '%d' % (int(res,16))
	def binary(self,melange=0):
		res = self.hexa(True,melange=False) if not(melange) else self.hexa(True,melange=True)
		pad = ceross*'0' if(paddin) else ''
		return pad+bin(int(res,16))[2:]
	def overflow(self,melange=False):
		global ip
		ip = self.zero().split(pointer)if not(melange) else ip[self.quart]
		res = ''
		for i in ip:
			if not(melange): 
				res += str(int(i)+256)+'.'
			else:	
				res += str(int(ip) + 256)+'.'
			if(melange):break
		return res[:-1]

	def all(self):
		global ippa,ip,notationTypes
		respu = ''
		ip = ippa = self.zero().split(pointer)
		obfuscated = {} 
		for quarter in range(len(ip)+1):
			if not(quarter == len(ip)):
				self.quart = quarter
				for obfType in range(4):
					obfuscated[quarter,obfType] = eval('self.'+notationTypes[obfType+2]+'(melange=True)')
					ip = ippa
					#print('resultado quarter_%d: --------- %s----------\n: %s' % (quarter, notationTypes[obfType+2], obfuscated[quarter,obfType]) ) #debbugging
			else:
				self.itteration(obfuscated,quarter)


	def itteration(self,obfuscated,quarter,a=0,b=0,c=0,d=0):
		boom = 0
		if((bool(a) or bool(b) or bool(c)) and bool(d)):
			foo = obfuscated[quarter,0].split('.')
			if(c):
				if(c > quarter-1):
					b += 1
					c = 0
				else:
					obfuscated[quarter,0] = '.'.join(foo[:2])+'.'
					self.itteration(obfuscated,quarter,a,b,c,d=0)
			if(b):
				d=0
				if(quarter == 3):
					if(b > quarter):
						a += 1
						b = 0
						d = 1
				else:
					if(b > quarter-1):
						a += 1
						b = 0
						self.itteration(obfuscated,quarter,a,b,c,1)
				obfuscated[quarter,0] = '.'.join(foo[:1])+'.'
				self.itteration(obfuscated,quarter,a,b,c,d)
			if(a):
				if(quarter ==2 ):
					if(a//2 > quarter-1):exit(0)
				elif(quarter ==3):
					if(a//2 == quarter-1):exit(0)
				else:
					if(a > quarter-1):
						exit(0)
				obfuscated[quarter,0] = ''
				self.itteration(obfuscated,quarter,a,0,0,0)
		else:
			if (c):
				n = c 
				d = quarter-2
				f = d
			elif (b):
				n = b
				d = 2 if (quarter ==4 ) else 1
				f = quarter-2
			elif (a):
				n = a
				d = f= 0
			else:
				n = f =0
			while f < quarter:
				if(d == quarter-1):
					if(quarter == 3):
						b +=1
						c = 0
					if(quarter == 4):c += 1
					if(quarter == 2):a += 1
					for i in range(4):
						print('%s%s' % (obfuscated[quarter, 0],obfuscated[d, i]))
				else:
					try:
						obfuscated[quarter, 0] += obfuscated[d , n]+'.'
						if(a): n = 0;
					except(KeyError):
						obfuscated[quarter, 0] = ''
						obfuscated[quarter, 0] += obfuscated[d , n]+'.'
				f += 1
				d += 1	
			self.itteration(obfuscated,quarter,a,b,c,d)

	def paddinng(self, seg):
		pad = ceross * '0'
		seg = pad + seg
		return seg

def print_info():
	global ip, TYPE, paddin, ceross, notationTypes, dotless
	Parser = argparse.ArgumentParser()
	Parser.add_argument('-t', '--type',dest='typp', help="Type of obfuscation: \n 1:zero\n 2:octal \n 3:hexa \n 4:dword\n 5:binary\n 6:overFlow \n", type=int,choices=[1,2,3,4,5,6])
	Parser.add_argument('-u','--ip-address',dest='ipp',help="IP address to be obfuscated",type=str)
	Parser.add_argument('-d','--dotless',dest='dotless',help="Resulting IP dottless (default) i.e. 0x7f01",action="store_true")
	Parser.add_argument('-p','--padding',dest='padding',help="How many ceros to pad", type=int, nargs='?', const=7)
	Parser.add_argument('-a','--alll', dest='alll', help="all combinations, default padding is 7", action='store_true')
	
	Args = Parser.parse_args()
	ip = Args.ipp
	if (Args.dotless): 
		dotless = True
	if (Args.alll):
		Args.typp = 8
	if ip  is None :
		Parser.print_help()
		exit(1)
	if TYPE  is None :
		Parser.print_help()
		exit(1)
	TYPE = notationTypes[Args.typp] 
	if Args.padding is not None:
		paddin = True
		ceross = Args.padding	
	return 0
	
print_info()
obfuscate = ObfusType()
print(obfuscate.switch(TYPE))

