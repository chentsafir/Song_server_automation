import logging

# Step 1: Create a logger object with the module's name
logger = logging.getLogger(__name__)

# Step 2: Set the logging level for the logger to INFO
logger.setLevel(logging.INFO)

# Step 3: Create a StreamHandler for console output
console_handler = logging.StreamHandler()

# Step 4: Define a formatter for the console handler
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Step 5: Attach the formatter to the console handler
console_handler.setFormatter(console_formatter)

# Step 6: Add the console handler to the logger
logger.addHandler(console_handler)

# Step 7: Create a FileHandler for error logs
error_file_handler = logging.FileHandler('error.log')

# Step 8: Set the logging level for the FileHandler to ERROR
error_file_handler.setLevel(logging.ERROR)

# Step 9: Define a formatter for the error file handler
error_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Step 10: Attach the formatter to the error file handler
error_file_handler.setFormatter(error_file_formatter)

# Step 11: Add the error file handler to the logger
logger.addHandler(error_file_handler)