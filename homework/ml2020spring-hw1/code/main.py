import pandas as pd
import os

# Specify the file path
DATA_DIR = "../data/"
TRAIN_FILE_PATH = os.path.join(DATA_DIR,"train.csv")

# function to load data and preprocess
def loadData(file_path):
    try:
        df_origin = pd.read_csv(file_path, encoding = "big5")
    except IOError:
        print("Error: file not existed!")
    print(df_origin)




def main():
    loadData(TRAIN_FILE_PATH);


main()

