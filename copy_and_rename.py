import os
import shutil
import re
from PIL import Image  # Requires Pillow: pip install Pillow

def generate_landscape_copies(source_dir, dest_dir):
    """
    Generate landscape copies of images from source_dir to dest_dir.
    
    Args:
        source_dir (str): Path to the source directory containing images.
        dest_dir (str): Path to the destination directory to save processed images.
    """
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Regex pattern to match source files (1.1.jpg, 1.2.png, etc.)
    pattern = re.compile(r'^1\.([1-8])\.(.+)$')
    
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if not os.path.isfile(source_path):
            continue  # Skip non-files
        
        match = pattern.match(filename)
        if match:
            middle_number = match.group(1)  # Middle number (1-8)
            file_extension = match.group(2).lower()  # File extension
            
            # Generate copies for numbers 1 to 44
            for n in range(1, 45):
                new_filename = f"{n}.{middle_number}.{file_extension}"
                dest_path = os.path.join(dest_dir, new_filename)
                
                # Copy the file
                shutil.copy(source_path, dest_path)
                
                # Rotate to landscape if needed
                try:
                    with Image.open(dest_path) as img:
                        if img.width < img.height:
                            # Rotate 90 degrees and overwrite
                            rotated = img.rotate(90, expand=True)
                            if file_extension in ['jpg', 'jpeg']:
                                rotated.save(dest_path, quality=95, optimize=True)
                            else:
                                rotated.save(dest_path)
                            print(f"Rotated {new_filename}")
                except Exception as e:
                    print(f"Error processing {new_filename}: {str(e)}")

if __name__ == '__main__':
    # Hardcoded paths
    SOURCE_DIR = r""
    DEST_DIR = r""
    
    generate_landscape_copies(SOURCE_DIR, DEST_DIR)