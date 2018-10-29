import csv
from db import engine, campaigns, audience


conn = engine.connect()
with open('samples/launch_audience.csv', newline='') as f:
    file_reader = csv.reader(f, delimiter=';', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        print(line)
        if line:
            conn.execute(audience.insert().values(audience_name=line[0],
                                                  email=line[1],
                                                  phone=line[2]
                                                  ))


# with open('samples/launch campaign.tsv', newline='') as f:
#     file_reader = csv.reader(f, delimiter='\t', quotechar='|')
#     next(file_reader, None)
#     for line in file_reader:
#         print(line)
#         conn.execute(campaigns.insert().values(campaign_name=line[0],
#                                                adgroup=line[1],
#                                                description=line[2],
#                                                link_video=line[3],
#                                                destination_url=line[4],
#                                               ))
