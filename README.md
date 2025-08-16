# Library HTML Generator

This Python script generates a static HTML file with download buttons for all books and papers in your library collection.

## Features

- **Automatic Scanning**: Recursively scans the "Books and Papers" directory for all PDF files
- **Organized by Category**: Groups files by their subdirectory categories
- **Download Buttons**: Creates clickable download links following the GitHub raw URL pattern
- **File Information**: Displays file size and category for each document
- **Responsive Design**: Modern, mobile-friendly interface with hover effects
- **Statistics**: Shows total file count and category count

## Usage

1. **Run the script** from your library root directory:
   ```bash
   python generate_library_html.py
   ```

2. **Open the generated file**: The script creates `library_index.html` in the same directory

3. **View in browser**: Open the HTML file in any web browser to see your library

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

## Output

The script generates:
- `library_index.html` - The main HTML file with your library
- Console output showing file count and categories

## File Structure

The script expects your library to be organized as:
```
Books and Papers/
├── Astrophysics and Cosmology/
├── Classical Mechanics/
├── Consciousness/
├── Data and Programming/
├── Eletrodynamics/
├── General Relativity/
├── Masters Points of Interest/
├── Mathematics/
├── Optics/
├── Probability and Statistics/
├── Quantum Mechanics & Information/
└── Thermodynamics & Statistical Mechanics/
```

## GitHub Integration

The script generates download URLs following this pattern:
```
https://raw.githubusercontent.com/Corbanez97/library/main/Books%20and%20Papers/[Category]/[Filename].pdf
```

## Customization

You can modify the script to:
- Change the GitHub repository URL
- Modify the HTML styling
- Add additional file metadata
- Change the output filename

## Example Output

The generated HTML includes:
- Beautiful gradient background
- Card-based layout for each file
- Hover effects and animations
- File size and category information
- Download buttons for each PDF
- Responsive design for mobile devices

## Troubleshooting

- **No files found**: Make sure you're running the script from the directory containing "Books and Papers"
- **Encoding issues**: The script uses UTF-8 encoding for international characters
- **Path issues**: The script handles Windows and Unix path separators automatically
