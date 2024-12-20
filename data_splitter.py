import os

def split_file(input_file, num_chunks):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    chunk_size = len(lines) // num_chunks
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
    
    for idx, chunk in enumerate(chunks):
        with open(f"chunk_{idx}.txt", 'w') as out_file:
            out_file.writelines(chunk)

if __name__ == "__main__":
    input_file = "large_text.txt"
    num_chunks = 4
    split_file(input_file, num_chunks)