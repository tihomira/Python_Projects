from bs4 import BeautifulSoup
import re
import json
import os

# Specify the path to your HTML files folder
html_folder_path = '/Users/tihomiranikolova/Documents/Python_projects/Python_projects_git/Python_Projects/BaanboardSearchBar/website'

# Initialize an empty list to store all data from different HTML files
all_data = []

# Iterate over HTML files in the folder
for filename in os.listdir(html_folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(html_folder_path, filename)

        # Read the HTML content from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract information from <li> elements
        data = []
        for li_tag in soup.find_all('li'):
            # Check if the <li> tag has an <a> tag with an 'href' attribute
            a_tag = li_tag.a
            if a_tag and 'href' in a_tag.attrs:
                # Extract title, file, and replies information
                title = a_tag.get_text(strip=True)
                file = a_tag['href'].replace("https://10.40.2.105/", "")
                replies_match = re.search(r'\((\d+)\sreplies\)', str(li_tag))
                replies = int(replies_match.group(1)) if replies_match else None

                # Append data to the list
                data.append({
                    'title': title,
                    'file': file,
                    'replies': replies
                })

        # Append data from the current HTML file to the overall data list
        all_data.extend(data)

# Save all data to a single JSON file
output_file_path = os.path.join(html_folder_path, 'data4.json')
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=2)

print(f'All data saved to {output_file_path}')
print('Data has been successfully extracted and stored in a single JSON file.')
