import subprocess
import os
subprocess.run('conda activate base && python D:/web_dev/warehouse-system/python_scripts/image_download.py && conda deactivate', shell=True)
subprocess.run('conda activate tensorflow && python D:/web_dev/warehouse-system/python_scripts/test_model.py && conda deactivate', shell=True)