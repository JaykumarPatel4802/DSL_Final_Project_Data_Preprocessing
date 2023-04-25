# combine the files summaries.py and filtered_lyrics.py

import json

summaries = open("summaries.txt", "r")
lyrics = open("filtered_lyrics2.txt", "r")
combined = open("combined.txt", "a+")
count = 0


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

for summary, lyric in zip(summaries, lyrics):
    count += 1

    json_summary = json.loads(summary)
    summary_track_id = json_summary["track_id"][0]
    summaries_summary = json_summary["summary"]
    if (type(summaries_summary) == list):
        summaries_summary = summaries_summary[0]

    if count > 101:
        summary_song = json_summary["song"][0]
        summary_artist = json_summary["artist"][0]
    else:
        summary_song = "NAN"
        summary_artist = "NAN"
    
    json_lyric = json.loads(lyric)
    lyric_track_id = json_lyric["track_id"][0]
    lyric_song = json_lyric["song"][0]
    lyric_artist = json_lyric["artist"][0]
    lyrics_lyric = json_lyric["lyrics"][0]


    if summary_track_id != lyric_track_id:
        print("ERROR1")
        break
    if count > 101:
        if summary_song != lyric_song:
            print("ERROR2")
            break
        if summary_artist != lyric_artist:
            print("ERROR3")
            break
    
    json_string = json.dumps({"track_id": {summary_track_id}, "song": {lyric_song}, "artist": {lyric_artist}, "summary": {summaries_summary}, "lyrics": {lyrics_lyric}}, default=set_default)
    combined.write(json_string + "\n")

summaries.close()
lyrics.close()
combined.close()
