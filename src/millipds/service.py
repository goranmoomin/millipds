import time

"""
This gets invoked via millipds.__main__.py
"""
def run(config):
	print("pretending to run millipds with config:", config)
	while True:
		print("running...")
		time.sleep(10)