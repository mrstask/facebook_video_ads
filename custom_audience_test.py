from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi
from settings import my_access_token, my_app_id, my_app_secret, ad_account
import csv

custom_a_id = '23843064368750774'
audience = list()

with open('samples/audience.csv', newline='') as f:
    file_reader = csv.reader(f, delimiter=',', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        if line:
            audience.append(line)
            # print(line)
# print(audience)
# audience = ['hartwell.1987@mail.ru','mcculloch-85@mail.ru','lizzie.dusek.86@mail.ru','swickh@mail.ru',
#             'washburn-91@mail.ru','lavenia_watson_watson@mail.ru','helena.mcarthur.84@mail.ru']
# aud_new = list()
# i = 0
# for line in audience:
#     aud_new.append(['name' + str(i), line, 'second_name' + str(i)])
#     i+=1
# print(aud_new)


def create_custom_audience():
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount(f'act_{ad_account}')
    fields = [
    ]
    params = {
        'name': 'My new Custom Audience-MK-1000',
        'subtype': 'CUSTOM',
        'description': 'People who purchased on my website',
        'customer_file_source': 'BOTH_USER_AND_PARTNER_PROVIDED',
    }
    print(my_account.create_custom_audience(
        fields=fields,
        params=params,
    ))


def add_users_email(ca_id, audience_list):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    audience = CustomAudience(ca_id)
    users = audience_list

    audience.add_users(CustomAudience.Schema.email_hash, users)


def add_users_mk(ca_id, users):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    audience = CustomAudience(ca_id)

    schema = [
              CustomAudience.Schema.MultiKeySchema.email,
              ]

    audience.add_users(schema, users, is_raw=True)
    return audience.get_id()


if __name__ == '__main__':
    print(add_users_mk(custom_a_id, audience))
    # create_custom_audience()