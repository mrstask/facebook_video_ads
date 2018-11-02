import csv
import time
from campaign_creation import create_campaign
from custom_audience import create_custom_audience, add_users_mk
from ad_set_creation import create_ad_set
from creative_creation import create_video_creation, video_upload, video_download
from add_video_to_group import add_creative_to_group
import sqlalchemy as sa
from db_queries import get_campaign_name, set_campaign_id, get_audience_name, set_audience_id,\
    get_custom_audience, get_audience_name_mk, get_data_for_adset, set_adset_id, set_audience_mk,\
    get_data_video_upload, set_video_id, get_data_video_creation, set_video_creation_id, \
    get_creative_group, set_creative_group_id


page_id = '723430371025671'

# 1. campaign creation
campaign_name = get_campaign_name()
if campaign_name:
    campaign_id = create_campaign(campaign_name)
    set_campaign_id(campaign_name, campaign_id)
    time.sleep(5)

# 2. create audience
audience_name = get_audience_name()
if audience_name:
    custom_audience_id = create_custom_audience(audience_name)
    set_audience_id(audience_name, custom_audience_id)
    time.sleep(5)

# 3. add users to group
audience_name, custom_audience_id = get_audience_name_mk()
aud_to_go = get_custom_audience(audience_name)
if aud_to_go:
    used_ids = add_users_mk(custom_audience_id, aud_to_go)
    set_audience_mk(custom_audience_id)
    time.sleep(5)

# 4. creating adset
campaign_id, custom_audience_id, audience_name = get_data_for_adset()
if campaign_id:
    ad_set_id = create_ad_set(campaign_id, custom_audience_id, audience_name)['id']
    set_adset_id(custom_audience_id, ad_set_id)
    time.sleep(10)

# 5. Uploading video
adgroup, custom_audience_id, link_video = get_data_video_upload()
# Downloading video
if adgroup:
    path = video_download(link_video, adgroup)
    video_id = video_upload(path, adgroup)
    print('Video is uploaded, id is: ', video_id)
    set_video_id(custom_audience_id, video_id)

# 6. Create video creation
adgroup, video_id, destination_url, description = get_data_video_creation()
video_creation_id = create_video_creation(video_id, destination_url, description, adgroup, page_id)
set_video_creation_id(video_id, video_creation_id)


ad_set_id, ad_creative_id, adgroup = get_creative_group()
creative_group_id = add_creative_to_group(ad_set_id, ad_creative_id, adgroup)
set_creative_group_id(ad_creative_id, creative_group_id)
