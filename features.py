from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    features = {}

    features["having_IP_Address"] = 1 if parsed.hostname and parsed.hostname.replace(".", "").isdigit() else -1
    features["URL_Length"] = len(url)
    features["Shortining_Service"] = 1 if "bit.ly" in url else -1
    features["having_At_Symbol"] = 1 if "@" in url else -1
    features["double_slash_redirecting"] = 1 if url.count("//") > 1 else -1
    features["Prefix_Suffix"] = 1 if "-" in parsed.hostname else -1
    features["having_Sub_Domain"] = 1 if parsed.hostname.count(".") > 2 else -1
    features["SSLfinal_State"] = 1 if parsed.scheme == "https" else -1

    return features
