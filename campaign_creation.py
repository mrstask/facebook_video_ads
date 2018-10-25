from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from settings import my_access_token, my_app_id, my_app_secret, ad_account


def create_campaign(name):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount(f'act_{ad_account}')

    fields = [
    ]
    params = {
        'name': name,
        'objective': 'VIDEO_VIEWS',
        'status': 'PAUSED',
    }
    return my_account.create_campaign(
        fields=fields,
        params=params,
    )


def list_campaigns():
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount(f'act_{ad_account}')
    fields = ['id', 'name']
    return my_account.get_campaigns(fields=fields)


if __name__ == '__main__':
    # print(create_campaign('lop'))
    print(list_campaigns())


