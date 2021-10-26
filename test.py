import os


VH_INPUTS_DIR = os.getenv('VH_INPUTS_DIR', '.inputs/')
VH_OUTPUTS_DIR = os.getenv('VH_OUTPUTS_DIR', '.outputs/')


image_path = os.path.join(VH_INPUTS_DIR, 'imagine-test-image/0002202d-d8be-4ddf-8fdb-b2dbb8606bee')
assert os.path.exists(image_path)

with open(os.path.join(VH_OUTPUTS_DIR, 'test.txt'), 'w') as f:
    f.write('Hello!')
