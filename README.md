# Steam Workshop Comments Scraper

## Overview

This repo contains a programm written for a seminar at the Goethe University of Frankfurt am Main.
The "Steam Workshop Comments Scraper" is a web scraping project built using Scrapy and Scrapy-Playwright. 
Its build on the following tutorial-series: https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t and optimized for the javascript elements that the Steam Webpage has. 
This project aims to collect comments from a specific Steam Workshop page and save them for further analysis.
The maincode can be found under spiders - Steam Crawler.py. 
Execute the Crawler by writing the following in the command line, if you expect the output to be small enough you can save it in a csv file like so: 
scrapy crawl 81tiles -o data.csv



## Features

- Scrapes comments from a Steam Workshop page using Scrapy and Scrapy-Playwright.
- Handles pagination to scrape comments from multiple pages.
- Saves scraped comments to a structured format for analysis.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Scrapy
- Scrapy-Playwright
- Playwright
