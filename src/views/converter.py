from aiohttp import web
import cv2
from src.util.api_util import get_data
import numpy as np
import re


class ConvertHandler(web.View):
    def __init__(self, request):
        super().__init__(request)

    async def post(self):
        multipart = await self.request.multipart()
        data = await get_data(multipart)
        images = [cv2.imdecode(np.frombuffer(p[1], dtype="uint8"), flags=1) for p in data.items() if
                  bool(re.search(r'file\d+', p[0]))]
        converter = self.request.app['model']
        converter.convert(images[0])
        return web.Response(text='Done')
        # converter = self.request.app['model']
