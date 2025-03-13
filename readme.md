# Image Batch Copier & Renamer

A Python script to batch copy, rename, and enforce landscape orientation for image files. Designed for auction catalog preparation.

## Features
- **Batch Copy & Rename**: Generates 44 copies of original files (1.1-1.8) as 1.1-44.8  
- **Auto-Rotation**: Forces landscape orientation (rotates portrait images 90° clockwise)  
- **Regex Matching**: Processes only files matching `1.[1-8].[extension]` pattern  
- **Directory Handling**: Auto-creates destination folder if missing  
- **Format Preservation**: Maintains original file extensions (.jpg, .png, .jpeg, etc.)

## Prerequisites
- Python 3.6+
- Pillow library:  
  ```bash
  pip install Pillow
  ```

## Usage
1. **File Structure**:
   ```
   C:\Users\user\Downloads\  
   ├── Auction Auctioneers LOTS/  # Source directory  
   │   └── 1.1.jpg, 1.2.png...  # Original files  
   └── Kelani processed/         # Auto-created destination
   ```

2. **Run Script**:
   ```bash
   python copy_and_rename.py
   ```

3. **Process Flow**:
   - Creates destination directory if missing  
   - Copies while renaming files (1.1.jpg → 1.1.jpg, 2.1.jpg ... 44.1.jpg)  
   - Rotates portrait-oriented images to landscape  
   - Prints progress to console

## Output Structure
```
Kelani processed/  
├── 1.1.jpg  
├── 1.2.png  
├── ...  
├── 44.7.webp  
└── 44.8.jpeg  
```
*Note: All images will have width ≥ height after processing*

## Example
**Original**: `Aution Auctioneers LOTS/1.3.jpeg` (Portrait: 900x1600)  
**Processed**:  
- `Auction processed/44.3.jpeg` (Rotated to 1600x900)  

## Notes
- File name pattern must be: `[number].[1-8].[extension]`  
- Supports common image formats: JPG, PNG, JPEG, WEBP  
- Existing files in destination will be overwritten  

## License
MIT License - free for modification and redistribution
