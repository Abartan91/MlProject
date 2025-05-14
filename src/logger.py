import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log filename with timestamp
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Create a logger instance
logger = logging.getLogger(__name__)
