import csv
from campaign_creation import create_campaign
from custom_audience import create_custom_audience
from ad_set_creation import create_ad_set
from creative_creation import create_video_creation, video_upload

filename = 'samples/campaign_for_api.csv'
device_cat = 'mobile'
image_url = 'https://scontent.fiev5-1.fna.fbcdn.net/v/t1.0-9/c0.0.409.409/20155695_1703818186327573_' \
            '1330708989496355145_n.jpg?_nc_cat=109&_nc_ht=scontent.fiev5-1.fna&oh=88ac809ec5e6a4f345b650' \
            'f8d575fd83&oe=5C4EF6F8'
path = 'samples/SampleVideo_360x240_1mb.mp4'

result = list()
with open(filename, newline='') as f:
    file_reader = csv.reader(f, delimiter=',', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        campaign_name, adgroup, IMAGE_URL, Discription, page_id, link_video, device_cat = line
        campaign_id = create_campaign(campaign_name)['id']
        print('Campaign created, id is: ', campaign_id)
        custom_audience_id = create_custom_audience(campaign_id)
        print('Custom audience created, id is: ', custom_audience_id)
        ad_set_id = create_ad_set(campaign_id, custom_audience_id, device_cat)['id']
        print('AdSet created, id is: ', ad_set_id)
        video_id = video_upload(path)
        print('Video is uploaded, id is: ', video_id)
        video_creation_id = create_video_creation(video_id, image_url, page_id)['id']
        print(video_creation_id)
        # result.append([campaign_name, adgroup, IMAGE_URL, Discription, PAGE_ID, link_video, device_cat, campaign_id])

