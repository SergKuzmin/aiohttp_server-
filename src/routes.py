import pathlib

from src.views.converter import ConvertHandler

def setup_rotes(app):
    app.router.add_route('*', r'/api/convert', ConvertHandler)