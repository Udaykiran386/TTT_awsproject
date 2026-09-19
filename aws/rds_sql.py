import pandas as pd
from sqlalchemy import create_engine, inspect, text

# 1. Credentials
LOCAL_USER = "postgres"
LOCAL_PASS = "root"
LOCAL_HOST = "localhost"
LOCAL_PORT = "5432"
LOCAL_DB   = "postgres"

RDS_USER = "postgres"
RDS_PASS = "YourRDSPassword123!"  # Ensure special characters are URL-encoded if present
RDS_HOST = "my-rds-postgres.cjuyycosmf6k.eu-north-1.rds.amazonaws.com"
RDS_PORT = "5432"
RDS_DB   = "postgres"

# 2. Engines
local_engine = create_engine(f"postgresql://{LOCAL_USER}:{LOCAL_PASS}@{LOCAL_HOST}:{LOCAL_PORT}/{LOCAL_DB}")
rds_engine   = create_engine(f"postgresql://{RDS_USER}:{RDS_PASS}@{RDS_HOST}:{RDS_PORT}/{RDS_DB}")

tables_to_migrate = ["emps", "departs", "projects"]

# 3. Migration
for table in tables_to_migrate:
    print(f"Reading '{table}' from Local Postgres...")
    with local_engine.connect() as local_conn:
        df = pd.read_sql_table(table, con=local_conn)
    
    print(f"Writing '{table}' to AWS RDS ({len(df)} rows)...")
    with rds_engine.connect() as rds_conn:
        # method="multi" batches batch inserts for faster transfer
        df.to_sql(table, con=rds_conn, if_exists="replace", index=False, method="multi")
        rds_conn.commit()
    
    print(f"Successfully migrated '{table}'!")

print("\n--- Verification ---")

# 4. Inspection & Verification
inspector = inspect(rds_engine)
print("RDS Tables found:", inspector.get_table_names())

with rds_engine.connect() as rds_conn:
    for table in tables_to_migrate:
        result = rds_conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
        print(f"Table '{table}' row count on RDS: {result.scalar()}")