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
    get_data_video_upload



# 1. campaign creation
# campaign_name = get_campaign_name()
# if campaign_name:
#     campaign_id = create_campaign(campaign_name)
#     set_campaign_id(campaign_name, campaign_id)
#     time.sleep(5)
#
# # # create audience
# audience_name = get_audience_name()
# if audience_name:
#     custom_audience_id = create_custom_audience(audience_name)
#     set_audience_id(audience_name, custom_audience_id)
#     time.sleep(5)
#
# # add users to group
# audience_name, custom_audience_id = get_audience_name_mk()
# aud_to_go = get_custom_audience(audience_name)
# if aud_to_go:
#     used_ids = add_users_mk(custom_audience_id, aud_to_go)
#     set_audience_mk(custom_audience_id)
#     time.sleep(5)
#
# # creating adset
# campaign_id, custom_audience_id, audience_name = get_data_for_adset()
# if campaign_id:
#     ad_set_id = create_ad_set(campaign_id, custom_audience_id, audience_name)['id']
#     set_adset_id(custom_audience_id, ad_set_id)
#     time.sleep(10)

# Uploading video
adgroup, custom_audience_id, link_video = get_data_video_upload()
# Downloading video
path = video_download(link_video, adgroup)

video_id = video_upload(path, adgroup)
print('Video is uploaded, id is: ', video_id)
# conn.execute(campaigns.update().where(
#     campaigns.c.custom_audience_id.match(custom_audience_id)
# ).values(
#     video_id=str(video_id))
# )

# adgroup, video_id, destination_url, description = conn.execute(sa.select(
#     [campaigns.c.adgroup, campaigns.c.video_id, campaigns.c.destination_url, campaigns.c.description]
# ).where(
#     sa.and_(campaigns.c.video_creation_id == None, campaigns.c.video_id != None))).fetchone()
# print(adgroup,video_id,destination_url, description)
# page_id = '723430371025671'
# video_creation_id = create_video_creation(video_id, destination_url, description, adgroup, page_id)
# print(video_creation_id)
# conn.execute(campaigns.update().where(
#     campaigns.c.video_id.match(video_id)
# ).values(
#     video_creation_id=str(ad_creation_id))
# )
# ad_set_id, ad_creative_id = conn.execute(sa.select(
#     [campaigns.c.ad_set_id, campaigns.c.video_creation_id]
# ).where(
#     sa.and_(campaigns.c.creative_group_id == None, campaigns.c.video_creation_id != None))).fetchone()
#
# creative_group_id = add_creative_to_group(ad_set_id, ad_creative_id)
# conn.execute(campaigns.update().where(
#     campaigns.c.video_creation_id.match(ad_creative_id)
# ).values(
#     creative_group_id=str(creative_group_id))
# )
#
#
#
#
#
#
#
#
#
