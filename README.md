# rtvslo4d-extractor
Extracts video and or subtitle URL's from 4d.rtvslo.si

## Requirements
Python 3 interpreter.

## Usage
```bash
git clone https://github.com/nyokinyoki/rtvslo4d-extractor.git
cd rtvslo4d-extractor
chmod +x rtvslo4d-extractor.py
./rtvslo4d-extractor.py https://4d.rtvslo.si/arhiv/ljudje-in-zemlja/174673802
```

### Example output
```bash
:~/rtvslo4d-extractor$ ./rtvslo4d-extractor.py https://4d.rtvslo.si/arhiv/ljudje-in-zemlja/174673802
Video:
        URL:            https://videoweb2.rtvslo.si/ava_archive01//2020/02/23/Ljudje_in_zemlja2020-02-23-010210-SLO1.mp4
        resolution:     640x360
        URL:            https://videoweb2.rtvslo.si/ava_archive01//2020/02/23/Ljudje_in_zemlja2020-02-23-010210-SLO1_1.mp4
        resolution:     1280x720
Subtitles:
        URL:            https://img.rtvslo.si/_up/ava/ava_misc/subs/2020/02/23/02-23-2020-liz.vtt
        language:       sl
```