import os
import openai
import json

openai_key = "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"
openai.api_key = os.environ.get("OPENAI_API_KEY", openai_key)

combined_lyrics2 = open("combined_final.txt", "a+")

# lyric2 = "Oh, here it comes That funny feeling again Winding me up inside Every time we touch Hey, I don't know Oh, tell me where to begin 'Cause I never ever Felt so much Hey And I can't recall Any love at all Oh, baby, this blows 'em all away It's got what it takes So tell me why can't this be love? Straight from my heart Oh, tell me why can't this be love? I tell myself Hey, only fools rush in Only time will tell if we stand the test of time All I know You've got to run to win And I'll be damned if I'll get Hung up on the line, hey No, I can't recall Anything at all Ah, baby, this blows 'em all away Woo You might also like It's got what it takes So tell me why can't this be love? You want it straight from the heart Oh, tell me why can't this be love? Woo, it's got what it takes So tell me why can't this be love? Straight from the heart Tell me why can't this be love? Baby, why can't this be love? Got to know why can't this be love? I wanna know why can't this be love?3Embed"
# # lyric = "Once upon a time, a few mistakes ago I was in your sights, you got me alone You found me, you found me You found me-e-e-e-e I guess you didn't care and I guess I liked that And when I fell hard, you took a step back Without me, without me Without me-e-e-e-e And he's long gone when he's next to me And I realize the blame is on me 'Cause I knew you were trouble when you walked in So shame on me now Flew me to places I'd never been 'Til you put me down, oh I knew you were trouble when you walked in So shame on me now Flew me to places I'd never been Now I'm lying on the cold hard ground Oh, oh Trouble, trouble, trouble Oh, oh Trouble, trouble, trouble No apologies, he'll never see you cry Pretends he doesn't know that he's the reason why You're drowning, you're drowning You're drowning-ing-ing-ing-ing And I heard you moved on from whispers on the street A new notch in your belt is all I'll ever be And now I see, now I see Now I see-e-e-e-e He was long gone when he met me And I realize the joke is on me, hey I knew you were trouble when you walked in (Oh) So shame on me now Flew me to places I'd never been 'Til you put me down, oh I knew you were trouble when you walked in So shame on me now Flew me to places I'd never been (Yeah) Now I'm lying on the cold hard ground Oh, oh (Yeah) Trouble, trouble, trouble (Trouble) Oh, oh Trouble, trouble, trouble And the saddest fear Comes creeping in That you never loved me or her Or anyone, or anything, yeah. I knew you were trouble when you walked in So shame on me now Flew me to places I'd never been (Never been) 'Til you put me down, oh I knew you were trouble when you walked in (Knew it right there) So shame on me now (Knew it right there) Flew me to places I'd never been (Ooh) Now I'm lying on the cold hard ground Oh, oh Trouble, trouble, trouble (Oh) Oh, oh Trouble, trouble, trouble (Trouble) 'Cause I knew you were trouble when you walked in Trouble, trouble, trouble 'Cause I knew you were trouble when you walked in Trouble, trouble, troubleEmbed"
# # lyric = "HiEmbed"
# prompt_prefix = "Given the following, generate a really short summary without including the song name or the artist name in the summary: "
prompt_prefix = "Given the following, generate a 2-4 sentence summary without including the song name or the artist name in the summary: "
# prompt = prompt_prefix + lyric2

combined_lyrics = open("combined.txt", "r")


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# count = 0

while (True):
    line = combined_lyrics.readline()
    if not line:
        break

    # count += 1

    json_object = json.loads(line)
    track_id = json_object["track_id"][0]
    lyric = json_object["lyrics"][0]
    song = json_object["song"][0]
    artist = json_object["artist"][0]
    summary = json_object["summary"][0]

    # if (count < 101) or (summary == "NAN"):
    #     continue

    if (summary == "NAN"):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt_prefix},
                    {"role": "user", "content": lyric}
                ],
                stop=["Embed"],
                temperature=0.25,
                frequency_penalty=0.5,
                presence_penalty=0.5)
            
            summary = response["choices"][0]["message"]["content"]

            json_string = json.dumps({"track_id": {track_id}, "song": {song}, "artist": {artist}, "summary": {summary}, "lyrics": {lyric}}, default=set_default)
            combined_lyrics2.write(json_string + "\n")
        except:
            # json_string = json.dumps({"track_id": {track_id}, "song": {song}, "artist": {artist}, "summary": "NAN", "lyrics": {lyric}}, default=set_default)
            combined_lyrics2.write("\n")
    else:
        combined_lyrics2.write(line)

combined_lyrics2.close()
combined_lyrics.close()