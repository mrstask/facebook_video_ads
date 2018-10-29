from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi
from settings import my_access_token, my_app_id, my_app_secret, ad_account


def create_custom_audience(name):
    try:
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        my_account = AdAccount(f'act_{ad_account}')
        audience = CustomAudience(parent_id=my_account.get_id_assured())
        audience.update({
            CustomAudience.Field.name: name,
            CustomAudience.Field.subtype: CustomAudience.Subtype.custom,
            CustomAudience.Field.customer_file_source: CustomAudience.CustomerFileSource.both_user_and_partner_provided
        })
        audience.remote_create()
        audience = CustomAudience(audience[CustomAudience.Field.id])
        return audience['id']
    except Exception as e:
        print(type(e))


def add_users_mk(ca_id, users):
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        audience = CustomAudience(ca_id)
        audience_to_query = list()
        used_ids = list()

        for line in users:
            contact_id, aud_name, email, phone, used = line
            audience_to_query.append([email, phone])
            used_ids.append(contact_id)

        schema = [
            CustomAudience.Schema.MultiKeySchema.email,
            CustomAudience.Schema.MultiKeySchema.phone
        ]

        audience.add_users(schema, audience_to_query, is_raw=True, pre_hashed=True)
        print(used_ids)
        return audience.get_id()


def list_custom_audiences():
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount(f'act_{ad_account}')
    fields = ['account_id'
    ,'approximate_count'
    ,'customer_file_source'
    ,'data_source'
    ,'delivery_status'
    ,'description'
    ,'household_audience'
    ,'id'
    ,'is_household'
    ,'is_snapshot'
    ,'is_value_based'
    ,'name'
    ,'operation_status'
    ,'permission_for_actions'
    ,'retention_days'
    ,'seed_audience'
    ,'sharing_status'
    ,'subtype'
    ,'time_content_updated'
    ,'time_created'
    ,'time_updated'
    ]
    audiences = my_account.get_custom_audiences(fields=fields)
    return audiences


if __name__ == '__main__':
    print(list_custom_audiences())
    # audience_l = list()
    # with open('samples/campaign for api - audience.csv', newline='') as f:
    #     file_reader = csv.reader(f, delimiter=',', quotechar='|')
    #     next(file_reader, None)
    #     for line in file_reader:
    #         audience_name, email, phone = line
    #         audience_l.append([audience_name, email])
    # print(create_custom_audience('katya'))