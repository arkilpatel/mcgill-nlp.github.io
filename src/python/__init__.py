import urllib.request


def parse_issue_body(body):
    """
    Parse the body of the issue and return a dictionary of the parsed data.
    """
    parsed = {}
    k = None

    for line in body.split("\n"):
        if line.startswith("###"):
            k = line.removeprefix("###").strip().lower().replace(" ", "_")
            parsed[k] = ""
        else:
            if k is not None:
                parsed[k] += line.strip()

    return parsed

def save_url_image(fname, profile, key, path):
    if key in profile and profile[key].startswith("http"):
        ext = profile[key].split(".")[-1]
        file_path = f"{path}/{fname}.{ext}"
        urllib.request.urlretrieve(profile[key], file_path)
        profile[key] = "/" + file_path