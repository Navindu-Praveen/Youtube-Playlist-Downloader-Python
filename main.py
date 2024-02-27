from pytube import Playlist


def download_playlist(playlist_url, output_path='./downloads'):
    playlist = Playlist(playlist_url)
    playlist_title = playlist.title  # Fix: Remove parentheses

    print(f'Downloading playlist: {playlist_title}')

    for video in playlist.videos:
        print(f'Downloading video: {video.title}')
        video.streams.get_highest_resolution().download(output_path)

    print('Download complete!')


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    download_playlist(playlist_url)
