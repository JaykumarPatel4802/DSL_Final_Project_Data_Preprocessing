import lyricsgenius
import json
import csv
from unidecode import unidecode

lyrics_file = open("lyrics2.txt", "a+")
# genius = lyricsgenius.Genius("x_CF3VynuaQGF8gtouHsnKfCdxi53mpbm8l9Shw5eb26VJHqCtA8VqFraMVHFyid")
genius = lyricsgenius.Genius('x_CF3VynuaQGF8gtouHsnKfCdxi53mpbm8l9Shw5eb26VJHqCtA8VqFraMVHFyid', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True, timeout = 60)

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

with open("sampled_dataset.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    
    for row in reader:
        count = count + 1
        
        if count < 3000:
            continue
        if count == 10100:
            break

        if count % 100 == 0:
            print("Done with " + str(count) + " songs")

        song_name = row['track_name']
        artist_name = row['artists']
        track_id = row['track_id']
        try:
            song = genius.search_song(song_name, artist_name)
        except:
            json_object = json.dumps({"track_id": {track_id}, "song": {song_name}, "artist": {artist_name}, "lyrics": "NAN"}, default=set_default)
            lyrics_file.write(json_object + "\n")
            continue
        if song is None:
            json_object = json.dumps({"track_id": {track_id}, "song": {song_name}, "artist": {artist_name}, "lyrics": "NAN"}, default=set_default)
            lyrics_file.write(json_object + "\n")
            continue
        original_lyrics = song.lyrics
        lyrics = original_lyrics.split('\n')[1:]
        newLyrics = list()
        for i in lyrics:
            if i != "" and i[0] != "[" and i[len(i) - 1] != "]":
                newLyrics.append(i)
        newLyrics = " ".join(newLyrics)
        clean_lyrics = unidecode(newLyrics)

        json_object = json.dumps({"track_id": {track_id}, "song": {song_name}, "artist": {artist_name}, "lyrics": {clean_lyrics}}, default=set_default)

        lyrics_file.write(json_object + "\n")
    
    print("Done with " + str(count) + " songs")

lyrics_file.close()


# song_name = "I knew you were trouble"
# artist_name = "Taylor Swift"

# song = genius.search_song(song_name, artist_name)

# original_lyrics = song.lyrics
# lyrics = original_lyrics.split('\n')[1:]
# newLyrics = list()
# for i in lyrics:
#     if i != "" and i[0] != "[" and i[len(i) - 1] != "]":
#         newLyrics.append(i)

# newLyrics = " ".join(newLyrics)
# newLyrics = newLyrics + "\n"
# # print(original_lyrics)
# # print('----------------')
# # print(newLyrics)

# def set_default(obj):
#     if isinstance(obj, set):
#         return list(obj)
#     raise TypeError

# json_object = json.dumps({"song": {song_name}, "artist": {artist_name}, "lyrics": {newLyrics}}, default=set_default)

# lyrics_file.write(json_object)

# lyrics_file.close()