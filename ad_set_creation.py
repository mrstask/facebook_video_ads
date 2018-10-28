import time
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targeting import Targeting
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign


from settings import ad_account, my_access_token


campaign_id = '23843066772040774'
audience_id = '23843066772060774'
audience_name = 'test'


def create_ad_set(campaign_id, audience_id, audience_name):
    try:
        FacebookAdsApi.init(access_token=my_access_token)
        fields = []
        params = {
            AdSet.Field.name: audience_name,
            AdSet.Field.campaign_id: campaign_id,
            AdSet.Field.daily_budget: 5000,
            AdSet.Field.start_time: int(time.time()),
            AdSet.Field.end_time: int(time.time() + 100000),
            AdSet.Field.optimization_goal: AdSet.OptimizationGoal.video_views,
            AdSet.Field.billing_event: AdSet.BillingEvent.video_views,
            AdSet.Field.bid_amount: 100,
            AdSet.Field.targeting: {
             "geo_locations": {
               "countries": ["UA"],
             },
             "age_min": 18,
             "age_max": 65,
             "custom_audiences": [
                     {
                         "id": audience_id}]},
            Targeting.Field.device_platforms: ['mobile', 'desktop'],
            }
        return AdAccount(f'act_{ad_account}').create_ad_set(fields=fields, params=params)
    except Exception as e:
        print(type(e))


def list_ad_set():
    FacebookAdsApi.init(access_token=my_access_token)
    fields = ['account_id',
              'attribution_spec',
              'bid_strategy',
              'billing_event',
              'budget_remaining',
              'campaign',
              'campaign_id',
              'configured_status',
              'created_time',
              'creative_sequence',
              'daily_budget',
              'destination_type',
              'effective_status',
              'id',
              'lifetime_budget',
              'lifetime_imps',
              'name',
              'optimization_goal',
              'pacing_type',
              'recommendations',
              'recurring_budget_semantics',
              'source_adset_id',
              'start_time',
              'status',
              'targeting',
              'updated_time',
              'use_new_app_click',
    ]

    return Campaign(f'act_{ad_account}').get_ad_sets(fields=fields)


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
    # print(list_ad_set())
    print(create_ad_set(campaign_id, audience_id, audience_name))
    # print(connect_audience(campaign_id, audience_id, device_cat))
