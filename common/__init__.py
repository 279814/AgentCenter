import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
sys.path.insert(0, model_file_path)

from Common import *