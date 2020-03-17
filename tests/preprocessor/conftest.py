#!/usr/bin/env python
# coding=utf-8

import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def soup():
    return BeautifulSoup("""
<h1 id="chapter-1">chapter</h1>
<h2 id="section-1">chapter</h2>
<a href="/abs/path">abs path test</a>
<a href="https://url/abs/path">url abs path test</a>
<a href="../rel/#path">rel path test</a>
    """, features="html5lib")
