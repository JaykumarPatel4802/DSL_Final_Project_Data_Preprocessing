import os
import openai
import json

openai_key = "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"
openai.api_key = os.environ.get("OPENAI_API_KEY", openai_key)


lyrics = "Where will you go when it's over? Who will you know when it's over? I know, yeah, I saw you, you know that, right? Just know that I saw you (I saw you, I saw, I saw) Where will you go when it's over? Do you get lost on your own? I know, yeah, I saw you, you know that, right? Just know that I saw you (I saw you, I saw, I saw) Late night, zip ties Make you wanna miss your flight Flipping through your feelings like a Gemini I'm staring at your dark sideSo far, so gone Standing with a white dress on Only say you need me when your friends gone home You're tryna get your mind right But if I only get one life, this is what I wanna do And if I only get one life, I wanna live it with you And if I only have one night, yeah, I'd spend it with you So if I only get one life, I wanna live it with you I’m gonna live it with you Say something like (It's only you) It's only you New wave, riptideHoping I can change your life If you need a second chance, you can take mine See you in a new light (See you in a new—) Skintight, cocaine You don't wanna feel this way You know I'd do anything to make you stay I'm pulling out my best lines But if I only get one life, this is what I wanna do And if I only get one life, I wanna live it with you And if I only have one night, yeah, I'd spend it with you So if I only get one life, I wanna live it with you Say something like It's only you It's only you Say something like It’s only you It’s only you Where will you go when it's over? Who will you know when it's over? I know, yeah, I saw you, you know that, right? Just know that I saw you (I saw you, I saw, I saw)"
prompt_prefix = "Given the following, generate a 2-4 sentence summary without including the song name or the artist name in the summary: "


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt_prefix},
        {"role": "user", "content": lyrics}
    ],
    stop=["Embed"],
    temperature=0.25,
    frequency_penalty=0.5,
    presence_penalty=0.5)

summary = response["choices"][0]["message"]["content"]
print(summary)