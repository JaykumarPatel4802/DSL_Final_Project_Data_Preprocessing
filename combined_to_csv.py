import csv
import json

train_file = open('combined_final_csv_format.csv', 'w')
combined_file = open('combined_final.txt', 'r')

# writer = csv.writer(train_file, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)
writer = csv.writer(train_file, delimiter=',', quoting=csv.QUOTE_ALL)
writer.writerow(['track_id', 'summary', 'lyrics'])

for line in combined_file:
    if (line == "\n"):
        continue
    json_string = json.loads(line)
    summary = json_string['summary'][0]
    lyrics = json_string['lyrics'][0]
    track_id = json_string['track_id'][0]

    writer.writerow([track_id, summary, lyrics])

train_file.close()
combined_file.close()
