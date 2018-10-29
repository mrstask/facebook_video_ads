from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.advideo import AdVideo
from facebook_business.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreativevideodata import AdCreativeVideoData
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage
import time

from settings import ad_account, my_access_token


def image_upload(image_path):
    FacebookAdsApi.init(access_token=my_access_token)
    image = AdImage(parent_id=f'act_{ad_account}')
    image[AdImage.Field.filename] = image_path
    image.remote_create()
    image_hash = image[AdImage.Field.hash]
    return image_hash


def create_video_creation(video_id, destination_url, description, adgroup, page_id):
    FacebookAdsApi.init(access_token=my_access_token)
    video_data = AdCreativeVideoData()
    # video_data[AdCreativeVideoData.Field.description] = description
    video_data[AdCreativeVideoData.Field.video_id] = video_id
    image_hash = image_upload(f'samples/images/{adgroup}.png')
    video_data[AdCreativeVideoData.Field.image_hash] = image_hash
    video_data[AdCreativeVideoData.Field.call_to_action] = {
        'type': 'LIKE_PAGE',
        'value': {
            'page': page_id,
        },}

    object_story_spec = AdCreativeObjectStorySpec()
    object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = page_id
    object_story_spec[AdCreativeObjectStorySpec.Field.video_data] = video_data

    creative = AdCreative(parent_id=f'act_{ad_account}')
    creative[AdCreative.Field.name] = f'Video {adgroup}'
    creative[AdCreative.Field.object_story_spec] = object_story_spec
    creative[AdCreative.Field.url_tags] = destination_url
    return creative.remote_create()['id']



def video_upload(file_path, name):
    FacebookAdsApi.init(access_token=my_access_token)
    video = AdVideo(parent_id=f'act_{ad_account}')
    video[AdVideo.Field.filepath] = file_path
    video[AdVideo.Field.name] = name
    video.remote_create()
    video.waitUntilEncodingReady()
    time.sleep(10)
    return video['id']


def creation_list():
    FacebookAdsApi.init(access_token=my_access_token)
    fields = [
        'name',
        'video_id'
    ]

    return AdAccount(f'act_{ad_account}').get_ad_creatives(fields=fields)


if __name__ == '__main__':
    video_id = '301667993765449'
    image_url = 'https://scontent.fiev5-1.fna.fbcdn.net/v/t1.0-9/c0.0.409.409/20155695_1703818186327573_' \
                '1330708989496355145_n.jpg?_nc_cat=109&_nc_ht=scontent.fiev5-1.fna&oh=88ac809ec5e6a4f345b650' \
                'f8d575fd83&oe=5C4EF6F8'
    page_id = '723430371025671'
    path = 'samples/SampleVideo_360x240_1mb.mp4'
    # print(creation_list())
    # print(video_id)
    # video_id = video_upload(path)
    # print(video_id)
    print(create_video_creation(video_id, image_url, page_id))
