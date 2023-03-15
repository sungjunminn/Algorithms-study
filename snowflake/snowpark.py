import os
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {
    "account" : os.environ["snowflake_account"],
    "user" : os.environ["snowflake_user"],
    "password" : os.environ["snowflake_password"],
    "role" : os.environ["snowflake_role"],
    "warehouse" : os.environ["snowflake_warehouse"],
    "database" : os.environ["snowflake_database"],
    "schema" : os.environ["snowflake_schema"]
}