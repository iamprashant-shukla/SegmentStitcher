import requests
import os

# Base URL for the segments
base_url = '#'

# Directory to save the .ts files
save_dir = 'video_segments'
os.makedirs(save_dir, exist_ok=True)

# Start from the first segment
segment_num = 1

while True:
    try:
        segment_url = f"{base_url}{segment_num}-v1-a1.ts"
        response = requests.get(segment_url)
        
        # If the segment is not found, break the loop
        if response.status_code != 200:
            print(f"Segment {segment_num} not found. Stopping download.")
            break
        
        segment_path = os.path.join(save_dir, f"segment{segment_num}.ts")
        with open(segment_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded segment {segment_num}")
        segment_num += 1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Combining all segments into one file using ffmpeg
with open('filelist.txt', 'w') as f:
    for i in range(1, segment_num):
        f.write(f"file '{save_dir}/segment{i}.ts'\n")

# Using ffmpeg to concatenate
os.system("ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4")

print("Video compiled as output.mp4")
