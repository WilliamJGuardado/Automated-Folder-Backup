# Daily Folder Backup Script

This repository contains a Python script designed to automatically copy a specified source directory to a backup location every day at a specified time. The script uses the `schedule` library to manage timing and the `shutil` library to handle the copying process.

## Features

- **Automatic Daily Backups**: Set the script to run daily at 07:39 AM.
- **Error Handling**: Handles situations where the backup folder already exists, avoiding duplicates.
- **Logging**: Utilizes Python's logging module to log all actions, making it easier to debug and maintain.

## Prerequisites

Before you run this script, you will need to have Python installed along with the following Python packages:
- `datetime`
- `shutil`
- `os`
- `schedule`
- `time`
- `logging`

You can install the necessary libraries using pip:

```bash
pip install schedule

schedule.every().day.at("07:39").do(lambda: copy_folder_to_directory(source_dir, destination_dir))


### Implementation Notes:
- **Script Naming**: Ensure that your Python script is named `daily_backup.py` or adjust the documentation to match the actual filename.
- **License File**: If you mention a `LICENSE` file, make sure to actually include one in your repository. You can easily find MIT License templates online to include in your repository.



