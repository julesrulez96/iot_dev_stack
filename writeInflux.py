from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "VgxNX-i8i-aUpAAoVGq0X33Xtlhp_9hXZp1TQBseN14lFPDGFMWPi0HKfZaJ_UZLZ4GYRE55HGNfZdlKuK796w=="
org = "dev"
bucket = "testdb"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)