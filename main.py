from aiohttp import web

import request


async def hello():
    request.post('hhh')


async def handler(request):
    data = {'some': 'data'}
    return web.json_response(data)

app = web.Application()

# app.add_routes([web.get('/', hello)])
# app.add_routes([web.get('/1', handler)])

web.run_app(app)