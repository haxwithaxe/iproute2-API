'''__init__.py: iproute2 exec API'''

import subprocess

# internal imports
import util
import defs
import address
import interface
import route

__all__ = ['address', 'defs', 'interface', 'parse', 'route', 'util']

class ip(object):
	def __init__(self):
		self.interfaces = []

	def list(self, **kwargs):
		pass

	def get(self, **kwargs):
		pass

	def add(self, **kwargs):
		pass

	def del(self, **kwargs):
		pass

