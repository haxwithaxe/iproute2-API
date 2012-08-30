
def resolve_any(any_dict, key):
	if key and type(any_dict) == dict and key in any_dict:
		return any_dict[key]
	return any_dict

