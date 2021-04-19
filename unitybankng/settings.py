BOT_NAME = 'unitybankng'

SPIDER_MODULES = ['unitybankng.spiders']
NEWSPIDER_MODULE = 'unitybankng.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'unitybankng.pipelines.UnitybankngPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
