from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

from settings import ad_account, my_access_token


def add_creative_to_group(ad_set_id, ad_creative_id):
    FacebookAdsApi.init(access_token=my_access_token)
    fields = []
    params = {
        'name': 'My Ad',
        'adset_id': ad_set_id,
        'creative': {'creative_id': ad_creative_id},
        'status': 'PAUSED',
      }
    return AdAccount(f'act_{ad_account}').create_ad(
        fields=fields,
        params=params,
    )


def list_creative():
    FacebookAdsApi.init(access_token=my_access_token)
    return AdAccount(f'act_{ad_account}').get_ad_creatives()


if __name__ == '__main__':
    print(list_creative())
    # ad_set_id = '23843061830090774'
    # ad_creative_id = '23843061833550774'
    # print(add_creative_to_group(ad_set_id, ad_creative_id))

