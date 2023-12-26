import sys
import hashlib
import json
import os
import shutil
from cryptography.fernet import Fernet
import logging
import subprocess


def hash_string(input_string):
    """Hash a string using SHA-256."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def check_status():
    with open(os.path.join(get_system(),"id1fs_status.json"), "r") as f:
        stat = json.load(f)
    if stat["status"] == "started":
        return True
    if stat["status"] == "stoped":
        return False


    
# user functions
def get_user():
    with open(os.path.join(get_system(),"id1fs_status.json"), "r") as f:
        stat = json.load(f)
    return stat["connected_user"]

def check_user():
    with open(os.path.join(get_system(),"id1fs_status.json"), "r") as f:
        stat = json.load(f)
    if stat["connected_user"] == "None":
        return False
    else:
        return True


def check_root():
    with open(os.path.join(get_system(),"id1fs_status.json"), "r") as f:
        stat = json.load(f)
    if stat["connected_user"] == "root":
        return True
    else:
        return False

def delete_user(username, users):
    """Delete a user from ID1FS."""
    print("User deleted.")
    del users[username]
    with open(os.path.join(get_system(),"login.json"), "w")as f:
        json.dump(users, f, indent=4)





# Path functions

def get_basename(path):
    """Return the basename of a path."""
    return os.path.basename(path)
def get_path(path):
    """Return the path of a file."""
    return os.path.dirname(path)
def check_path(path):
    """Check if the path exists."""
    if os.path.isdir(path):
        return True
    else:
        return False




# access functions
def check_access(path, access_type):
    """Check if the user has the access to the file."""
    if not check_file(path):
        print("This file doesn't exist.")
        return False
    user=get_user()
    key = load_key()
    fernet = Fernet(key)
    mdf = get_metadata_folder()
    for file in os.listdir(mdf):
        file_temp = bytes(file,'utf-8')
        temp = fernet.decrypt(file_temp).decode('utf-8')
        if temp.split('|')[0] == path:
            file_metadata = mdf+"/"+file
            with open(file_metadata, "r") as f:
                metadata = json.load(f)
                break
    if user == "root":
        return True
    elif metadata["access"][access_type] != "all" and metadata["owner"] != user:
        return False
    else:
        return True

def change_access(path, access_type, access):
    """Change the access to the file."""
    user=get_user()
    key = load_key()
    fernet = Fernet(key)
    mdf = get_metadata_folder()
    for file in os.listdir(mdf):
        file_temp = bytes(file, 'utf-8')
        temp = fernet.decrypt(file_temp).decode('utf-8')
        if temp.split('|')[0] == path:
            file_metadata = os.path.join(mdf,file)
            with open(file_metadata, "r") as f:
                metadata = json.load(f)
                break
    if metadata["owner"] != user and user != 'root':
        logging_config()
        logging.error(f"{get_user()} - {path.replace(get_root(),'')} changing access Permission denied.")
        print("You are not the owner of this file.")
        return False
    else:
        metadata["access"][access_type] = access
        with open(file_metadata, "w") as f:
            json.dump(metadata, f, indent=4)
        return True







def check_file(path):
    try:
        with open(path, "r"):
            return True
    except FileNotFoundError:
        return False


def create_file(path):
    """Create a file in the filesystem."""
    with open(path, "x"):
        pass
    create_file_backup(path)
    create_metadata(path)

def create_file_backup(path):
    """Create a backup file in the filesystem."""
    key = load_key()
    fernet = Fernet(key)
    bp_folder = get_backup()
    bp_name = generate_bp_name(path)
    bp_path = os.path.join(get_backup(),bp_name)
    for file in os.listdir(bp_folder):
        file_temp = bytes(file, 'utf-8')
        temp = fernet.decrypt(file_temp).decode('utf-8')
        if temp.split('|')[0] == path:
            os.remove(os.path.join(bp_folder,file))
            break
    print(bp_path)
    shutil.copy(path, bp_path)

def delete_file(path):
    """Delete a file from the filesystem."""
    if not check_file(path):
        print("This file doesn't exist.")
        return False
    else:
        if check_access(path, "w"):
            os.remove(path)
            delete_metadata(path)
            print(f"{path} deleted.")
            return True
        else:
            print("You are not the owner of this file.")
            return False
def delete_file_backup(path):
    """Delete a file backup from the filesystem."""
    key = load_key()
    fernet = Fernet(key)
    bp_folder = get_backup()
    for file in os.listdir(bp_folder):
        file_temp = bytes(file, 'utf-8')
        temp = fernet.decrypt(file_temp).decode('utf-8')
        if temp.split('|')[0] == path:
            os.remove(os.path.join(bp_folder,file))
            break


# directory functions
def check_dir(path):
    """Check if the directory exists."""
    if os.path.isdir(path):
        return True
    else:
        return False





# Metadata functions
def generate_md_name(path):
    """generate the backup name"""
    key = load_key()
    fernet = Fernet(key)
    md_name= path + '|' +get_user()
    md_name = fernet.encrypt(md_name.encode()).decode('utf-8')
    return md_name

def create_metadata(path):
    user = get_user()
    with open(get_system() + "/access.json", "r") as f:
        access=json.load(f)
    metadata={
            "owner":user,
            "access":access
            }
    with open(get_metadata_folder() +"/"+generate_md_name(path), "w") as f:
        json.dump(metadata, f, indent=4)

def delete_metadata(path):
    """Delete the metadat of a file."""
    mdf=get_metadata_folder()
    key = load_key()
    fernet = Fernet(key)
    for file in os.listdir(mdf):
        file_temp = bytes(file, 'utf-8')
        temp = fernet.decrypt(file_temp).decode('utf-8')
        if temp.split('|')[0] == path:
            os.remove(mdf+"/"+file)
            break
    




def load_key():
    with open(os.path.join(get_system(),"key.key"), "rb") as f:
        key = f.read()
    return key

def get_cwd():
    """Return the current working directory."""
    with open(get_system() + "/env.json", "r") as f:
        stat = json.load(f)
    return stat["cwd"]


def check_if_full_path(path):
    """Check if the path is a full path."""
    if path[0] == "/":
        return True
    else:
        return False


def get_root():
    """Return the root directory."""
    with open(get_system() + "/env.json", "r") as f:
        stat = json.load(f)
    return stat["root"]
def get_backup():
    """Return the backup directory."""
    with open(get_system() + "/env.json", "r") as f:
        stat = json.load(f)
    return stat["bf"]
def get_system():
    """Return the full paht to the system."""
    result = subprocess.run("whoami",capture_output = True, text = True,check = True)
    home_directory = "/home/" + result.stdout.strip()
    fs = f"{home_directory}/.temp/.FS/ID1FS"
    with open(f"{fs}/system/env.json", "r") as f:
        stat = json.load(f)
    return stat["systm"]

def get_metadata_folder():
    """Return the metadata folder."""
    with open(os.path.join(get_system(),"env.json"), "r") as f:
        stat = json.load(f)
    return stat["md"]

def generate_full_path(path):
    """Generate a name for a file."""
    if check_if_full_path(path):
        name = path
        return get_root() + name
    else:
        if path[0] == ".":
            name = path[1:]
            name = get_root()+get_cwd() + name
            return name
        else:
            if get_cwd() == "/":
                return get_root() + get_cwd() + path
            return get_root() + get_cwd() + '/' + path


def generate_bp_name(path):
    """generate the backup name"""
    key = load_key()
    fernet = Fernet(key)
    bp_name= path + '|' + get_user()
    bp_name = fernet.encrypt(bp_name.encode()).decode('utf-8')
    return bp_name


def restore_bp_name(bp_name):
    """Restore the backup path and owner."""
    key = load_key()
    fernet = Fernet(key)
    bp_name_temp = bytes(bp_name,'utf-8')
    temp = fernet.decrypt(bp_name_temp).decode('utf-8')
    path = temp.split("|")[0]
    owner = temp.split("|")[1]
    return [path, owner]


def restore_file(path):
    """Restore a file from a backup."""
    if not check_file(path):
        print("This file doesn't exist.")
        return False
    else:
        delete_file(path)
        bp_folder = get_backup()
        key = load_key()
        fernet = Fernet(key)
        for file in os.listdir(bp_folder):
            temp = fernet.decrypt(file).decode('utf-8')
            if temp.split('|')[0] == path:
                shutil.copy(bp_folder+"/"+file, path)
                break
        print(f"{path} restored.")
        return True

def get_log_file():
    with open(get_system() +'/env.json', 'r') as f:
        stat = json.load(f)
    return stat["log"]

def logging_config():
    """Configuring the log file."""
    log_file = get_log_file()
    logging.basicConfig(
        filename = log_file,
        level = logging.DEBUG,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )