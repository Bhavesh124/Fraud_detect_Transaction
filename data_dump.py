import pymongo
import json
#import pandas
import dask.dataframe as dd

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.4ajckbg.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "C:\Users\Suyash\Downloads\PS_20174392719_1491204439457_log.csv (1)\PS_20174392719_1491204439457_log.csv"
DATABASE_NAME = "Fraud_detection"
COLLECTION_NAME = "Transaction"


if __name__=="__main__":
    
    df=dd.read_csv(DATA_FILE_PATH,assume_missing=True)
    df=df.query('isFraud == 1')
    df = df.head(40,000)
    print(f"Rows and columns:",df.head())

    #df=df.compute()
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)