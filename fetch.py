#! /usr/bin/env python3

import re
import time

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playright):
    chromium = playwright.chromium

    browser = None
    try:
        browser = chromium.launch(headless=False, artifacts_dir='Downloads')
        page = browser.new_page()
        page.goto('https://www.avis.com/en/reservation/view-modify-cancel')

        page.locator('#onetrust-accept-btn-handler').click()

        page.get_by_placeholder('Enter your last name').fill('Strack')
        page.get_by_placeholder('Enter your number').fill('437635203')
        page.get_by_role("button", name=re.compile('Find Reservation')).click()
        print("clicked Find Reservation")
        time.sleep(2)

        with page.expect_download() as download_info:
            page.get_by_test_id('pdf-download-button').click()
            print("clicked Download pdf")
            time.sleep(2)
        download = download_info.value

        print(f"suggested_filename is '{ download.suggested_filename }'")
        print(f"download is '{ download }'")

    finally:
        if browser is not None:
            browser.close()

with sync_playwright() as playwright:
    run(playwright)
