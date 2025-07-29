import click
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress


RESOLUTIONS = ["360p", "480p", "720p", "1080p"]


@click.command()
@click.argument("url", type=str)
@click.argument("path", type=click.Path(exists=False), required=0)
@click.option(
    "--audio_only",
    "-ao",
    default=False,
    required=0,
    help="If set to True (-ao True), will download only audio from video in m4a format.",
)
@click.option(
    "--resolution",
    "-r",
    type=click.Choice(RESOLUTIONS),
    default="1080p",
    help="Used to change resolution in downloaded video, it can't upscale video. Set by default to 1080p.",
)
def video(url, path, audio_only, resolution):
    """Command that is used to download an Youtube video from given URL. Use video --help for more information."""
    yt = YouTube(url, on_progress_callback=on_progress)

    if audio_only == True:
        ys = yt.streams.get_audio_only()
        if ys:
            click.echo(f"Downloading audio for {ys.title}")
            ys.download()
        else:
            click.echo(f"Video audio is not available.")
    else:
        ys = yt.streams.filter(res=resolution, file_extension="mp4").first()
        if ys:
            click.echo(f"Downloading {yt.title}")
            ys.download(output_path=path)
        else:
            click.echo(
                f"Video is not available. Check if {resolution} is supported in this youtube video."
            )


@click.command()
@click.argument("url", type=str)
@click.argument("path", type=click.Path(exists=False), required=0)
@click.option(
    "--audio_only",
    "-ao",
    default=False,
    required=0,
    help="If set to True (-ao True), will download only audio from video in m4a format.",
)
@click.option(
    "--resolution",
    "-r",
    type=click.Choice(RESOLUTIONS),
    default="1080p",
    help="Used to change resolution in downloaded video, it can't upscale video. Set by default to 1080p.",
)
def playlist(url, path, audio_only, resolution):
    """Command that is used to download an Youtube playlist form given URL. Use playlist --help for more information."""
    pl = Playlist(url)
    if audio_only == True:
        for video in pl.videos:
            ys = video.streams.get_audio_only()
            if ys:
                click.echo(f"Downloading audio for {video.title}.")
                ys.download(output_path=path)
            else:
                click.echo(f"Video {video.title} audio is not available.")
    else:
        for video in pl.videos:
            ys = video.streams.filter(res=resolution, file_extension="mp4").first()
            if ys:
                ys.download(output_path=path)
            else:
                click.echo(
                    f"Video {video.title} is not available. Check if {resolution} is supported in this youtube video."
                )
