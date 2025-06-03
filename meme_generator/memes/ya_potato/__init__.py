from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.tags import MemeTags

imgdir = Path(__file__).parent / "images"

def ya_potato(images: list[BuildImage], texts, args):
    return BuildImage.open(imgdir / '0.jpeg').save_jpg()

add_meme(
    "ya_potato",
    ya_potato,
    min_images=0,
    max_images=0,
    keywords=["呀土豆"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 3),
    date_modified=datetime(2025, 6, 3),
)
