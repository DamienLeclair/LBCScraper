class ForceUTF8Response(object):
    """A downloader middleware to force utf8 encoding for all responses."""

    def process_response(self, request, response, spider):
        ubody = response.body_as_unicode().encode('utf8')
        return response.replace(body=ubody, encoding='utf8')

