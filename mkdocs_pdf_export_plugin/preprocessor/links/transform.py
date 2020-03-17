import os

from .util import is_doc, normalize_href
from slugify import slugify


def transform_href(href: str, rel_url: str, should_slugify=False):
    # normalize href to #foo/bar/section:id
    head, tail = os.path.split(href)
    section = ''
    id = ''
    if not head:
        head, section = os.path.split(rel_url)
        section = os.path.splitext(section)[0]
    else:
        head = normalize_href(head, rel_url)

    if head != '':
        head += '/'

    if tail.startswith('#'):
        id = tail[1:]
    elif '#' in tail:
        section, id = str.split(tail, '#', 1)
        section, dummy_ext = os.path.splitext(section)
    else:
        if not is_doc(href):
            return href

        return '#{}{}:'.format(head, tail)

    if should_slugify:
        id = slugify(id)

    return '#{}{}:{}'.format(head, section, id)

# normalize id to foo/bar/section:id


def transform_id(id: str, rel_url: str, should_slugify=False):
    head, tail = os.path.split(rel_url)
    section, _ = os.path.splitext(tail)

    if len(head) > 0:
        head += '/'

    if should_slugify:
        id = slugify(id)

    return '{}{}:{}'.format(head, section, id)
