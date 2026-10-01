from pathlib import Path
import shutil


def organize_folder_by_extension(target_directory):
    """Groups files in target_directory into subfolders based on their file extensions."""
    folder_path = Path(target_directory)

    # Ensure the directory exists
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Directory '{target_directory}' does not exist or is not a folder.")
        return

    for item in folder_path.iterdir():
        # Process files only (ignore subdirectories)
        if item.is_file():
            # Extract extension without leading dot (e.g., 'pdf', 'txt').
            # Label files without an extension as 'no_extension'
            ext = item.suffix[1:].lower() if item.suffix else "no_extension"

            # Destination folder path named after extension
            dest_folder = folder_path / ext

            # Create destination directory if it doesn't exist
            dest_folder.mkdir(exist_ok=True)

            # Move file into the extension subfolder
            destination = dest_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {ext}/")


# --- Example Usage ---
# Replace 'practice_folder' with your target directory path
practice_folder = "./practice_folder"

# Creating a test directory with sample files for demonstration
test_dir = Path(practice_folder)
test_dir.mkdir(exist_ok=True)
(test_dir / "document.pdf").touch()
(test_dir / "notes.txt").touch()
(test_dir / "image.png").touch()
(test_dir / "script.py").touch()
(test_dir / "README").touch()

# Run the organizer
organize_folder_by_extension(practice_folder)