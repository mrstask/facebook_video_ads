from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from settings import my_access_token, my_app_id, my_app_secret, ad_account


def create_campaign(name):
    try:
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        my_account = AdAccount(f'act_{ad_account}')

        fields = [
        ]
        params = {
            'name': name,
            'objective': 'VIDEO_VIEWS',
            'status': 'PAUSED',
        }
        create_campaign_id = my_account.create_campaign(
            fields=fields,
            params=params,
        )
        return create_campaign_id['id']
    except Exception as e:
        print(e)


def list_campaigns():
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount(f'act_{ad_account}')
    fields = ['account_id',
              'budget_rebalance_flag',
              'budget_remaining',
              'buying_type',
              'can_create_brand_lift_study',
              'can_use_spend_cap',
              'configured_status',
              'created_time',
              'effective_status',
              'id',
              'name',
              'objective',
              'recommendations',
              'source_campaign',
              'source_campaign_id',
              'spend_cap',
              'start_time',
              'status',
              'updated_time',
    ]
    return my_account.get_campaigns(fields=fields)


if __name__ == '__main__':
    # print(create_campaign('lop'))
    print(list_campaigns())


