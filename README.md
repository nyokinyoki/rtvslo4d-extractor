# rtvslo4d-extractor
Extracts video and subtitle URL's from [4d.rtvslo.si](https://4d.rtvslo.si/). Optionally, it can also download vtt subtitles and convert them to srt format by using [vtt_to_srt library](https://github.com/0um/vtt-to-srt.py).

## Requirements
Python 3 interpreter.

## Usage
```bash
git clone https://github.com/nyokinyoki/rtvslo4d-extractor.git
cd rtvslo4d-extractor
chmod +x rtvslo4d-extractor.py
./rtvslo4d-extractor.py https://4d.rtvslo.si/arhiv/v-imenu-ljudstva/174673680
```

### Example output
```bash
:~/rtvslo4d-extractor$ ./rtvslo4d-extractor.py https://4d.rtvslo.si/arhiv/v-imenu-ljudstva/174673680
Video:
        URL:            https://videoweb2.rtvslo.si/ava_archive01/2020/02/22/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1_0.mp4
        resolution:     1280x720
        URL:            https://videoweb2.rtvslo.si/ava_archive01/2020/02/22/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1_1.mp4
        resolution:     640x360
Subtitles:
        URL:            https://img.rtvslo.si/_up/ava/ava_misc/subs/2020/02/23/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1.vtt
        language:       sl

Do you want to download and convert vtt subtitles to srt? (yes/no)y
file being read: subtitles/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1.vtt

subtitles/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1.srt
file created: subtitles/IGR-VIMENULJUDSTVA-20200129-004--LP-SLO--A1A2-O1-F1.srt

Subtitles downloaded to /home/istok/rtvslo4d-extractor/subtitles
Done.
```