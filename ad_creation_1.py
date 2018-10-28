from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreativetextdata \
    import AdCreativeTextData
from facebook_business.adobjects.adcreativelinkdata \
    import AdCreativeLinkData

from settings import my_access_token, ad_account

FacebookAdsApi.init(access_token=my_access_token)


link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.link] = 'http://allaboutfasionbyvs.wordpress.com'
link_data[AdCreativeLinkData.Field.message] = 'Click Me!'

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = 723430371025671
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data


fields = []
params = {
    'title': 'My Test Creative',
    'object_story_spec' : object_story_spec,
}

adcreate = AdAccount(f'act_{ad_account}').create_ad_creative(
    fields = fields,
    params = params,
)

print("Adcreative: ",adcreate)
