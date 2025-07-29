# PyVideoDownloader

A simple command-line tool for downloading YouTube videos and playlists with customizable options.

## Legal Disclaimer

**This tool is created as an educational hobby project for learning purposes only.**

- This project is **NOT** intended for copyright infringement or content piracy
- Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws
- Only download content you have permission to download or content that is in the public domain
- Respect content creators' rights and consider supporting them through official channels
- This tool is for personal, educational, and non-commercial use only
- The author assumes no responsibility for misuse of this software

**Please use this tool responsibly and ethically.**

## Important

I will export this project as an app in future. For now you need to type commands below in the same directory as source code.

## Features

- Download individual YouTube videos
- Download entire YouTube playlists
- Audio-only download option (m4a format)
- Multiple resolution options (360p, 480p, 720p, 1080p)
- Progress tracking during downloads
- Custom output path support

## Installation

This project uses `uv` for dependency management. Make sure you have Python 3.13+ installed.

1. Clone the repository:

```bash
git clone https://github.com/Leopoldmiszcz/PyVideoDownloader.git
cd PyVideoDownloader
```

2. Install dependencies using uv:

```bash
uv sync
```

## Usage

The tool provides two main commands: `video` for downloading individual videos and `playlist` for downloading entire playlists.

### Basic Usage

```bash
python main.py --help
```

### Download a Single Video

```bash
python main.py video <youtube_url> [output_path]
```

**Examples:**

```bash
# Download video to current directory in 1080p (default)
python main.py video "https://www.youtube.com/watch?v=VIDEO_ID"

# Download video to specific directory
python main.py video "https://www.youtube.com/watch?v=VIDEO_ID" "/path/to/downloads"

# Download video in 720p resolution
python main.py video "https://www.youtube.com/watch?v=VIDEO_ID" -r 720p

# Download only audio
python main.py video "https://www.youtube.com/watch?v=VIDEO_ID" -ao True
```

### Download a Playlist

```bash
python main.py playlist <youtube_playlist_url> [output_path]
```

**Examples:**

```bash
# Download entire playlist to current directory
python main.py playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Download playlist to specific directory in 480p
python main.py playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" "/path/to/downloads" -r 480p

# Download playlist audio only
python main.py playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" -ao True
```

## Command Options

### Video Command

```bash
python main.py video --help
```

**Arguments:**

- `url` (required): YouTube video URL
- `path` (optional): Output directory path

**Options:**

- `--audio_only, -ao`: Download only audio in m4a format (default: False)
- `--resolution, -r`: Video resolution - choices: 360p, 480p, 720p, 1080p (default: 1080p)

### Playlist Command

```bash
python main.py playlist --help
```

**Arguments:**

- `url` (required): YouTube playlist URL
- `path` (optional): Output directory path

**Options:**

- `--audio_only, -ao`: Download only audio in m4a format (default: False)
- `--resolution, -r`: Video resolution - choices: 360p, 480p, 720p, 1080p (default: 1080p)

## Available Resolutions

- **360p**: Standard definition
- **480p**: Enhanced definition
- **720p**: High definition (HD)
- **1080p**: Full high definition (Full HD) - _default_

_Note: The tool cannot upscale videos. If the requested resolution is not available for a video, an error message will be displayed._

## Dependencies

- **[click](https://click.palletsprojects.com/)**: For creating the command-line interface
- **[pytubefix](https://github.com/JuanBindez/pytubefix)**: For YouTube video downloading functionality

## Error Handling

The tool includes built-in error handling for common scenarios:

- **Video not available**: If a video cannot be downloaded at the specified resolution
- **Audio not available**: If audio-only download is requested but not available
- **Invalid URLs**: The tool will display appropriate error messages for invalid YouTube URLs

## Progress Tracking

Downloads include real-time progress tracking, showing the download status as files are being retrieved.

## File Formats

- **Video downloads**: MP4 format
- **Audio-only downloads**: M4A format

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

### Common Issues

1. **"Video is not available"**: The requested resolution might not be supported for that specific video. Try a lower resolution.

2. **"Video audio is not available"**: Some videos might not have extractable audio. Try downloading the full video instead.

3. **Permission errors**: Make sure you have write permissions to the output directory.

### Getting Help

Use the `--help` flag with any command to see detailed usage information:

```bash
python main.py --help
python main.py video --help
python main.py playlist --help
```

## Examples

### Download a single video in different scenarios:

```bash
# High quality video download
python main.py video "https://www.youtube.com/watch?v=dQw4w9WgXcQ" ~/Downloads -r 1080p

# Audio-only download for music
python main.py video "https://www.youtube.com/watch?v=dQw4w9WgXcQ" ~/Music -ao True

# Lower quality for faster download
python main.py video "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -r 480p
```

### Download an entire playlist:

```bash
# Download educational playlist
python main.py playlist "https://www.youtube.com/playlist?list=PLExample123" ~/Education

# Download music playlist as audio only
python main.py playlist "https://www.youtube.com/playlist?list=PLMusic456" ~/Music -ao True
```
