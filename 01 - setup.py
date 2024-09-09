# Databricks notebook source
# MAGIC %md
# MAGIC ##Setup Notebook

# COMMAND ----------

spark.read.csv(abfss://invoices@swethareddysa.dfs.core.windows.net/)
