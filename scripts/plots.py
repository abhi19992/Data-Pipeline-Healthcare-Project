import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from db import engine

'''
This script generates various plots to visualize key metrics from the
messages_enriched table defined in step - 4 of documentation.
'''
# 1️. Active & Total Users Per Week
# ---------------------------------

users_sql = """
SELECT
    DATE_TRUNC('week', CAST(message_inserted_at AS TIMESTAMP)) AS week,
    COUNT(DISTINCT CASE WHEN LOWER(direction)='inbound' THEN masked_from_addr END) AS active_users,
    COUNT(DISTINCT CASE WHEN LOWER(direction)='inbound' THEN masked_from_addr
                       WHEN LOWER(direction)='outbound' THEN masked_addressees END) AS total_users
FROM message_enriched
WHERE CAST(message_inserted_at AS TIMESTAMP) BETWEEN '2023-11-01' AND '2023-11-30'

GROUP BY week
ORDER BY week;
"""
users = pd.read_sql(users_sql, engine)
fig1 = px.line(users, x='week', y=['active_users','total_users'], title="Active vs Total Users per Week")
fig1.show()

# 2️. Fraction of non-failed outbound messages read
# ---------------------------------

frac_sql = """
SELECT 
   SUM(CASE WHEN LOWER(direction)='outbound' AND failed_timestamp IS NULL AND read_timestamp IS NOT NULL THEN 1 ELSE 0 END) AS read_count,
   SUM(CASE WHEN LOWER(direction)='outbound' AND failed_timestamp IS NULL AND read_timestamp IS NULL THEN 1 ELSE 0 END) AS remaining_count
FROM message_enriched;
"""
result = pd.read_sql(frac_sql, engine)
df=result.melt(value_vars=['read_count','remaining_count'],var_name="status",value_name="count")
fig = px.pie(df, names="status", values="count",
                title="Read vs Remaining (Non-Failed Outbound Messages)",
                color="status",
                color_discrete_map={"read_count": "green", "remaining_count": "gray"})
fig.show()

# 3. Time to read distribution
# ---------------------------------

time_sql = """
SELECT
    EXTRACT(EPOCH FROM (read_timestamp::timestamp - sent_timestamp::timestamp))/60 AS time_to_read_minutes
FROM message_enriched
WHERE LOWER(direction)='outbound' AND failed_timestamp IS NULL AND read_timestamp IS NOT NULL;
"""
time_df = pd.read_sql(time_sql, engine)
fig2 = px.histogram(time_df, x='time_to_read_minutes', nbins=20, title="Distribution of Time to Read (minutes)")
fig2.show()

# 4. Outbound messages in last week by status
# ---------------------------------

status_sql = """
SELECT
    COUNT(sent_timestamp) AS sent,
    COUNT(delivered_timestamp) AS delivered,
    COUNT(read_timestamp) AS read,
    COUNT(failed_timestamp) AS failed,
    COUNT(deleted_timestamp) AS deleted
FROM message_enriched
WHERE LOWER(direction)='outbound'
  AND CAST(message_inserted_at AS TIMESTAMP) >= (SELECT MAX(message_inserted_at::timestamp) - INTERVAL '7 days' FROM message_enriched);
"""
status_counts = pd.read_sql(status_sql, engine)
print(status_counts)
status_counts = status_counts.melt(var_name='status', value_name='count')
print(status_counts)
fig3 = px.bar(status_counts, x='status', y='count', title='Outbound Messages in Last Week by Status')
fig3.show()
