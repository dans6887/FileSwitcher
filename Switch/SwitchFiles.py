import os
import shutil
import sys

def manage_scripts():
    """
    Creates a new directory, moves an existing script, and copies a new script.
    This script requires elevated permissions (e.g., 'sudo python your_script_name.py')
    to modify files and directories in the /opt/ directory.
    """
    # Define the base directory where operations will occur
    scripts_base_dir = "/opt/parkplacetechnologies/agent/collector/etc/scripts"
    
    # Define the name of the script file
    script_file_name = "vmwarevsphere_login.groovy.ecf"

    # Define the path for the new directory where original scripts will be moved
    original_scripts_dir = os.path.join(scripts_base_dir, "original-scripts")

    # Define the full path of the script to be moved from the base directory
    # This assumes the file is initially in scripts_base_dir
    source_script_path_in_opt = os.path.join(scripts_base_dir, script_file_name)

    # Define the destination path for the script once it's moved
    destination_script_path_in_original_dir = os.path.join(original_scripts_dir, script_file_name)

    # Define the path of the new script file on the Desktop
    # IMPORTANT: Replace 'your_username' with your actual Linux username.
    # You can find your username by typing 'whoami' in your terminal.
    desktop_script_source_path = os.path.expanduser(f"/home/entuity/FileSwitcher/Switch/{script_file_name}")

    print(f"Starting script management operations...")
    print(f"Target base directory: {scripts_base_dir}")
    print(f"Script file name: {script_file_name}")

    # --- Step 1: Create a new directory called 'original-scripts' ---
    try:
        if not os.path.exists(original_scripts_dir):
            os.makedirs(original_scripts_dir)
            print(f"Successfully created directory: {original_scripts_dir}")
        else:
            print(f"Directory already exists: {original_scripts_dir}")
    except OSError as e:
        print(f"Error creating directory {original_scripts_dir}: {e}", file=sys.stderr)
        sys.exit(1) # Exit if directory creation fails

    # --- Step 2: Move the vmwarevsphere_login.groovy.ecf file to original-scripts directory ---
    try:
        if os.path.exists(source_script_path_in_opt):
            shutil.move(source_script_path_in_opt, destination_script_path_in_original_dir)
            print(f"Successfully moved '{script_file_name}' to '{original_scripts_dir}'")
        else:
            print(f"'{script_file_name}' not found in '{scripts_base_dir}', skipping move operation.")
            # Decide if this should be a fatal error or just a warning based on your needs
            # For now, it's a warning, and the script continues.
    except shutil.Error as e:
        print(f"Error moving file {source_script_path_in_opt} to {original_scripts_dir}: {e}", file=sys.stderr)
        sys.exit(1) # Exit if file move fails

    # --- Step 3: Copy the vmwarevsphere_login.groovy.ecf file from Desktop/ScriptSwitch to scripts_base_dir ---
    try:
        if os.path.exists(desktop_script_source_path):
            shutil.copy2(desktop_script_source_path, scripts_base_dir)
            print(f"Successfully copied '{script_file_name}' from '{desktop_script_source_path}' to '{scripts_base_dir}'")
        else:
            print(f"Error: Source file '{desktop_script_source_path}' not found. Cannot copy.", file=sys.stderr)
            sys.exit(1) # Exit if source file for copy doesn't exist
    except shutil.Error as e:
        print(f"Error copying file from {desktop_script_source_path} to {scripts_base_dir}: {e}", file=sys.stderr)
        sys.exit(1) # Exit if file copy fails

    print("All operations completed successfully!")



def add_x_extension_to_files(directory):
    """
    Adds a '.x' extension to every file in the specified directory.
    This function skips subdirectories.

    Args:
        directory (str): The path to the directory containing the files to rename.
    """
    print(f"\nAdding '.x' extension to files in '{directory}'...")
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            print(f"Error: Directory '{directory}' not found.", file=sys.stderr)
            return
            
        # List all entries in the directory
        for filename in os.listdir(directory):
            # Construct the full path
            old_filepath = os.path.join(directory, filename)
            
            # Check if the entry is a file (not a subdirectory)
            if os.path.isfile(old_filepath):
                # Check if the file already has a '.x' extension
                if not filename.endswith('.x'):
                    new_filepath = old_filepath + ".x"
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed '{filename}' to '{os.path.basename(new_filepath)}'")
                else:
                    print(f"File '{filename}' already has '.x' extension, skipping.")
    except OSError as e:
        print(f"Error processing files in directory {directory}: {e}", file=sys.stderr)
        sys.exit(1) # Exit if file renaming fails


if __name__ == "__main__":
    # Call the main function to run the script
    manage_scripts()
