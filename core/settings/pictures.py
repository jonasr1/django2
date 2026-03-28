# the following are defaults, but you can override them
PICTURES = {
    "BREAKPOINTS": {
        "xs": 576,
        "s": 768,
        "m": 992,
        "l": 1200,
        "xl": 1400,
    },
    "GRID_COLUMNS": 5,
    "CONTAINER_WIDTH": 1200,
    "FILE_TYPES": ["AVIF"],
    "PIXEL_DENSITIES": [1],
    "USE_PLACEHOLDERS": True,
    "QUEUE_NAME": "pictures",
    "BACKEND": "default",
    "PROCESSOR": "pictures.tasks.process_picture",
}
