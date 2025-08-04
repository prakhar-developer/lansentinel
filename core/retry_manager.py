retry_queue = []

def add_to_retry(packet):
    retry_queue.append(packet)

def retry_all():
    for packet in retry_queue:
        try:
            from core.client import send_message
            send_message(packet.receiver_host, packet.receiver_port, packet)
            retry_queue.remove(packet)
        except:
            continue
