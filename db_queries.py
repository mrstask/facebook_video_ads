import sqlalchemy as sa
from db import engine, campaigns, audience


def get_campaign_name():
    conn = engine.connect()
    campaign_name = conn.execute(sa.select([campaigns.c.campaign_name]).where(
        campaigns.c.campaign_id == None)).fetchone()
    if campaign_name:
        return campaign_name[0]


def set_campaign_id(camp_name, camp_id):
    conn = engine.connect()
    return conn.execute(campaigns.update().where(
        campaigns.c.campaign_name.match(camp_name)).values(campaign_id=camp_id))


def get_audience_name():
    conn = engine.connect()
    audience_name = conn.execute(sa.select([campaigns.c.adgroup]).where(
        sa.and_(campaigns.c.campaign_id != None, campaigns.c.custom_audience_id == None))).fetchone()
    if audience_name:
        return audience_name[0]


def set_audience_id(audience_name, custom_audience_id):
    conn = engine.connect()
    return conn.execute(campaigns.update().
                 where(campaigns.c.adgroup.match(audience_name)).values(custom_audience_id=custom_audience_id))


def get_audience_name_mk():
    conn = engine.connect()
    audience_name = conn.execute(sa.select([campaigns.c.adgroup, campaigns.c.custom_audience_id]).where(
        sa.and_(campaigns.c.custom_audience_id != None, campaigns.c.add_users_mk == False))).fetchone()
    if audience_name:
        return audience_name


def get_custom_audience(audience_name):
    conn = engine.connect()
    return conn.execute(audience.select().
                 where(audience.c.audience_name == audience_name)).fetchall()


def set_audience_mk(custom_audience_id):
    conn = engine.connect()
    conn.execute(campaigns.update().where(
        campaigns.c.custom_audience_id.match(custom_audience_id)).values(add_users_mk=True))


def get_data_for_adset():
    conn = engine.connect()
    data_for_adset = conn.execute(sa.select(
        [campaigns.c.campaign_id, campaigns.c.custom_audience_id, campaigns.c.adgroup]
    ).where(
        sa.and_(campaigns.c.ad_set_id == None, campaigns.c.custom_audience_id != None))).fetchone()
    if data_for_adset:
        return data_for_adset


def set_adset_id(custom_audience_id, ad_set_id):
    conn = engine.connect()
    conn.execute(campaigns.update().where(
        campaigns.c.custom_audience_id.match(custom_audience_id)).values(ad_set_id=ad_set_id))


def get_data_video_upload():
    conn = engine.connect()
    data_for_video = conn.execute(sa.select(
        [campaigns.c.adgroup, campaigns.c.custom_audience_id, campaigns.c.link_video]
    ).where(sa.and_(campaigns.c.video_id == None, campaigns.c.ad_set_id != None))).fetchone()
    if data_for_video:
        return data_for_video


def set_video_id(custom_audience_id, video_id):
    conn = engine.connect()
    return conn.execute(campaigns.update().where(
        campaigns.c.custom_audience_id.match(custom_audience_id)
    ).values(video_id=str(video_id)))


def get_data_video_creation():
    conn = engine.connect()
    data_video_creation = conn.execute(sa.select(
        [campaigns.c.adgroup, campaigns.c.video_id, campaigns.c.destination_url, campaigns.c.description]
    ).where(sa.and_(campaigns.c.video_creation_id == None, campaigns.c.video_id != None))).fetchone()
    if data_video_creation:
        return data_video_creation


def set_video_creation_id(video_id, video_creation_id):
    conn = engine.connect()
    return conn.execute(campaigns.update().where(campaigns.c.video_id.match(video_id)
        ).values(video_creation_id=str(video_creation_id)))


def get_creative_group():
    conn = engine.connect()
    creative_group_data = conn.execute(sa.select(
        [campaigns.c.ad_set_id, campaigns.c.video_creation_id, campaigns.c.adgroup]
    ).where(
        sa.and_(campaigns.c.creative_group_id == None, campaigns.c.video_creation_id != None))).fetchone()
    if creative_group_data:
        return creative_group_data


def set_creative_group_id(ad_creative_id, creative_group_id):
    conn = engine.connect()
    conn.execute(campaigns.update().where(
        campaigns.c.video_creation_id.match(ad_creative_id)
    ).values(creative_group_id=str(creative_group_id)))
