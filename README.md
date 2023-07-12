# scrapy_laptops_in_retail_stores

scrapy_laptops_in_retail_stores

## Init git Repo

1. Init git repo

## Init scrapy

1. Create a Project => `scrapy startproject scrapy_laptops_in_retail_stores`
    1. This will create a tutorial directory and contents.

## Init python project

1. install virtualenv `virtualenv venv`
1. activate virtualenv `source venv/Scripts/activate` (on linux | can use git bash console on windows)
1. create requirements.txt file and add (only scrapy /ˈskreɪpaɪ/ is mandatory)
    1. scrapy
    1. ipython
    1. ~~pprint~~ => this is not necessary. pprint is part of the Python standard library
1. and install it with `pip install -r requirements.txt`

## Main Steps

1. try the shell to obtain values from a response:
    1. Run: `scrapy shell https://www.oechsle.pe/tecnologia/computo/laptops`
    1. Run: `scrapy shell https://www.oechsle.pe/tecnologia/computo/laptops?page=1`
    1. Run: `scrapy shell https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=4`
        1. try selectors
            1. `x=response.css("div.product.instock")`
            1. `x[0].attrib['data-name'].get()`
            1. `x[0].attrib['data-name']`
        1. keep searching for the right selectors
        1. or run: `view(response)` inside the scrapy shell to open the response in a tmp browser
1. Add spiders. use this command: `scrapy genspider <spider_name> <start_url>`
    1. run: `scrapy genspider laptopsRipley https://simple.ripley.com.pe/tecnologia/computacion/laptops?source=menu&s=mdco`
    1. run: `scrapy genspider laptopsOechsle https://www.oechsle.pe/tecnologia/computo/laptops`
1. test spider:
    1. run: `scrapy crawl laptopsOechsle -o laptops.jsonl`
1. Add Type
1. Add Pipeline
