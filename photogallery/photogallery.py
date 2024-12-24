"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


from .lightgallery import render_gallery_component #import del componente para utilizarlo en la pagina index

data_json = {
    "galleries": {
        "commercial": {
            "tagline": "GUEVARA CONTRACTING REMODELINGS",
            "title": "Browse Our Gallery",
            "description": "Welcome to our gallery, where you can explore a diverse range of remodeling projects that highlight our expertise in both residential and commercial spaces. We take pride in showcasing our versatility and commitment to excellence through our varied portfolio.",
            "items": [
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-01.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-02.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-03.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-04.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-05.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-06.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-07.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-08.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-09.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-10.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-11.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-12.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-13.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-14.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-15.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-16.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-17.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-18.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-19.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-20.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-21.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-22.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-23.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-24.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-25.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-26.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-27.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-28.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-29.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-30.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-31.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-32.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-33.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-34.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-35.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-36.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-37.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-38.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-39.webp"
                },
                {
                    "image": "https://res.cloudinary.com/xiadom/image/upload/v1724515697/xiadom-websites/guevaracontracting/landing_page/gallery/general/082424-40.webp"
                },
            ],
        }
    }
}

def index():
    return rx.flex(render_gallery_component(data_json), justify="center")


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
