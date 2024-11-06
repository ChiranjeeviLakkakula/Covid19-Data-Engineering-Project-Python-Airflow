# _Covid19 Data Engineering Project_

## _Introduction_
In this project I have built an ETL(Extract, Transform, Load) pipeline using the Covid19 API on Airflow.
The pipeline will extract data from Covid19 API, transform it into desired format and load into AWS data store using Airflow installed on Docker.

## _Architecture - End to End ETL Pipeline_
![Architecture Diagram](https://github.com/ChiranjeeviLakkakula/Covid19-Data-Engineering-Project-Python-Airflow/blob/main/Covid19-Airflow-Architecture.jpg)

## _About Dataset/API_
The Covid19 collection includes APIs that provide data on new cases, deaths, and local infection rates. The data is sourced from top medical institutions and is available in JSON format. For this project I have taken the overall covid statistics across continents.

API documentation - [Covid19 API](https://api-sports.io/documentation/covid-19)

## _Language Used_

**Python** 
1. Used python to extract data from Covid19 API into JSON format.
2. Converted the extracted data set into Dataframe and performed transformation.
3. Created Airflow DAG and tasks for data extract and AWS S3 load.

## _Services Used_

1. **AWS S3:** Amazon S3 (Simple Storage Service) is a cloud-based object storage service provided by Amazon Web Services (AWS). It offers scalability, data availability, security, and performance to store and manage any amount of data for various use cases like data lakes, websites, mobile applications, and big data analytics

2. **Apache Airflow:** Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It allows you to define complex workflows as code and orchestrate them efficiently.

3. **Docker:**: Docker is an open-source platform that automates the deployment of applications inside lightweight, portable containers. It enables developers to package applications and their dependencies into a standardized unit for consistent development and deployment across different environments.

## _Python Packages Used_
````
pip install pandas
````

## _Data Pipeline flow_

Extract Data from Covid19 API using Airflow -> Load the extract into AWS S3 using Airflow
