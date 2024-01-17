import json

def split_json(input_file, output_file, records_per_chunk):
	with open(input_file,'r', encoding='utf-8', errors='replace') as file:
		data = json.load(file)

	total_records = len(data)
	# Calculate the number of chunks
	num_chunks = (total_records + records_per_chunk - 1 )// records_per_chunk

	for i in range(num_chunks):
		start_index = i * records_per_chunk
		end_index = (i + 1) * records_per_chunk
		chunk_data = data[start_index:end_index]

		output_data = f"{output_file}_chunk_{i + 1}.json"
		with open(output_data, 'w',encoding='utf-8', errors='replace') as outfile:
			json.dump(chunk_data,outfile, indent=2)

		print(f"Chunk {i + 1} written to {output_data}")


input_file = 'merged_data_id.json'
output_file = 'mrg/mrg_data_id'
records_per_chunk = 10000 

split_json(input_file,output_file,records_per_chunk)
