import logging
from datetime import datetime
from kafka import KafkaProducer
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def log_event(user_id, action):
    event_message = {
        'user_id': user_id,
        'action': action,
        'timestamp': datetime.utcnow().isoformat()
    }
    logger.info(f"Logging event: {event_message}")
    producer.send('your_topic_name', event_message)
    producer.flush()
