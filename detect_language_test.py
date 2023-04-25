
from langdetect import detect
from langdetect import detect_langs
from langdetect import DetectorFactory
import fasttext
import csv
import json
import pandas as pd

DetectorFactory.seed = 0
fast_text_model = fasttext.load_model('lid.176.ftz')

lyrics = open("lyrics2.txt", "r")

to_remove_song = list()
to_remove_track_id = list()
languages = list()

while (True):
    line = lyrics.readline()
    if not line:
        break

    json_object = json.loads(line)
    track_id = json_object["track_id"]
    song = json_object["song"]
    lyrics_string = json_object["lyrics"]
    prob = 0
    try:
        language = detect(lyrics_string[0])
        prob = 1

        # detect_langs_val = detect_langs(lyrics_string[0])[0]
        # detect_langs_val = str(detect_langs_val).split(":")
        # language = detect_langs_val[0]
        # prob = float(detect_langs_val[1])

        # language = fast_text_model.predict(lyrics_string[0], k=1)[0][0]
        # prob = float(fast_text_model.predict(lyrics_string[0], k=1)[1][0])
    except:
        to_remove_song.append(song)
        to_remove_track_id.append(track_id)
        continue

    if language != "en" or prob < 0.9:
        to_remove_song.append(song)
        to_remove_track_id.append(track_id)
    languages.append(language)

index = pd.Index(languages)
print(index.value_counts())
print(to_remove_track_id)
print(len(to_remove_track_id))
lyrics.close()

    # try:
    #     language = detect(lyrics_string)
    # except:
    #     continue
    # if language != "en":
    #     print(language)
    #     print(lyrics_string)