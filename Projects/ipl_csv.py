import pandas as pd

df = pd.read_csv(r'C:\Users\Dell\Desktop\DataVisualization\Projects\ipl.csv')

if __name__ == "__main__":
    print(df.head())
    
    # Information about the DataFrame
    print(df.info())
    
    # Shape of the DataFrame
    print(df.shape)