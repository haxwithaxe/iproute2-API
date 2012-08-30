
class defs(object):
	def __init__(self):
		# Layer 2 Types
		self.IP_4 = 0
		self.IP_6 = 1
		self.IP_BOTH = 10
		self.IPX = 2
		self.DNET = 3
		self.LINK = 4
		# Routes
		self.ROUTE_DEFAULT_IP_4 = '0.0.0.0'
		self.ROUTE_DEFAULT_IP_6 = '::0'
		self.ROUTE_DEFAULT_ANY = {self.IP_4:self.DEFAULT_ROUTE_IP_4, self.IP_6:self.DEFAULT_ROUTE_IP_6}
		# Subnets
		self.IP_4_ANY = '0.0.0.0/0'
		self.IP_6_ANY = '[::]/0'
		self.SUBNET_ANY = {self.IP_4:self.IP_4_ANY, self.IP_6:self.IP_6_ANY}

