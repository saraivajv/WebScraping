from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def scrape_steamdb_sales():
    driver = webdriver.Chrome(executable_path=config['chromedriver_path'])
    driver.get(config['steamdb_url'])

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'app')))
    
    games = []
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.app')
    for row in rows:
        try:
            name = row.find_element(By.CSS_SELECTOR, 'td.b > a').text
            original_price = row.find_element(By.CSS_SELECTOR, 'td.price-discount__price').text
            discount_price = row.find_element(By.CSS_SELECTOR, 'td.price-discount__discount').text
            discount_percent = row.find_element(By.CSS_SELECTOR, 'td.price-discount__discount').text
            reviews = row.find_element(By.CSS_SELECTOR, 'td.rating').text

            games.append({
                'Nome': name,
                'Preço Original': original_price,
                'Preço com Desconto': discount_price,
                'Percentual de Desconto': discount_percent,
                'Avaliação': reviews
            })
        except Exception as e:
            print(f"Erro ao extrair dados: {e}")

    driver.quit()
    return games
