from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))
from pelicanconf import *  # noqa: F403

SITEURL = "https://blog.grayvines.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
