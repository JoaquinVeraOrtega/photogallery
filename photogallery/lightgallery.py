import reflex as rx


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


def create_responsive_image(image_src):
    """Componente de imagen responsiva con efectos on hover."""
    return rx.image(
        src=image_src,
        transition_duration="300ms",
        height="16rem",
        _hover={"transform": "scale(0.95)", "border": "5px solid #D32F2F"},
        object_fit="cover",
        transition_property="transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
        border_radius="10px",
    )


def create_image_card(image_src):
    """Componente contenedor de la imagen con afectos de animacion de entrada y lightbox."""
    return rx.el.a(
        create_responsive_image(
            image_src,
        ),
        href=image_src,
        custom_attrs={"data-lightbox": "gallery"},
        display="block",
        data_aos="fade-up",
        data_aos_duration="2000",
    )


def create_image_grid():
    """Grilla de imagenes que se adapta a distintos tamaños de pantalla. Recorre el dict con la data de las imagenes."""
    return rx.box(
        [
            create_image_card(item["image"])
            for item in data_json["galleries"]["commercial"]["items"]
        ],
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "640px": "repeat(2, minmax(0, 1fr))",
                "1024px": "repeat(3, minmax(0, 1fr))",
                "1224px": "repeat(4, minmax(0, 1fr))",
            }
        ),
        id="gallery",
        overflow="hidden",
    )


def create_heading_section():
    """Componente de encabezado. Crea el titulo, tagline y descripcion a partir del dict con la data"""
    return rx.flex(
        rx.heading(data_json["galleries"]["commercial"]["tagline"], size="5"),
        rx.heading(data_json["galleries"]["commercial"]["title"], size="9"),
        rx.text(
            data_json["galleries"]["commercial"]["description"],
        ),
        width="100%",
        max_width=rx.breakpoints(sm="640px", md="768px", lg="1024px", xl="1280px"),
        justify="center",
        align="center",
        spacing="5",
        direction="column",
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_main_content():
    """Componente principal. Se junta la grilla de imagenes con el encabezado"""
    return rx.box(
        rx.box(
            create_heading_section(),
            create_image_grid(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max_width": "640px"},
                    "768px": {"max_width": "768px"},
                    "1024px": {"max_width": "1024px"},
                    "1280px": {"max_width": "1280px"},
                    "1536px": {"max_width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="2rem",
            padding_bottom="2rem",
            background_color="#eff6ff",
        ),
        width="100%",
    )


def render_gallery_component():
    """Carga los scripts necesarios para la funcionalidad lightbox y de animacion al scrollear. Renderiza el componente completo"""
    return rx.fragment(
        rx.box(
            create_main_content(),
            rx.script(
                src="https://unpkg.com/aos@2.3.1/dist/aos.js",
                on_ready=rx.call_script(
                    """
                        AOS.init();
                    """
                ),
            ),
            rx.script(
                src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js",
                on_ready=rx.call_script(
                    """
                    const script = document.createElement("script");
                    script.src = "https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js";
                    script.onload = function() {
                        lightbox.option({
                            'resizeDuration': 200,
                            'wrapAround': true
                        });
                    };
                    document.body.appendChild(script);
                    """
                ),
            ),
        ),
    )
