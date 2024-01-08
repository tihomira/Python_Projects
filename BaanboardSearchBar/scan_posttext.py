from bs4 import BeautifulSoup
import json
import os
import shlex

# Specify the path to your HTML files folder
folder_path = '/Users/tihomiranikolova/Documents/Python_projects/Python_projects_git/Python_Projects/BaanboardSearchBar/website'

# Escape special characters in the file path (original structure kept)
html_folder_path = shlex.quote(folder_path)

# Initialize an empty list to store all data from different HTML files
all_data = []

# Iterate over HTML files in the folder
for filename in os.listdir(html_folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(html_folder_path,filename)

        # Read the HTML content from the file
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all occurrences of the 'posttext' div tag
        posttext_tags = soup.find_all('div', class_='posttext')

        # Initialize posttexts for the current file
        posttexts = []

        # Iterate over all found 'posttext' tags in the current HTML file
        for posttext_tag in posttext_tags:
            # Extract the text content of the 'posttext' tag
            posttext_content = posttext_tag.get_text(strip=True).lower()

            # Append posttext to the list
            posttexts.append(posttext_content)

        # Join posttexts with "=|=|=" separator
        posttexts_joined = " =|=|= ".join(posttexts)

        # Append data to the list
        all_data.append({
            'file': filename,
            'posttext': posttexts_joined
            })
        
        # Print a message if no 'posttext' tags were found in the current file
        if not posttext_tags:
            print(f'No posttext tags found in file: {filename}')


# Save all data to a single JSON file
output_file_path = os.path.join(html_folder_path, 'data_posttext.json')
with open(output_file_path, 'w', encoding='utf-8', errors='replace') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=2)

print(f'All data saved to {output_file_path}')
print('Data has been successfully extracted and stored in a single JSON file.')
