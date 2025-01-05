import logging

# Step 1: Create a logger object with the module's name
logger = logging.getLogger(__name__)

# Step 2: Set the logging level to INFO (captures INFO, WARNING, ERROR, and CRITICAL messages)
logger.setLevel(logging.INFO)

# Step 3: Create a StreamHandler to output log messages to the console
handler = logging.StreamHandler()

# Step 4: Define a formatter to specify the layout of log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Step 5: Attach the formatter to the handler
handler.setFormatter(formatter)

# Step 6: Add the handler to the logger
logger.addHandler(handler)
