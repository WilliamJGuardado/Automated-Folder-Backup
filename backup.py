import os
import shutil
import datetime
import schedule
import time
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

source_dir = "C:/Users/William/Documents"
destination_dir = "T:/Documents Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        logging.info(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        logging.warning(f"Folder already exists in: {dest_dir}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Scheduling the copy task
schedule.every().day.at("08:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))


try:
    while True:
        schedule.run_pending()
        time.sleep(60)
except KeyboardInterrupt:
    logging.info("Program terminated by user.")
