import logging
from datetime import datetime
from kafka import KafkaProducer
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')    
)


def log_event(user_id, action, timestamp=None):
    if timestamp is None:
        timestamp = datetime.utcnow().isoformat()
    event_message = {
        'user_id': user_id,
        'action': action,
        'timestamp': timestamp
    }
    logger.info(f"Logging event: {event_message}")

    try:
        producer.send('your_topic_name', event_message)
        producer.flush()
    except Exception as e:
        logger.error(f"Failed to send event: {e}")


def close_producer():
    producer.close()
