#!/usr/bin/env python
import json
import os
import jupyter_client

km = None
client = None

def start(name):
	global client
	global km
	km = jupyter_client.KernelManager(kernel_name=name)
	km.start_kernel()
	client = km.blocking_client()
	msg = client.get_iopub_msg()
	while not (msg['msg_type'] == 'status' and 
		    msg['content']['execution_state'] == 'starting'):
		msg = client.get_iopub_msg()

def execute(code):
	global client
	outputs = []
	msg = None
	client.execute(code)
	msg = client.get_iopub_msg()
	while not (msg['msg_type'] == 'status' and
		    msg['content']['execution_state'] == 'idle'):
		if msg['msg_type'] == 'stream':
			outputs.append(msg['content'])
		msg = client.get_iopub_msg()
	return outputs



__dirname = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

	start('matlab_kernel')

	notebook = json.load(open(os.path.join(__dirname, '..', 'scalar-arithmetic', 'scalar-arithmetic.ipynb')))
	for cell in notebook['cells']:
		if cell['cell_type'] == 'code':
			inputs = ''.join(cell['source'])
			if len(inputs) == 0:
				continue
			print 'input: ' + json.dumps(inputs)
			print 'executing input'
			actual_outputs = execute(inputs)
			expected_outputs = cell['outputs']
			print 'expected output: ' + json.dumps(expected_outputs)
			print 'actual output: ' + json.dumps(actual_outputs)

	client.shutdown()

