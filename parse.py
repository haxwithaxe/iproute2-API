import util


def parse_ip_addr_show(stdout, stderr):
	if len(stdout) > 0:
		lines = []
		_line = []
		for line in stdout.split('\n'):
			if ip_first_line_re.match(line):
				lines.append(';'.join(_line))
				_line = line.split(':',2)
			else:
				_line.append(line.strip())
	else:
		_parse_ip_err(stderr)

