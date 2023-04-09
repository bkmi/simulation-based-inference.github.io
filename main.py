from scholar.api import crawl

SEARCH_TERM = '"simulation-based+inference"'

if __name__ == '__main__':
    # crawl(SEARCH_TERM)  # For crawling all results (start a new database)
    crawl(SEARCH_TERM, stop_days=14)  # For crawling only the last 14 days (simulate google scholar alerts)