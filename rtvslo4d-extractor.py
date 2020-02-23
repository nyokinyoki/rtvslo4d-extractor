#!/usr/bin/env python3

import json
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", metavar='URL', help="content URL")
args = parser.parse_args()

content_url = args.url
json_api_url = "http://api.rtvslo.si/ava/getRecording/{0}?client_id=82013fb3a531d5414f478747c1aca622"

content_id = content_url.split('/')[-1]
content_api_url = json_api_url.format(content_id)


raw_json_data = urllib.request.urlopen(content_api_url).read().decode()
# Parse raw json data to object
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
    subtitles = json_data['response']['subtitles'][0]['file']
    subtitles_language = json_data['response']['subtitles'][0]['language']
    
    print("Subtitles:")
    print("\tURL:\t\t{0}".format(subtitles, subtitles_language))
    print("\tlanguage:\t{0}".format(subtitles_language))

exit(0)
