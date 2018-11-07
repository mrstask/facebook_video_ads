import time
from campaign_creation import create_campaign
from custom_audience import create_custom_audience, add_users_mk
from ad_set_creation import create_ad_set
from creative_creation import create_video_creation, video_upload, video_download
from add_video_to_group import add_creative_to_group
from db_queries import get_campaign_name, set_campaign_id, get_audience_name, set_audience_id,\
    get_custom_audience, get_audience_name_mk, get_data_for_adset, set_adset_id, set_audience_mk,\
    get_data_video_upload, set_video_id, get_data_video_creation, set_video_creation_id, \
    get_creative_group, set_creative_group_id


page_id = '723430371025671'
for i in range(100):
    print(i)
    # 1. campaign creation
    if get_campaign_name():
        campaign_name = get_campaign_name()
        campaign_id = create_campaign(campaign_name)
        set_campaign_id(campaign_name, campaign_id)
        time.sleep(10)

    # 2. create audience
    if get_audience_name():
        audience_name = get_audience_name()
        custom_audience_id = create_custom_audience(audience_name)
        set_audience_id(audience_name, custom_audience_id)
        time.sleep(20)

    # 3. add users to group
    if get_audience_name_mk():
        audience_name, custom_audience_id = get_audience_name_mk()
        aud_to_go = get_custom_audience(audience_name)
        used_ids = add_users_mk(custom_audience_id, aud_to_go)
        set_audience_mk(custom_audience_id)
        time.sleep(20)

    # 4. creating adset
    if get_data_for_adset():
        campaign_id, custom_audience_id, audience_name = get_data_for_adset()
        ad_set_id = create_ad_set(campaign_id, custom_audience_id, audience_name)['id']
        set_adset_id(custom_audience_id, ad_set_id)
        time.sleep(20)

    # 5. Uploading video
    if get_data_video_upload():
        adgroup, custom_audience_id, link_video = get_data_video_upload()
        # Downloading video
        path = video_download(link_video, adgroup)
        video_id = video_upload(path, adgroup)
        set_video_id(custom_audience_id, video_id)
        time.sleep(20)

    # 6. Create video creation
    if get_data_video_creation():
        adgroup, video_id, destination_url, description = get_data_video_creation()
        video_creation_id = create_video_creation(video_id, destination_url, description, adgroup, page_id)
        set_video_creation_id(video_id, video_creation_id)
        time.sleep(20)

    if get_creative_group():
        ad_set_id, ad_creative_id, adgroup = get_creative_group()
        creative_group_id = add_creative_to_group(ad_set_id, ad_creative_id, adgroup)
        set_creative_group_id(ad_creative_id, creative_group_id['id'])
        time.sleep(20)
