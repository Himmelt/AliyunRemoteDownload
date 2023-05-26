import os
import wget
from aligo import Aligo

name = 'filename'
url = 'https://url'

os.system("wget --no-check-certificate -O ${name} ${url}")

ali = Aligo()
remote_folder = ali.get_folder_by_path('RemoteDownload')
ali.upload_file(name, parent_file_id=remote_folder.file_id)
