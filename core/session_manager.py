from datetime import datetime

peer_sessions = {}

def update_session(peer_name):
    peer_sessions[peer_name] = datetime.now()

def get_last_seen(peer_name):
    return peer_sessions.get(peer_name, "Never")
