# Serverless Metadata Scraper API
A cloud-native, serverless microservice built to scrape website metadata on-demand. This project demonstrates how to decouple applications logic from Infrastructure using AWS services and Iac concepts.

## Architecture Overview
A fully serverless architecture that ensures a high scalability and zero idle costs:
* **AWS API Gateway:** Acts as the entry point
* **AWS Lambda:** Executes the Python scraping logic ('BeautifulSoup4' & 'Requests') on demand
* **Amazon Cloudwatch:** Handles structured logging and error tracking.

## Tech Stack
* **Language** Python
* **Libs** Request & BeautifulSoup4
* **Cloud Provider** AWS
* **Version control** Git/Github

