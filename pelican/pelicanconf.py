from pathlib import Path

HERE = Path(__file__).parent.resolve()
PATH = HERE.parent / "entries"

AUTHOR = "Julian Berman"

SITEURL = ""
SITENAME = "Julian"

TIMEZONE = "America/New_York"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%-d %B %Y"

THEME = HERE / "theme"

PLUGIN_PATHS = [HERE / "plugins", "plugins"]
PLUGINS = []

GITHUB_URL = "https://github.com/Julian"
SOCIAL = [
    ("github", GITHUB_URL),
    ("mastodon", "https://mastodon.social/@JulianWasTaken"),
    ("photos", "https://photos.grayvines.com/"),
]

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

DRAFT_URL = "drafts/{slug}/"
DRAFT_SAVE_AS = "drafts/{slug}/index.html"

CATEGORY_URL = "categories/{slug}/"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_SAVE_AS = "tags/index.html"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TYPOGRIFY = True

DOCUTILS_SETTINGS = dict(
    initial_header_level=4,  # Use h4 since we use h3 for entry titles
)

STATIC_PATHS = []
