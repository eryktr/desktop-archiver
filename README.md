# desktop-archiver
Script to automatically clean your desktop and save its state to properly a properly date-marked folder.

## Installing dependencies

      pip install -r requirements.txt
      
## Changing base folder
Change the value of the **destination_folder** key in **config.txt**.

## Functioning
The script will create a folder with today's date (according to your locale) as its name and move there all files from your desktop.

##Running

      python desktop-archiver.py
