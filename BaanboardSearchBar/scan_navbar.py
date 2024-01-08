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

        # Extracting category and subcategory from the div with id "navbar"
        navbar_div = soup.find('div', {'id': 'navbar'})

        if navbar_div:
            # Find all anchor tags inside the navbar_div
            anchor_tags = navbar_div.find_all('a')[-2:]

            if len(anchor_tags) == 2:
                category = anchor_tags[0].get_text(strip=True)
                subcategory = anchor_tags[1].get_text(strip=True)
                
                # Append data to the list
                all_data.append({
                    'file': filename,
                    'category': category,
                    'subcategory': subcategory
                })
            # Extract category if there is only one anchor tag
            elif len(anchor_tags) == 1:
                category = anchor_tags[0].get_text(strip=True)
                
                # Append data to the list
                all_data.append({
                    'file': filename,
                    'category': category,
                    'subcategory': None
                })
            else:
                # Append data to the list if there are no anchor tags
                all_data.append({
                    'file': filename,
                    'category': None,
                    'subcategory': None
                    })
                
                print(f'No navbar div found in file: {filename}')


# Save all data to a single JSON file
output_file_path = os.path.join(html_folder_path, 'data_navbar.json')
with open(output_file_path, 'w', encoding='utf-8', errors='replace') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=2)

print(f'All data saved to {output_file_path}')
print('Data has been successfully extracted and stored in a single JSON file.')
