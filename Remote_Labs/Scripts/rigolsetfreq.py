#!/usr/bin/env python3
#
# Set center frequency on the RSA5065N Spectrum Analyzer
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import argparse
import pyvisa as visa

parser = argparse.ArgumentParser(description="Set a 5.6 GHz uplink channel as Rigol center frequency")
parser.add_argument("frequency", type=int, help="Desired center frequency")
args = parser.parse_args()

frequency = args.frequency

rm = visa.ResourceManager('@py')
sa = rm.open_resource('TCPIP::rsa5065n.sandiego.openresearch.institute::INSTR')
print(sa.query('*IDN?'))

sa.write(f':SENS:FREQ:CENT {frequency}')
print(sa.query(':SENSe:FREQuency:CENTer?'))
