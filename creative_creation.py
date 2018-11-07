from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.advideo import AdVideo
from facebook_business.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreativevideodata import AdCreativeVideoData
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage
from pprint import pprint
import os
import time
import urllib3
import certifi
from unidecode import unidecode
from settings import ad_account, my_access_token


def image_upload(image_path):
    files = list()
    image_path = unidecode(image_path)
    print(image_path)
    if not os.path.isfile(f'samples/images/{image_path}.png'):
        for file in os.listdir('samples/images/'):
            if file.startswith(image_path.split('_')[0]):
                files.append(file)
        for file in os.listdir('samples/images/'):
            if file.startswith(image_path[0:3]):
                files.append(file)
        if not files:
            for file in os.listdir('samples/images/'):
                if file.startswith(image_path[0]):
                    files.append(file)
        # pprint(files)
        # image_path = input('Set valid path: ')
        image_path = files[0]

    FacebookAdsApi.init(access_token=my_access_token)
    image = AdImage(parent_id=f'act_{ad_account}')
    if image_path.endswith('.png'):
        image[AdImage.Field.filename] = f'samples/images/{image_path}'
    else:
        image[AdImage.Field.filename] = f'samples/images/{image_path}.png'
    image.remote_create()
    image_hash = image[AdImage.Field.hash]
    return image_hash


def create_video_creation(video_id, destination_url, description, adgroup, page_id):
    FacebookAdsApi.init(access_token=my_access_token)
    video_data = AdCreativeVideoData()
    # video_data[AdCreativeVideoData.Field.description] = description
    video_data[AdCreativeVideoData.Field.video_id] = video_id
    image_hash = image_upload(adgroup)
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


def video_download(url, file_name):
    url = url.split('/')[5]
    url = f'https://drive.google.com/uc?authuser=0&id={url}&export=download'
    file_name = unidecode(file_name).replace(' ', "_")
    file_name = f'samples/video/{file_name}.mp4'
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', url, preload_content=False)
    with open(file_name, 'wb') as out:
        while True:
            data = r.read()
            if not data:
                break
            out.write(data)
    r.release_conn()
    return file_name


if __name__ == '__main__':
    video_id = '301667993765449'
    page_id = '723430371025671'
    path = 'samples/video/ruslan_litvinenko.mp4'
    image_upload('/home/stask/PycharmProjects/facebook_app/samples/images/Ivan_Omelchenko.png')
    # print(creation_list())
    # print(video_id)
    # video_id = video_upload(path, 'some-2')
    # video_download()
    # print(video_id)
    # print(create_video_creation(video_id, image_url, page_id))
