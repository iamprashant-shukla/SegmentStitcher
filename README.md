## SegmentStitcher
SegmentStitcher is a Python script that downloads video segments from a given base URL, saves them as '.ts' files, and compiles them into a single video file using FFmpeg. This tool is particularly useful for reconstructing videos from segmented streams.
## Features

- Automatic Downloading: Continuously downloads segments from a specified base URL until all segments are retrieved.
- Error Handling: Stops downloading if a segment is not found or an error occurs.
- Segment Compilation: Combines all downloaded .ts segments into a single .mp4 video file.
- Simple Configuration: Minimal setup required with easy-to-modify parameters.

## System Requirements
- Python 3.x
- requests library: Install it using pip install requests
- FFmpeg: Ensure FFmpeg is installed and added to your system's PATH.
## Installation

Clone the Repository:

```bash
git clone https://github.com/yourusername/SegmentStitcher.git
cd SegmentStitcher
```
Install the Required Python Package:
```bash
pip install requests
```
Ensure FFmpeg is Installed:
```bash
Verify that FFmpeg is installed by running ffmpeg -version in your terminal. If not installed, download it from here and add it to your PATH.
```
## Contributing

Contributions are welcome. To contribute:

- Fork the repository.
- Create a new branch for your feature or fix.
- Commit your changes with descriptive messages.
- Open a pull request with a detailed description of the changes.

## Usage
Update the Base URL:

- Open segment_stitcher.py in your preferred text editor.
- Update the base_url variable with the base URL of your video segments.
```javascript
base_url = 'https://example.com/path/to/segments/seg-'
```
Run the Script:
- Run the script to start downloading segments and compiling them into a video
```javascript
python segment_stitcher.py
```
Check the Output:
- The downloaded .ts segments will be stored in the video_segments directory.
- The final compiled video will be saved as output.mp4 in the same directory as the script.



## Acknowledgements

 - [FFmpeg](https://www.ffmpeg.org/)
 - [requests](https://pypi.org/project/requests/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

