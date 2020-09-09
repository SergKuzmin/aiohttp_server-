import re

import cv2
import numpy as np
from aiohttp import web


class ConvertHandler(web.View):
    def __init__(self, request):
        super().__init__(request)

    async def post(self):
        data = await self.request.post()
        print(data)
        images = [cv2.imdecode(np.frombuffer(p[1].file.read(), dtype="uint8"), flags=1) for p in data.items() if
                  bool(re.search(r'file\d+', p[0]))]
        converter = self.request.app['model']
        converter.convert(images[0])
        return web.Response(text='Done')
        # converter = self.request.app['model']
