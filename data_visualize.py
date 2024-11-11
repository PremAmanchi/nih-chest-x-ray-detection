import pandas as pd
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the data
csv_file = 'chest-x-ray/Data_Entry_2017.csv'
try:
    df = pd.read_csv(csv_file)
    logging.info(f'Data loaded successfully from {csv_file}')
except FileNotFoundError:
    logging.error(f'File {csv_file} not found')
    exit()

# Display basic information about the data
logging.info(f'Data shape: {df.shape}')
logging.info(f'Data columns: {df.columns.tolist()}')
logging.info(f'Data types:\n{df.dtypes}')

# Visualize some data
plt.figure(figsize=(10, 5))
df['Finding Labels'].value_counts().plot(kind='bar')
plt.title('Distribution of Findings')
plt.xlabel('Finding Labels')
plt.ylabel('Count')
plt.show()
