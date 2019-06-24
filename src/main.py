import asyncio
from aiohttp import web
from src.module_class.image_net import ImageConverter
from src.routes import setup_rotes


async def init_model(app):
    app['model'] = ImageConverter()


def init(loop):
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app.on_startup.append(init_model)
    return app


def start():
    loop = asyncio.get_event_loop()
    app = init(loop=loop)
    setup_rotes(app)
    web.run_app(app=app)

if __name__ == "__main__":
    start()