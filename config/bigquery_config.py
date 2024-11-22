from google.oauth2 import service_account
import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def get_bigquery_credentials():
    return service_account.Credentials.from_service_account_file("config/credentials.json")

def get_bigquery_config():
    return config["bigquery_project_id"], config["bigquery_dataset"], config["bigquery_table"]
