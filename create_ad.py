from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi

from settings import ad_account, my_access_token
image_hash = '4fd83c19ffaaf36ea2632cd2a430e979'


def image_upload(image_path):
    FacebookAdsApi.init(access_token=my_access_token)
    image = AdImage(parent_id=f'act_{ad_account}')
    image[AdImage.Field.filename] = image_path
    image.remote_create()

    return image[AdImage.Field.hash]

FacebookAdsApi.init(access_token=my_access_token)
creative = AdCreative(parent_id=f'act_{ad_account}')
creative[AdCreative.Field.name] = 'My Test Creative'
creative[AdCreative.Field.object_id] = '248309528557650'
creative[AdCreative.Field.page_id] = '248309528557650'
creative[AdCreative.Field.instagram_actor_id] = '254397038'

creative[AdCreative.Field.body] = 'sdfasdf'
creative[AdCreative.Field.video_id] = '6102071283352'
creative[AdCreative.Field.image_hash] = image_hash

# Finally, create your ad along with ad creative.
# Please note that the ad creative is not created independently, rather its
# data structure is appended to the ad group
ad = Ad(parent_id=f'act_{ad_account}')
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = '6102071163152'
ad[Ad.Field.creative] = creative
ad.remote_create(params={
    'status': Ad.Status.paused,
})