import csv
import time
from campaign_creation import create_campaign
from custom_audience import create_custom_audience, add_users_mk
from ad_set_creation import create_ad_set
from creative_creation import create_video_creation, video_upload
from add_video_to_group import add_creative_to_group
import sqlalchemy as sa

from db import engine, campaigns, audience


conn = engine.connect()
# 1. campaign creation
camp_name = conn.execute(sa.select([campaigns.c.campaign_name]).where(campaigns.c.campaign_id == None)).fetchone()[0]
if camp_name:
    campaign_id = create_campaign(camp_name)
    conn.execute(campaigns.update().where(campaigns.c.campaign_name.match(camp_name)).values(campaign_id=campaign_id))
    time.sleep(10)

# create audience
audience_name = conn.execute(sa.select([campaigns.c.adgroup]).
                         where(sa.and_(campaigns.c.campaign_id != None,
                                       campaigns.c.adgroup != None))).fetchone()[0]
if audience_name:
    custom_audience_id = create_custom_audience(audience_name)
    conn.execute(campaigns.update().
                 where(campaigns.c.adgroup.match(audience_name)).values(custom_audience_id=custom_audience_id))

# add users to group
aud_to_go = conn.execute(audience.select().
                             where(audience.c.audience_name == audience_name)).fetchall()
if aud_to_go:
    used_ids = add_users_mk(custom_audience_id, aud_to_go)
    conn.execute(campaigns.update().where(
        campaigns.c.custom_audience_id.match(custom_audience_id)
    ).values(
        add_users_mk=True)
    )
time.sleep(10)

# creating adset
campaign_id, custom_audience_id, audience_name = conn.execute(sa.select(
    [campaigns.c.campaign_id, campaigns.c.custom_audience_id, campaigns.c.adgroup]
).where(
    sa.and_(campaigns.c.ad_set_id == None, campaigns.c.custom_audience_id != None))).fetchone()
print(campaign_id, custom_audience_id, audience_name)
ad_set_id = create_ad_set(campaign_id, custom_audience_id, audience_name)['id']

print(ad_set_id)
conn.execute(campaigns.update().where(
    campaigns.c.custom_audience_id.match(custom_audience_id)
).values(
    ad_set_id=ad_set_id)
)
print('AdSet created, id is: ', ad_set_id)
time.sleep(10)

filename, custom_audience_id = conn.execute(sa.select(
    [campaigns.c.adgroup, campaigns.c.custom_audience_id]
).where(
    sa.and_(campaigns.c.video_id == None, campaigns.c.ad_set_id != None))).fetchone()
path = 'samples/video/' + filename + '.mp4'
video_id = video_upload(path, filename)
print('Video is uploaded, id is: ', video_id)
conn.execute(campaigns.update().where(
    campaigns.c.custom_audience_id.match(custom_audience_id)
).values(
    video_id=str(video_id))
)
adgroup, video_id, destination_url, description = conn.execute(sa.select(
    [campaigns.c.adgroup, campaigns.c.video_id, campaigns.c.destination_url, campaigns.c.description]
).where(
    sa.and_(campaigns.c.video_creation_id == None, campaigns.c.video_id != None))).fetchone()
print(adgroup,video_id,destination_url, description)
page_id = '723430371025671'
video_creation_id = create_video_creation(video_id, destination_url, description, adgroup, page_id)
print(video_creation_id)
conn.execute(campaigns.update().where(
    campaigns.c.video_id.match(video_id)
).values(
    video_creation_id=str(ad_creation_id))
)
ad_set_id, ad_creative_id = conn.execute(sa.select(
    [campaigns.c.ad_set_id, campaigns.c.video_creation_id]
).where(
    sa.and_(campaigns.c.creative_group_id == None, campaigns.c.video_creation_id != None))).fetchone()

creative_group_id = add_creative_to_group(ad_set_id, ad_creative_id)
conn.execute(campaigns.update().where(
    campaigns.c.video_creation_id.match(ad_creative_id)
).values(
    creative_group_id=str(creative_group_id))
)









