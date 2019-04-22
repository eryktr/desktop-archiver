import shutil
import os   
import datetime
import glob

class FileManager:

    def archive_desktop_files(self, base_path):
        files = self._get_desktop_files_list()
        base_path = os.path.expanduser(base_path)
        for fil in files:
            self._move_to_appropriate_folder(fil, base_path)

    def _get_desktop_files_list(self):
        desktop_path = os.path.expanduser("~/Desktop/*")
        files = [f for f in glob.glob(desktop_path) if os.path.isfile(f) or os.path.isdir(f)]
        return files
            
    def _move_to_appropriate_folder(self, source, base_path):
        path = self._assemble_destination_name(base_path)
        if not os.path.isdir(path):
            os.makedirs(path)
        shutil.move(source, path)

    def _assemble_destination_name(self, base_path):
        date = str(datetime.datetime.today().strftime('%Y-%m-%d'))
        path = os.path.join(base_path, date)
        return path