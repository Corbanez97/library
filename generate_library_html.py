import os
import urllib.parse
from pathlib import Path


def get_file_size(file_path):
    """Get file size in human readable format"""
    size_bytes = os.path.getsize(file_path)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def generate_github_url(file_path, base_path):
    """Generate GitHub raw URL for a file"""
    # Convert Windows path to Unix-style path
    relative_path = os.path.relpath(file_path, base_path)
    relative_path = relative_path.replace('\\', '/')

    # URL encode the path components
    encoded_path = '/'.join(urllib.parse.quote(part)
                            for part in relative_path.split('/'))

    # Base GitHub raw URL
    base_url = "https://raw.githubusercontent.com/Corbanez97/library/main"

    return f"{base_url}/{encoded_path}"


def scan_directory(directory_path, base_path):
    """Recursively scan directory for PDF files"""
    files = []

    for root, dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, base_path)
                category = os.path.relpath(root, base_path)

                files.append({
                    'name': filename,
                    'path': file_path,
                    'category': category,
                    'size': get_file_size(file_path),
                    'github_url': generate_github_url(file_path, base_path)
                })

    return files


def generate_html(files):
    """Generate HTML content"""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library - Books and Papers</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            color: white;
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .stats {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            text-align: center;
            color: white;
        }
        
        .stats h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        
        .category {
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            margin-bottom: 30px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
        }
        
        .category-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .files-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 15px;
            padding: 20px;
        }
        
        .file-item {
            background: white;
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #e1e5e9;
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        
        .file-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            border-color: #667eea;
        }
        
        .file-name {
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 0.95rem;
            line-height: 1.4;
            word-wrap: break-word;
        }
        
        .file-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            font-size: 0.85rem;
            color: #7f8c8d;
        }
        
        .download-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .download-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        
        .download-btn:active {
            transform: translateY(0);
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            color: white;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            .files-grid {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Library</h1>
            <p>Books and Papers Collection</p>
        </div>
"""
    html_content += f"""
        <div class="stats">
            <h3>📊 Collection Statistics</h3>
            <p>Total Files: {len(files)} | Total Categories: {len(set(file_info['category'] for file_info in files))}</p>
        </div>
"""

    # Group files by category
    categories = {}
    for file_info in files:
        category = file_info['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(file_info)

    # Generate HTML for each category
    for category, category_files in sorted(categories.items()):
        html_content += f"""
        <div class="category">
            <div class="category-header">
                📁 {category}
            </div>
            <div class="files-grid">
"""

        for file_info in sorted(category_files, key=lambda x: x['name'].lower()):
            html_content += f"""
                <div class="file-item">
                    <div class="file-name">{file_info['name']}</div>
                    <div class="file-meta">
                        <span>📏 {file_info['size']}</span>
                        <span>📂 {file_info['category']}</span>
                    </div>
                    <a href="{file_info['github_url']}" class="download-btn" download>
                        ⬇️ Download PDF
                    </a>
                </div>
"""

        html_content += """
            </div>
        </div>
"""

    html_content += f"""
        <div class="footer">
            <p>Generated on {os.popen('date').read().strip() if os.name != 'nt' else 'Windows'}</p>
            <p>Total files: {len(files)}</p>
        </div>
    </div>
</body>
</html>"""

    return html_content


def main():
    """Main function"""
    # Get the current working directory
    current_dir = os.getcwd()
    books_papers_dir = os.path.join(current_dir, "Books and Papers")

    if not os.path.exists(books_papers_dir):
        print(
            f"Error: 'Books and Papers' directory not found in {current_dir}")
        return

    print("Scanning for PDF files...")
    files = scan_directory(books_papers_dir, current_dir)

    if not files:
        print("No PDF files found!")
        return

    print(f"Found {len(files)} PDF files")

    # Generate HTML content
    html_content = generate_html(files)

    # Write to file
    output_file = "docs/index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML file generated successfully: {output_file}")
    print(f"Total files: {len(files)}")

    # Show categories
    categories = set(file_info['category'] for file_info in files)
    print(f"Categories: {len(categories)}")
    for category in sorted(categories):
        category_files = [f for f in files if f['category'] == category]
        print(f"  {category}: {len(category_files)} files")


if __name__ == "__main__":
    main()
