#!/usr/bin/env python3

import json
import urllib.request
import argparse
from vtt_to_srt.__main__ import vtt_to_srt
import pathlib


# https://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)


parser = argparse.ArgumentParser()
parser.add_argument("url", metavar='URL', help="content URL")
args = parser.parse_args()

content_url = args.url

# API URL sourced from @Randomness: https://slo-tech.com/forum/t598506/p6736691#p6736691
json_api_url = "https://api.rtvslo.si/ava/getMedia/{0}?client_id={1}"
json_api_client_id = "82013fb3a531d5414f478747c1aca622&jwt=qYRYxFVkMT9blEBOr28QzoIxOfRrb5U_r7dS6L_rqos"

content_id = content_url.split('/')[-1]
content_api_url = json_api_url.format(content_id, json_api_client_id)


raw_json_data = urllib.request.urlopen(content_api_url).read().decode()
json_data = json.loads(raw_json_data)

print("Video:")
for media_file in json_data['response']['mediaFiles']:
    resolution_width = media_file['width']
    resolution_height = media_file['height']
    streamer_url = media_file['streams']['http']
    #filename = media_file['filename']
    filesize = media_file['filesize']

    print("\tURL:\t\t{0}".format(streamer_url))
    print("\tresolution:\t{0}x{1}".format(resolution_width, resolution_height))
    print("\tfile size:\t{0}".format(sizeof_fmt(filesize)))


# Subtitle output
json_api_subtitle_url = "http://api.rtvslo.si/ava/getRecording/{0}?client_id=82013fb3a531d5414f478747c1aca622"
content_subtitle_api_url = json_api_subtitle_url.format(content_id)
raw_json_subtitle_data = urllib.request.urlopen(content_subtitle_api_url).read().decode()
json_subtitle_data = json.loads(raw_json_subtitle_data)

if "subtitles" in json_subtitle_data['response']:
    subtitles_url = json_subtitle_data['response']['subtitles'][0]['file']
    subtitles_language = json_subtitle_data['response']['subtitles'][0]['language']
    
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
