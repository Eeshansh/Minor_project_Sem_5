from urllib.parse import urlparse
import re

def extract_demo_features(url):
    features = {}

    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    # BASIC URL FEATURES (dataset-aligned names)
    features["URLLength"] = len(url)
    features["DomainLength"] = len(domain)
    features["IsDomainIP"] = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", domain) else 0
    features["NoOfSubDomain"] = domain.count(".")
    features["TLDLength"] = len(domain.split(".")[-1]) if "." in domain else 0

    # Minimal safe defaults for remaining dataset columns
    DEFAULT_ZERO_COLUMNS = [
        "URLSimilarityIndex", "CharContinuationRate", "URLCharProb",
        "TLDLegitimateProb", "HasObfuscation", "NoOfObfuscatedChar",
        "ObfuscationRatio", "NoOfLettersInURL", "LetterRatioInURL",
        "NoOfEqualsInURL", "NoOfQMarkInURL", "NoOfAmpersandInURL",
        "NoOfOtherSpecialCharsInURL", "SpacialCharRatioInURL",
        "IsHTTPS", "LineOfCode", "LargestLineLength",
        "HasTitle", "DomainTitleMatchScore", "URLTitleMatchScore",
        "HasFavicon", "Robots", "IsResponsive", "NoOfURLRedirect",
        "NoOfSelfRedirect", "HasDescription", "NoOfPopup",
        "NoOfiFrame", "HasExternalFormSubmit", "HasSocialNet",
        "HasSubmitButton", "HasHiddenFields", "HasPasswordField",
        "Bank", "Pay", "Crypto", "HasCopyrightInfo",
        "NoOfImage", "NoOfCSS", "NoOfJS", "NoOfSelfRef",
        "NoOfEmptyRef", "NoOfExternalRef"
    ]

    for col in DEFAULT_ZERO_COLUMNS:
        features[col] = 0

    return features
