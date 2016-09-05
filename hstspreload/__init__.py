import os, sys, gzip, json

with gzip.open(os.path.join(os.path.dirname(__file__), "hsts_preload_domains.json.gz")) as fh:
    hsts_preload_domains = set(json.loads(fh.read().decode()))

def in_hsts_preload(hostname):
    parts = hostname.rsplit(".", 4)
    for i in range(len(parts)):
        superdomain = ".".join(parts[len(parts)-i-1:])
        if superdomain in hsts_preload_domains:
            return True
    return False
