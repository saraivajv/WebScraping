from scraping.steamdb_scraper import scrape_steamdb_sales
from bigquery.bigquery_uploader import upload_to_bigquery
import pandas as pd

def main():
    data = scrape_steamdb_sales()
    df = pd.DataFrame(data)
    upload_to_bigquery(df)

if __name__ == '__main__':
    main()
