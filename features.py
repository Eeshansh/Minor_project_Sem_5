import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}

    features['url_length'] = len(url)
    features['dot_count'] = url.count('.')
    features['has_at'] = 1 if '@' in url else 0
    features['has_https'] = 1 if url.startswith('https') else 0
    features['digit_count'] = sum(char.isdigit() for char in url)

    suspicious_words = ['login', 'verify', 'secure', 'update', 'bank']
    features['suspicious_word_count'] = sum(
        word in url.lower() for word in suspicious_words
    )

    # IP address check
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0

    return features
