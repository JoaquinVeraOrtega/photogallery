"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_motion import motion

from .lightgallery import (
    render_gallery_component,
)  # import del componente para utilizarlo en la pagina index

data_json = {
    "galleries": {
        "commercial": {
            "tagline": "GUEVARA CONTRACTING REMODELINGS",
            "title": "Browse Our Gallery",
            "description": "Welcome to our gallery, where you can explore a diverse range of remodeling projects that highlight our expertise in both residential and commercial spaces. We take pride in showcasing our versatility and commitment to excellence through our varied portfolio.",
            "items": [
                {
                    "image": "https://picsum.photos/200/400"
                },
                {
                    "image": "https://picsum.photos/400/300"
                },
                {
                    "image": "https://picsum.photos/500/400"
                },
                {
                    "image": "https://picsum.photos/300"
                },
                {
                    "image": "https://picsum.photos/450/300"
                },
                {
                    "image": "https://picsum.photos/200/300"
                },
                {
                    "image": "https://picsum.photos/250/360"
                },
                {
                    "image": "https://picsum.photos/500/320"
                },
                {
                    "image": "https://picsum.photos/400"
                },
                {
                    "image": "https://picsum.photos/500"
                },
            ],
        }
    }
}


def index():
    return rx.flex(render_gallery_component(data_json), justify="center")
    


app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css",  # css para la funcionalidad lightbox de la galeria de imagenes
    ],
    theme=rx.theme(
        appearance="light",
    ),
)
app.add_page(index)
