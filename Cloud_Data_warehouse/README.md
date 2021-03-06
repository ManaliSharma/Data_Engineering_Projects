# Project Datawarehouse

## Project description

Sparkify is a music streaming startup with a growing user base and song database.

Their user activity and songs metadata data resides in json files in S3. The goal of the current project is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. 

## How to run

1. To run this project you will need to fill the following information, and save it as *dwh.cfg* in the project root folder.

```
[CLUSTER]
HOST=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_PORT=5439

[IAM_ROLE]
ARN=

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'

[AWS]
KEY=
SECRET=

[DWH]
DWH_CLUSTER_TYPE       = multi-node
DWH_NUM_NODES          = 4
DWH_NODE_TYPE          = dc2.large
DWH_CLUSTER_IDENTIFIER = 
DWH_DB                 = 
DWH_DB_USER            = 
DWH_DB_PASSWORD        = 
DWH_PORT               = 5439
DWH_IAM_ROLE_NAME      = 
```

2. Create a python environment with the dependencies listed on *requirements.txt*
- Use following commands
  - conda create -n yourenv pip
  - pip install -r requirements.txt
3. Run the *create_infrastructure* script to set up the needed infrastructure for this project.

    `$ python create_infrastructure.py`
    
4. Run the *check_Cluster_Avalabiliity* and *kill_Cluster* script to check availabilty status of cluster and to kill all the resources

    `$ python create_tables.py`

5. Run the *create_tables* script to set up the database staging and analytical tables

    `$ python create_tables.py`

6. Finally, run the *etl* script to extract data from the files in S3, stage it in redshift, and finally store it in the dimensional tables.

    `$ python etl.py`


## Project structure

This project includes five script files:

- analytics.py runs a few queries on the created star schema to validate that the project has been completed successfully.
- create_infrastructure.py is where the AWS components for this project are created programmatically
- create_tables.py is where fact and dimension tables for the star schema in Redshift are created.
- etl.py is where data gets loaded from S3 into staging tables on Redshift and then processed into the analytics tables on Redshift.
- sql_queries.py where SQL statements are defined, which are then used by etl.py, create_table.py and analytics.py.
- README.md is current file.
- requirements.txt with python dependencies needed to run the project

## Database schema design
![Alt text](https://github.com/ManaliSharma/Data_Engineering_Projects/blob/c8f833c6248398cd2787d1949e94a02fc1cc528f/Cloud_Data_warehouse/data-warehouse-project-der-diagram.png)
#### Staging Tables
- staging_events
- staging_songs

####  Fact Table
- songplays - records in event data associated with song plays i.e. records with page NextSong - 
*songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

#### Dimension Tables
- users - users in the app - 
*user_id, first_name, last_name, gender, level*
- songs - songs in music database - 
*song_id, title, artist_id, year, duration*
- artists - artists in music database - 
*artist_id, name, location, lattitude, longitude*
- time - timestamps of records in songplays broken down into specific units - 
*start_time, hour, day, week, month, year, weekday*


### Steps followed on this project

1. Create Table Schemas
- Design schemas for your fact and dimension tables
- Write a SQL CREATE statement for each of these tables in sql_queries.py
- Complete the logic in create_tables.py to connect to the database and create these tables
- Write SQL DROP statements to drop tables in the beginning of - create_tables.py if the tables already exist. This way, you can run create_tables.py whenever you want to reset your database and test your ETL pipeline.
- Launch a redshift cluster and create an IAM role that has read access to S3.
- Add redshift database and IAM role info to dwh.cfg.
- Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

2. Build ETL Pipeline
- Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
- Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
- Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.
- Delete your redshift cluster when finished.


