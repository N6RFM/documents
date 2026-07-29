#!/usr/bin/env python3
#
# Set center frequency by channel number on the RSA5065N Spectrum Analyzer
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import argparse
import pyvisa as visa
import sys

base = 5.6e9

parser = argparse.ArgumentParser(description=f"Set a {base/1e9} GHz uplink channel as Rigol center frequency")
parser.add_argument("channel", type=int, help="Desired channel number 1-31 or 33-63")
args = parser.parse_args()

channel = args.channel

if channel < 1 or channel == 32 or channel > 63:
	print(f'Channel {channel} is invalid')
	sys.exit(1)

if channel < 32:
	frequency = base + channel * 0.15625e6
else:
	frequency = base - (64 - channel) * 0.15625e6

print(f"Setting frequency to channel {channel} = {frequency / 1e6} MHz")

rm = visa.ResourceManager('@py')
sa = rm.open_resource('TCPIP::rsa5065n.sandiego.openresearch.institute::INSTR')
# print(sa.query('*IDN?'))

sa.write(f':SENS:FREQ:CENT {frequency}')
print(sa.query(':SENSe:FREQuency:CENTer?'))
