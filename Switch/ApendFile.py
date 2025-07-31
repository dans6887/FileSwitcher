import os
import sys

def append_extension_to_files(directory_path, extension=".x"):
    """
    Appends a specified extension to all files in the given directory.

    Args:
        directory_path (str): The path to the directory containing the files.
        extension (str): The extension to append (e.g., ".x").
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.", file=sys.stderr)
        return

    print(f"Attempting to append '{extension}' to files in: {directory_path}")
    print("-" * 50)

    files_processed = 0
    files_skipped = 0

    try:
        # List all entries in the given directory
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)

            # Check if the entry is a file (and not a directory or symlink)
            if os.path.isfile(full_path):
                # Construct the new filename by appending the extension
                new_full_path = full_path + extension
                try:
                    # Rename the file
                    os.rename(full_path, new_full_path)
                    print(f"Renamed: '{entry}' -> '{entry}{extension}'")
                    files_processed += 1
                except OSError as e:
                    print(f"Error renaming '{entry}': {e}", file=sys.stderr)
                    files_skipped += 1
            else:
                print(f"Skipped: '{entry}' (not a file)")
                files_skipped += 1

    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'. "
              "Please run the script with appropriate permissions (e.g., using sudo if necessary).", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

    print("-" * 50)
    print(f"Summary: {files_processed} files processed, {files_skipped} files skipped.")

if __name__ == "__main__":
    # Define the target directory.
    # IMPORTANT: Change this to the actual directory you intend to modify.
    # For safety, it's initially set to a placeholder.
    # Uncomment and modify the line below with your actual directory path.
    # target_directory = "/opt/parkplacetechnologies/agent/collector/etc/scripts/original-scripts"
    
    # For testing purposes, you might want to use a temporary directory first:
    # import tempfile
    # temp_dir = tempfile.mkdtemp()
    # print(f"Using temporary directory for testing: {temp_dir}")
    # with open(os.path.join(temp_dir, "testfile1"), "w") as f: f.write("content")
    # with open(os.path.join(temp_dir, "testfile2.txt"), "w") as f: f.write("content")
    # os.makedirs(os.path.join(temp_dir, "subdir"), exist_ok=True) # Create a subdir to show it's skipped
    # target_directory = temp_dir

    # *** IMPORTANT: Replace the placeholder below with your actual directory path. ***
    target_directory = "/opt/parkplacetechnologies/agent/collector/etc/scripts/original-scripts"

    # Call the function to append the extension
    append_extension_to_files(target_directory, ".x")

    # If you used a temporary directory for testing, you might want to clean it up:
    # import shutil
    # shutil.rmtree(temp_dir)
