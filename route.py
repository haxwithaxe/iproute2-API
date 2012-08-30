#!/usr/bin/env python2

import util

class route(object):
	def __init__(self, src=SUBNET_ANY, dest=SUBNET_ANY, rtype=ROUTE_DEFAULT, proto=IP_4):
		self.proto = proto
		self.src = _resolve_any(src, proto)
		self.dest = _resolve_any(dest, proto)
		self.rtype = rtype
	def set(self):
		pass

	def remove(self):
		pass

