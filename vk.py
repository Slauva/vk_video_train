import vk_api
import config

class Train:

    def __init__(self, user_login, user_pass, albums_id, owner_id):
        vk = vk_api.VkApi(user_login, user_pass, auth_handler=self.auth_handler, captcha_handler=self.captcha_handler)
        vk.auth()
        self.user = vk.get_api()
        self.run(albums_id, owner_id)

    def captcha_handler(self, captcha):
        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
        return captcha.try_again(key)

    def auth_handler(self):
        key = input("Enter authentication code: ")
        # If: True - save, False - do not save.
        remember_device = True
        return key, remember_device

    def getVediosID(self, album_id, owner_id):
        vk_videos = self.user.video.get(owner_id = -owner_id, album_id = album_id, count = 200)
        vk_videos_id = []
        for video in vk_videos['items']:
            vk_videos_id.append(video.get('id'))
        return vk_videos_id

    def addAlbum(self, title):
        r = self.user.video.addAlbum(title = title)
        return r['album_id']

    def getAlbumTitle(self, album_id, owner_id):
        album = self.user.video.getAlbumById(owner_id = -owner_id, album_id = album_id)
        return album['title']

    def run(self, albums_id, owner_id):
        for album_id in albums_id:
            videos = self.getVediosID(album_id, owner_id)
            new_album_id = self.addAlbum(self.getAlbumTitle(album_id, owner_id))
            for video in videos:
                self.user.video.addToAlbum(album_id = new_album_id, owner_id = -owner_id, video_id = video)
            print('Complete')


if __name__ == "__main__":
    _ = Train(config.USER_LOGIN, config.USER_PASS, config.ALBUMS_ID, config.OWNER_ID)
