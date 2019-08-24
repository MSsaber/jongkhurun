#!/usr/bin/python
# -*- coding: utf-8 -*-

import Log
import re
import logging
import itertools
import urllib.request
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib import robotparser

def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    logging.info('Download from ' + url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        logging.info('Download error ' + url + ' ' + e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1, charset)
    return html

def get_links(html):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)

def link_crawler(start_url, link_regex):
    crawl_queue = [start_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop(0)
        html = download(url)
        if not html:
            continue
        for link in get_links(html):
            # logging.debug(link[15:])
            if re.match(link_regex, link[15:]):
                abs_link = urljoin(start_url, link)
                if abs_link not in seen:
                    seen.add(abs_link)
                    crawl_queue.append(abs_link)

def crawl_sitemap(url):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        if not html:
            break

def get_robot_parser(robot_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robot_url)
    rp.read()
    return rp

Log.JLogging(File=True, Function=True, LogLevel=True, Line=True, LogFile='../JongRun.log')
link_crawler('http://example.python-scraping.com', '/(index|view)/')
#crawl_sitemap('http://example.python-scraping.com/view/-')