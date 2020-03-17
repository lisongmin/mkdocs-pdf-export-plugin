import os

from .links import transform_href, transform_id, get_body_id, replace_asset_hrefs, rel_pdf_href

from weasyprint import urls
from bs4 import BeautifulSoup
from slugify import slugify


def get_combined(soup: BeautifulSoup, base_url: str, rel_url: str, should_slugify=False):
    for id in soup.find_all(id=True):
        id['id'] = transform_id(id['id'], rel_url, should_slugify)

    for a in soup.find_all('a', href=True):
        if urls.url_is_absolute(a['href']) or os.path.isabs(a['href']):
            continue

        a['href'] = transform_href(a['href'], rel_url, should_slugify)

    soup.body['id'] = get_body_id(rel_url)
    soup = replace_asset_hrefs(soup, base_url)
    return soup


def get_separate(soup: BeautifulSoup, base_url: str, should_slugify=False):
    if should_slugify:
        for id in soup.find_all(id=True):
            id['id'] = slugify(id['id'])

        for a in soup.find_all('a', href=True):
            href = a['href']
            if urls.url_is_absolute(href) or os.path.isabs(href):
                continue

            if '#' in href:
                section, id = href.rsplit('#', 1)
                a['href'] = '{}#{}'.format(section, slugify(id))

    # transforms all relative hrefs pointing to other html docs
    # into relative pdf hrefs
    for a in soup.find_all('a', href=True):
        a['href'] = rel_pdf_href(a['href'])

    soup = replace_asset_hrefs(soup, base_url)
    return soup
