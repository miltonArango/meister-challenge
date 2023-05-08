# Meister Data Processing

Meister Data Engineer Coding Assignment

* Test if the data of the previous table (or the augmented version of it) has any days without new sign-ups
* Has less than 5% of null values in the country column

## Installation

* Table must be available as a csv in the data folder

```bash
cd pipeline
python3 -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
```

## Usage

```bash
python processing.py
```

## Tests

```bash
python -m unittest tests/test.py
```

## Data Modeling

In order to analyze the impact of Twitter in terms of new subscribers it is necessary to build an ETL pipeline to process the raw data in a format usable for analytics purposes. The **recovery** and **storage** steps would be covered by the pipeline and the analysis step would require a different set of tools for visualization and analytics.

### Recover

* Identification of the input source and data schema. Depending on the input source a few design decisions must be made. If the input is a real-time stream from a message bus or if the input is an SQL table or a NoSQL document. This would define if the pipeline must be batch or streaming. In this step, the schema of the input is also important to define the transformations needed for the data. This includes parsing dates, denormalizing data fields, anonymization, and other transformations.

* After the input and schema have been defined, then the output structure of the data must be defined by the requirements of the data scientist or analysts. This will allow us to select the most convenient output format for the data (i.e. JSON, Parquet, CSV, ...) and also the transformations the data needs are influenced by this. For example, date formats, encoding, aggregate functions.

### Store

* Finally, once the _Recover_ step has been finished, it's time to store the data, depending on the design decisions of the previous step there are several options. For a streaming pipeline, the data can be stored in BigQuery using the stream ingest capabilities of the tool. For a batch pipeline, the output depends on where the processing is happening. It could be stored in Cloud Storage in a format appropriate for data analysis like Parquet where it can be easily accessed by the relevant stakeholders.

### Analyze

* Once the data is available in a suitable format, the data analysts or scientists can use it to answer business questions or to discover new insights using BigQuery analytic capabilities. For the visualization option, there are plenty of tools and platforms capable of using the data produced by the pipeline. In the Google ecosystem, Looker Studio is a suitable option for dashboards.

## Data compliance

After reviewing a few online sources [1], [2] and [3]. A list of processes can be derived from the sources to be GDPR compliant.

1. Data inventory and mapping: A process to identify all data belonging to a particular user.
2. Data retention policies: A set of guidelines that outlines how long the company should retain personal data, including when and how to delete it.
3. Data erasure or deletion procedures: A set of procedures that describe how to securely delete personal data from all systems and devices. This can be an automated process triggered on user request.
4. Data access and deletion request procedures: A process to enable individuals to request access to their personal data or request that it be deleted. It can be a web interface or a UI element on a mobile application.
5. Reporting: Keeping track of user's requests and enforcement of the retention policies.

## Data orchestration

In order to develop a system with table replication and materialized views it's necessary to use a database that supports High Availability configuration over network nodes and a data orchestration tool for scheduling and controlling the workflow (e.g. Apache Airflow).

* Configure the database for example PostgreSQL in HA mode to replicate the tables to a number of nodes that can handle the expected load.
* Writing the Materialized Views queries in SQL. Then, create a DAG in Airflow to define the view's creations task using Postgres to run the queries.
* Testing the outputs requires another DAG to validate the outputs of any transformation against the expected values. The testing code can be a Pytest script.
* Airflow provides a few deployment options that can be adjusted depending on the existing data infrastructure. The Airflow executor can be in distributed mode to provide scalability and error recovery.

## Sources

1. https://www.unique.ch/en/blog/software-companies-and-gdpr-compliance-everything-you-need-to-know
2. https://nordicdefender.com/blog/gdpr-compliance-checklist-and-gdpr-requirements-for-software-development
3. https://gdpr.eu/checklist/