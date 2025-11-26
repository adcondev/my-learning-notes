import re

def convert_html_to_md(html_file, md_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the table body
    table_match = re.search(r'<table xmlns="" class="grid">(.*?)</table>', content, re.DOTALL)
    if not table_match:
        print("Table not found")
        return

    table_content = table_match.group(1)
    
    # Extract headers
    headers = []
    header_match = re.search(r'<thead>(.*?)</thead>', table_content, re.DOTALL)
    if header_match:
        header_row = header_match.group(1)
        # Simple regex to find content inside th > div > div or just th
        # Based on the file content: <th><div><div>Command</div></div></th>
        headers = re.findall(r'<th>\s*<div>\s*<div>(.*?)</div>\s*</div>\s*</th>', header_row, re.DOTALL)
    
    if not headers:
        # Fallback if structure is slightly different or just to be safe
        headers = ["Command", "Description", "Category"]

    md_lines = []
    md_lines.append("| " + " | ".join(headers) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    # Extract rows
    body_match = re.search(r'<tbody>(.*?)</tbody>', table_content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        rows = re.findall(r'<tr>(.*?)</tr>', body_content, re.DOTALL)
        
        for row in rows:
            cols = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
            clean_cols = []
            for col in cols:
                # Check for links
                link_match = re.search(r'<a href="(.*?)">(.*?)</a>', col, re.DOTALL)
                if link_match:
                    href = link_match.group(1)
                    text = link_match.group(2).strip()
                    # Remove newlines and extra spaces from text
                    text = re.sub(r'\s+', ' ', text)
                    clean_cols.append(f"[{text}](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/{href})")
                else:
                    # Just text
                    text = re.sub(r'<.*?>', '', col) # Remove other tags if any
                    text = re.sub(r'\s+', ' ', text).strip()
                    clean_cols.append(text)
            
            if clean_cols:
                md_lines.append("| " + " | ".join(clean_cols) + " |")

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))
    
    print(f"Successfully created {md_file}")

if __name__ == "__main__":
    convert_html_to_md('escpos_commands.html', 'escpos_commands.md')
