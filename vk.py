# python 3.7
# Author: Slava Koshman
# GitHub: https://github.com/Slauva

import vk_api
import config

def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def auth_handler():
    key = input("Enter authentication code: ")
    # If: True - save, False - do not save.
    remember_device = True

    return key, remember_device

# Authorization
vk = vk_api.VkApi(config.USER_LOGIN, config.USER_PASS, auth_handler=auth_handler, captcha_handler=captcha_handler)
vk.auth()

# Get vk api
user = vk.get_api()

# Get videos id from group 
vk_videos = user.video.get(owner_id = -config.OWNER_ID, album_id = config.ALBUM_ID)
vk_videos_id = []
for video in vk_videos['items']:
    vk_videos_id.append(video.get('id'))

# Create new album for videos
if config.NEED_NEW_ALBUM:
    config.TO_ALBUM_ID = user.video.addAlbum(title = config.NEW_ALBUM_TITLE)
    config.TO_ALBUM_ID = config.TO_ALBUM_ID['album_id']

# Post videos to album
iteration = 0
for video_id in vk_videos_id: 
    user.video.addToAlbum(album_id = config.TO_ALBUM_ID, owner_id = -config.OWNER_ID, video_id = video_id)
    iteration+=1
    print(iteration, end='\r')
