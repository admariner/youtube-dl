import re

from .common import InfoExtractor
from ..utils import compat_urllib_parse

class PornHdIE(InfoExtractor):
    _VALID_URL = r'(?:http://)?(?:www\.)?pornhd\.com/videos/(?P<video_id>[0-9]+)/(?P<video_title>.+)'
    _TEST = {
        u'id': u'1962',
        u'url': u'http://www.pornhd.com/videos/1962/sierra-day-gets-his-cum-all-over-herself-hd-porn-video',
        u'md5': u'4fe06e5108e8b524c35896f4c54c7155',
        u'info_dict': {
            u"title": u"sierra-day-gets-his-cum-all-over-herself-hd-porn-video",
            u"age_limit": 18,
        }
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)

        video_id = mobj.group('video_id')
        video_title = mobj.group('video_title')
        video_extension = 'flv'

        webpage = self._download_webpage(url, video_id)


        self.report_extraction(video_id)

        video_url = self._html_search_regex(
            r'&hd=(http.+?)&', webpage, u'video URL')
        video_url = compat_urllib_parse.unquote(video_url)

        age_limit = 18

        return {
            'id':        video_id,
            'url':       video_url,
            'ext':       video_extension,
            'title':     video_title,
            'age_limit': age_limit,
        }
