# This script is supposed to run through pipelines and generate a sales report from a CSV file.
# It reads a CSV file named 'sales.csv', processes the data, and generates a bar chart of total sales by product.
# this python should run through virtual environment
# This script should have reuirements.txt file
# make sure to handle errors gracefully and print appropriate messages

import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
        df = pd.read_csv('sales.csv')
    
        # Simple bar chart of sales by product
        df.groupby('Product')['Sales'].sum().plot(kind='bar', title='Total Sales by Product')
        plt.ylabel('Sales')
        plt.tight_layout()
        plt.savefig('sales_report.png')


if __name__ == '__main__':
    main()
