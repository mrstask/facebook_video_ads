import csv
from campaign_creation import create_campaign
from custom_audience import create_custom_audience, add_users_mk
from ad_set_creation import create_ad_set
from creative_creation import create_video_creation, video_upload
import time

filename = 'samples/campaign for api.csv'
image_url = 'https://scontent.fiev5-1.fna.fbcdn.net/v/t1.0-9/c0.0.409.409/20155695_1703818186327573_' \
            '1330708989496355145_n.jpg?_nc_cat=109&_nc_ht=scontent.fiev5-1.fna&oh=88ac809ec5e6a4f345b650' \
            'f8d575fd83&oe=5C4EF6F8'
path = 'samples/SampleVideo_360x240_1mb.mp4'

result = dict()
audience = list()
created_campaigns = dict()

with open('samples/campaign for api - audience.csv', newline='') as f:
    file_reader = csv.reader(f, delimiter=',', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        if line:
            audience.append(line)

with open(filename, newline='') as f:
    file_reader = csv.reader(f, delimiter=',', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        # get cells of csv string
        campaign_name, adgroup, image_url, description, page_id, link_video, device_cat, audience_name = line
        # if there are no campaign with this name, create one
        if campaign_name not in created_campaigns.keys():
            campaign_id = create_campaign(campaign_name)['id']
            print('Campaign created, id is: ', campaign_id)
            created_campaigns[campaign_name] = campaign_id
            time.sleep(5)

        custom_audience_id = create_custom_audience(audience_name)
        add_users_mk(custom_audience_id, audience_name, audience)
        print('Custom audience created, id is: ', custom_audience_id)
        time.sleep(5)

        ad_set_id = create_ad_set(created_campaigns[campaign_name], custom_audience_id)['id']
        print('AdSet created, id is: ', ad_set_id)
        time.sleep(5)

        # video_id = video_upload(path)
        # print('Video is uploaded, id is: ', video_id)
        # video_creation_id = create_video_creation(video_id, image_url, page_id)['id']
        # print(video_creation_id)
        # todo write everything to db
        result[campaign_name] = [campaign_name, created_campaigns[campaign_name],
                                 custom_audience_id, ad_set_id]

print(result)

