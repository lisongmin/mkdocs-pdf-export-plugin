#!/usr/bin/env python
# coding=utf-8

import logging
import pytest
from mkdocs_pdf_export_plugin.preprocessor.prep \
    import get_combined, get_separate


def test_get_combined(soup):
    result = get_combined(soup, 'c', 'a/b/')

    assert result.find(attrs={'id': 'a/b/:chapter-1'})
    assert result.find(attrs={'id': 'a/b/:section-1'})

    assert result.find(attrs={'href': '/abs/path'})
    assert result.find(attrs={'href': 'https://url/abs/path'})

    assert result.find(attrs={'href': '#a/rel/:path'})


def test_get_seperate(soup):
    result = get_separate(soup, 'a/b/', True)

    assert result.find(attrs={'id': 'chapter-1'})
    assert result.find(attrs={'id': 'section-1'})

    assert result.find(attrs={'href': '/abs/path'})
    assert result.find(attrs={'href': 'https://url/abs/path'})

    assert result.find(attrs={'href': '../rel/#path'})
