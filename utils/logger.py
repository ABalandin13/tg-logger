import logging

# Create a custom logger
logger = logging.getLogger('my_project')

# Set the default log level
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()  # Console handler
f_handler = logging.FileHandler('app.log')  # File handler
c_handler.setLevel(logging.WARNING)  # Only log warnings to the console
f_handler.setLevel(logging.DEBUG)    # Log everything to a file

# Create formatters and add them to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)