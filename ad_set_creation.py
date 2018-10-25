import time
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targeting import Targeting
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign


from settings import ad_account, my_access_token


campaign_id = '6102070949352'
audience_id = '6102070949752'
device_cat = 'mobile'


def create_ad_set(campaign_id, audience_id, device_cat):
    FacebookAdsApi.init(access_token=my_access_token)
    fields = []
    params = {
        AdSet.Field.name: 'A CPV Ad Set',
        AdSet.Field.campaign_id: campaign_id,
        AdSet.Field.daily_budget: 5000,
        AdSet.Field.start_time: int(time.time()),
        AdSet.Field.end_time: int(time.time() + 100000),
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.video_views,
        AdSet.Field.billing_event: AdSet.BillingEvent.video_views,
        AdSet.Field.bid_amount: 100,
        AdSet.Field.targeting: {
         "geo_locations": {
           "countries": ["US"],
         },
         "age_min": 18,
         "age_max": 65,
         "custom_audiences": [
                 {
                     "id": audience_id}]},
        Targeting.Field.device_platforms: [device_cat],
        Targeting.Field.publisher_platforms: 'facebook'
        }
    return AdAccount(f'act_{ad_account}').create_ad_set(fields=fields, params=params)


def list_ad_set():
    FacebookAdsApi.init(access_token=my_access_token)

    fields = [
        'name',
        'start_time',
        'end_time',
        'daily_budget',
        'lifetime_budget',
    ]
    params = {
    }
    return Campaign(f'act_{ad_account}').get_ad_sets(fields=fields, params=params)


def connect_audience(campaign_id, audience_id, device_cat):
    adset = AdSet(fbid=audience_id, parent_id=f'act_{ad_account}')
    params = {
        AdSet.Field.name: 'A CPV Ad Set',
        AdSet.Field.campaign_id: campaign_id,
        AdSet.Field.daily_budget: 500,
        AdSet.Field.start_time: int(time.time()),
        AdSet.Field.end_time: int(time.time() + 100000),
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.video_views,
        AdSet.Field.billing_event: AdSet.BillingEvent.video_views,
        AdSet.Field.bid_amount: 100,
        AdSet.Field.targeting: {
         "geo_locations": {
           "countries": ["Ukraine"],
         },
         "age_min": 18,
         "age_max": 65,
         "custom_audiences": [
                 {
                     "id": audience_id}]},
        Targeting.Field.device_platforms: [device_cat],
        }
    adset.update(params=params)
    return adset


if __name__ == '__main__':
    # print(create_ad_set(campaign_id, audience_id, device_cat))
    print(connect_audience(campaign_id, audience_id, device_cat))
