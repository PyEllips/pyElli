import chardet


def detect_encoding(fname: str) -> str:
    r"""Detects the encoding of file fname.
    Args:
      fname (str): Filename
    Returns:
      str: Encoding identifier string.
    """
    with open(fname, "rb") as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result["encoding"]
