# Data_Engineering_Projects
## Part 1 : Data Modeling with Postgres

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Datasets available

The song dataset is a subset of real data from the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.

The log dataset consists of log files in JSON format generated by [this event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

### Setup Instructions and Steps followed

* Install following packages before starting this project
  1. conda install -c anaconda psycopg2
  2. conda install -c conda-forge ipython-sql=0.3.6
* Set up a local PostgreSQL instance on port 5432. Please see detailed instructions in the [PostgreSQL documentation](https://www.postgresql.org/docs/9.1/runtime.html).

### Program execution

* Execute the script to generate the database and its tables by executing the file create_tables.ipyb on jupyter notebook.
* Load the data and insert it to the database by executing file etl.py on jupyter notebook.

### Schema Design

* The fact table `songplays` stores the records in log data associated with song plays i.e. records with page.
* The dimension table `users` stores the users in the app.
* The dimension table `song` stores the songs in the music database.
* The dimension table `artists` stores the artists the in music database.
* The dimension table `time` stores the timestamps of records in songplays broken down into specific units.

### Files 
  1. `test.ipynb` displays the first few rows of each table to let you check your database.
  2. create_tables.ipyb drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
  3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on        the ETL process for each of the tables.
  4. etl.ipynb reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
  5. sql_queries.ipynb contains all your sql queries, and is imported into the last three files above.
  6.README.md provides discussion on your project.
### Purpose of this database

This database allows to aggregate all songs, artists, users and songplays in a single database. In this way, the company disposes of the needed data stored in a unique structure and can thus analyze different scenarios easily. For instance, one can analyze the popularity of different songs or artists. Also, it is possible to perform analysis with geographic information. One can for instance determine which song is popular in which country and region.
