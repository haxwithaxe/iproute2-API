'''interface.py: ip interface object'''

import util

class InterfaceError(Exception):
	def set_if(self, interface):
		self.interface = interface

class interface(object):
	def __init__(self, name=None, addrs=[], proto=IP_BOTH, mtu=1500, state=None, qdisc=None, qlen=1000):
		self.proto = proto
		self.name = name
		self.addrs = addrs
		self.mtu = mtu
		self.state = state
		self.qdic = qdisc
		self.qlen = qlen
	
	def set(self):
	
	def load(self):
		self = ip.get(interface=name)
		return self

