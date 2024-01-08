import json

# Read the contents of the first file
with open('website/data_title_links_replies.json', 'r') as file1:
    data1 = json.load(file1)

# Read the contents of the second file
with open('website/data_posttext.json', 'r') as file2:
    data2 = json.load(file2)

# Read the contents of the third file
with open('website/data_navbar.json', 'r') as file3:
    data3 = json.load(file3)

# Create a dictionary to store the merged data
merged_data_dict = {}

# Perform left join on the 'file' key for data1
for entry in data1:
    file_key = entry.get("file")
    # Create a dictionary for each file with initial values
    merged_data_dict[file_key] = {
        "title": entry.get("title", ""),
        "file": entry.get("file", ""),
        "replies": entry.get("replies", ""),
        "category": None,
        "subcategory": None,
        "posttext": None
    }
    print(f'all {merged_data_dict[file_key]}')

# Update 'posttext' value for existing files in merged_data_dict using data2
for entry in data2:
    file_key = entry.get("file")
    if file_key in merged_data_dict:
        merged_data_dict[file_key]["posttext"] = entry.get("posttext", None)
        print(f'posttext{merged_data_dict[file_key]}')

# Update 'category' and 'subcategory' values for existing files in merged_data_dict using data3
for entry in data3:
    file_key = entry.get("file")
    if file_key in merged_data_dict:
        merged_data_dict[file_key]["category"] = entry.get("category", None)
        merged_data_dict[file_key]["subcategory"] = entry.get("subcategory", None)
        print(f'category and subcategory{merged_data_dict[file_key]}')



# Convert the merged dictionary values to a list
merged_data_list = list(merged_data_dict.values())

# Write the merged data to a new file
with open('merged_data.json', 'w',errors='replace') as merged_file:
    json.dump(merged_data_list, merged_file, indent=2)

print("Merged data written to merged_data.json")