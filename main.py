import os
import wget
from aligo import Aligo

name = 'XXMixReal-v3.0.safetensors'
url = 'https://civitai.com/api/download/models/77903'

os.system("wget --no-check-certificate -O XXMixReal-v3.0.safetensors https://civitai.com/api/download/models/77903")

ali = Aligo()
remote_folder = ali.get_folder_by_path('AI绘画/SD_模型')
ali.upload_file(name, parent_file_id=remote_folder.file_id)
