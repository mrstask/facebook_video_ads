from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi
from settings import my_access_token, my_app_id, my_app_secret, ad_account

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(f'act_{ad_account}')


def list_custom_audiences():
    audiences_dict = dict()
    audiences = my_account.get_custom_audiences(fields=[
        CustomAudience.Field.name,
        CustomAudience.Field.description])
    if audiences:
        for audience in audiences:
            audiences_dict[audience[CustomAudience.Field.id]] = audience[CustomAudience.Field.name]
    return audiences_dict


def create_custom_audience(name, description=None):
    audience = CustomAudience(parent_id=my_account.get_id_assured())
    audience.update({
        CustomAudience.Field.name: name,
        CustomAudience.Field.subtype: CustomAudience.Subtype.custom,
        CustomAudience.Field.customer_file_source: CustomAudience.CustomerFileSource.both_user_and_partner_provided
    })

    if description:
        audience.update({CustomAudience.Field.description: description})
    audience.remote_create()
    return audience[CustomAudience.Field.id]


if __name__ == '__main__':
    print(list_custom_audiences())
    # print(create_custom_audience('some-2', description=None))