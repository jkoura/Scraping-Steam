import scrapy
import asyncio
from scrapy_playwright.page import PageMethod
from scrapy.selector import Selector
from ..items import WorkshopCommentsItem

class A81tilesSpider(scrapy.Spider):
    name = '81tiles' # select a Name that will call the Spider
    start_urls = ['https://steamcommunity.com/sharedfiles/filedetails/?id=2881031511'] # Change the Url here

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "div.commentthread_comment_container", timeout=600)
                ],
                "page_number": 1,
                "page_count": 0
            }
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        page_number = response.meta["page_number"]
        page_count = response.meta["page_count"]
        while True:
            try:
                cookie_popup = await page.query_selector('#rejectAllButton')
                await page.wait_for_selector('#rejectAllButton', state='visible', timeout=400)
                await cookie_popup.click()
                await page.wait_for_selector(
                    "#commentthread_PublishedFile_Public_76561198262198841_2881031511_fpagebtn_next", state='visible',
                    timeout=400)
            except:
                pass

            await page.wait_for_selector('div.commentthread_comment_container')

            content = await page.content() 
            selector = Selector(text=content)  
            for comment in selector.css("div.commentthread_comment"):
                steam_item = WorkshopCommentsItem(
                    post_time=comment.xpath(".//span[@class='commentthread_comment_timestamp']/text()").get().strip(),
                    post_content=comment.xpath(".//div[@class='commentthread_comment_text']/text()").get().strip(),
                    post_author=comment.xpath(".//bdi/text()").get().strip()
                )
                yield steam_item

            # Check if there are more pages
            next_page_available = await page.evaluate(
                "(function(){return Boolean(document.querySelector('#commentthread_PublishedFile_Public_76561198262198841_2881031511_fpagebtn_next:not([disabled])'));})()")

            if next_page_available and page_count < 45:

                print("Clicking on Next button")
                await page.click("#commentthread_PublishedFile_Public_76561198262198841_2881031511_fpagebtn_next")

                page_number += 1
                page_count += 1
                print(f"Processing page {page_number}")

                response.meta["page_number"] = page_number
                response.meta["page_count"] = page_count
                try:
                    await page.wait_for_selector("div.commentthread_comment_container", timeout=600)
                except:
                    pass
            else:
                break

        await page.close()
















