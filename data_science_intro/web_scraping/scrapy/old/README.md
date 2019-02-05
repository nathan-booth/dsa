# Scrapy Example

1. Create an environment for this project
2. Activate the environment
3. Navigate to project directory
4. Start a scrapy project with `scrapy startproject tutorial` of the form `scrapy startproject <project name>`
5. Use `scrapy crawl quotes` of the form `scrapy crawl <spider name>` to run the spider
6. Use the scrapy interactive shell to experiment with extracting elements: `scrapy shell 'htpL//quotes.toscrape.com/page/1/'` of the form `scrapy shell <URL>`
6. Run and save the output `scrapy crawl quotes -o quotes.json` of the form `scrapy crawl <spider name> -o <output filename>`
7. Run `python json-to-csv.py` to convert the JSON to CSV file.
