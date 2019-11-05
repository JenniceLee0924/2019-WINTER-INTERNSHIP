#!/usr/bin/env python

#convert int into hex 
def int_hex(n):
	hex = '{n:x}'.format(n=n)
	if len(hex) & 1:
		hex = '0' + hex
	return hex.decode('hex')

print(int_hex(1245427))