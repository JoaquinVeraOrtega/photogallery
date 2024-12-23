"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


from .lightgallery import render_gallery_component #import del componente para utilizarlo en la pagina index


def index():
    return rx.flex(render_gallery_component(), justify="center")


app = rx.App(
    stylesheets=[
        "https://unpkg.com/aos@2.3.1/dist/aos.css", #css para las animaciones on scroll
        "https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css", #css para la funcionalidad lightbox de la galeria de imagenes
    ],
    theme=rx.theme(
        appearance="light",
    ),
)
app.add_page(index)
