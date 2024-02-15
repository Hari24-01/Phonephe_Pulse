#          __Phonephe_Pulse__
## __PhonePe Pulse Data Analysis 2018-2023 Project__ 

### PROBLEM STATEMENT:
The aim of this project is to create a Streamlit application with a visualisation dashboard that provides interactive and visually appealing insights on the Phonepe pulse Github repository.

### PLATFORMS USED:
PYTHON ; GITHUB CLONING ; XAMPP SQL ; STREAMLIT AND PLOTLY

### LIBRARY USED:
gitpython, pandas, plotly.express, streamlit, streamlit_option_menu, mysql.connector, sqlalchemy(create_engine), PIL, sklearn.

### PROCEDURE:
* #### __STEP 1:__ Connecting To Github Repository For Data Extraction:
   Cloning the Phonepe Pulse Github repository with ["gitpython"](), then retrieving the data and saving it in the proper format (JSON or CSV).
* #### __STEP 2:__ Data Cleaning:
  Using [Python]() and [Pandas]() are used for data manipulation and pre-processing, which includes data cleansing, addressing missing values, and transforming data 
  formats for analysis and visualisation.
* #### __STEP 3:__ Data Insertion in MYSQL Server:
  The "mysql-connector-python" Python package is used to connect to a MySQL database and insert converted data in JSON or CSV format using SQL commands.
#### __STEP 4:__ Migrate data to a SQL data warehouse:
Using a SQL database like MySQL or XAMPPSQL, the data collected from multiple channels, including channel details, videos, and comments, is moved to a SQL data warehouse.
#### __STEP 5:__ Query the SQL data warehouse:
Use SQL queries to link tables in a data warehouse and obtain channel data depending on user input, while ensuring correct foreign and primary key assignment.
#### __STEP 6:__ Display data in the Streamlit app:
The obtained data is shown within the Streamlit application, where it is used to build charts and graphs for user analysis.
#### __STEP 7:__ OUTPUT:
