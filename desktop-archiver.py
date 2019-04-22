import config_parser
import file_manager

p = config_parser.ConfigParser()
f = file_manager.FileManager()

dest = p.get_destination()
f.archive_desktop_files(dest)