#!/usr/bin/env python3

import json
import urllib.request
import argparse
from vtt_to_srt.__main__ import vtt_to_srt
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("url", metavar='URL', help="content URL")
args = parser.parse_args()

content_url = args.url
json_api_url = "http://api.rtvslo.si/ava/getRecording/{0}?client_id=82013fb3a531d5414f478747c1aca622"

content_id = content_url.split('/')[-1]
content_api_url = json_api_url.format(content_id)


raw_json_data = urllib.request.urlopen(content_api_url).read().decode()
json_data = json.loads(raw_json_data)

print("Video:")
for media_file in json_data['response']['mediaFiles']:
    resolution_width = media_file['width']
    resolution_height = media_file['height']
    streamer_url = media_file['streamers']['http']
    filename = media_file['filename']

    print("\tURL:\t\t{0}/{1}".format(streamer_url, filename))
    print("\tresolution:\t{0}x{1}".format(resolution_width, resolution_height))


# Subtitle output
if "subtitles" in json_data['response']:
    subtitles_url = json_data['response']['subtitles'][0]['file']
    subtitles_language = json_data['response']['subtitles'][0]['language']
    
    print("Subtitles:")
    print("\tURL:\t\t{0}".format(subtitles_url, subtitles_language))
    print("\tlanguage:\t{0}\n".format(subtitles_language))

    user_input = input("Do you want to download and convert vtt subtitles to srt? (yes/no)").lower()
    if user_input[0] == 'y':
        subtitles_filename_vtt = subtitles_url.split('/')[-1]
        pathlib.Path("subtitles").mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(subtitles_url, 'subtitles/' + subtitles_filename_vtt)
        vtt_to_srt('subtitles/' + subtitles_filename_vtt)
        print("Subtitles downloaded to {0}/subtitles".format(pathlib.Path().absolute()))
        print("Done.")
    else:
        print("Exiting.")

exit(0)
