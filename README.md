# monhunautosavebackup
Small script to keep several backups of a savefile.
The script will run and following a configurable interval,
check for changes in the game's savefile and if it has been changed,
copy it to a directory.

## Running the script
You will need a working Python 2.7 environment for this script to work.
You may obtain it from [Python's download section](https://www.python.org/downloads/release/python-2715/)
Once Python is installed, you can simply run it from the command line with `python monhunautosave.py` or by using the prepared start_monhun_backup.bat executable.
The script should be run before launching the game, and stopped once you stop playing.
If you are using the bat file, simply closing the window opened by the script will stop the process.

## Configuration
The file ***autosaveconf.json*** contains a few options, 
that should be changed to the user's needs.

**saveDirectory**:
	This will tell the script where the save file is located. 
	This option is mandatory, as it needs your Steam id.
	Since the \\ character is special, you will need to escape it for the path to work,
	which  would look like \\\\

**backupDirectory**:
	This will tell the script where the backed up files will be stored.
	By default, it will use a local directory, but setting up 
	a different directory is recomended.

**maxNumberOfBackups**:
	Limits how many files will be stored in the backupDirectory.
	should the limit be exceeded, the oldest backup will be removed to accomodate the newer one.
	
**checkAssiduity**:
	Interval (in seconds) at which the script will check for changes in the file.
	By default, it is set to 30 minutes (1800), as it is a costly operation to check a file every second.
