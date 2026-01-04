from urllib.parse import urlparse
import re

def extract_demo_features(url):
    parsed = urlparse(url)

    features = {}

    # Simple, explainable features
    features["URLLength"] = len(url)
    features["DomainLength"] = len(parsed.netloc)
    features["IsDomainIP"] = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", parsed.netloc) else 0
    features["NoOfSubD"] = parsed.netloc.count(".")
    features["TLDLength"] = len(parsed.netloc.split(".")[-1])

    # Presence of suspicious characters
    features["CharContinuationRate"] = url.count("-") / len(url) if len(url) > 0 else 0
    features["DigitRatioInURL"] = sum(c.isdigit() for c in url) / len(url) if len(url) > 0 else 0

    return features
