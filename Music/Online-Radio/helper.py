import os
import json

def load_json(path, model):
	try:
		# Load settings, including station list
		with open(path, 'r') as f:
			loaded = json.load(f)
			model.show('Settings loaded.')
			return loaded

	except Exception as e:
		model.show('Exception occured:\n', e)
		return model.settings # default...


def clean_path(path):
	# In case path contains file name, 
	# remove it and return remaining path
	separator = '/'
	parts = path.split(separator) # TODO: make system independent
	if '.' in parts[-1]:
		path = separator.join(parts[:-1])
	return path
	

def save_json(path, data, model):
	folder = clean_path(path)
	# Make sure path exists
	if not os.path.exists(folder):
		os.makedirs(folder)
		model.show('Created path:', folder)

	with open(path, 'w') as f:
		json.dump(data, f)

	model.show('Saved setting to:', path)