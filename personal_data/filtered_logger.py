#!/usr/bin/env python3
"""Filter Datum

This module provides a function to obfuscate specified fields in a log message.

"""

import re

def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message.

    Args:
        fields (list): A list of strings representing fields to obfuscate.
        redaction (str): A string representing the obfuscation value.
        message (str): A string representing the log line.
        separator (str): A string representing the character separating fields in the log line.

    Returns:
        str: The obfuscated log message.

    """
    return re.sub(fr'({separator.join(fields)})=(.*?){separator}', fr'\1={redaction}{separator}', message)
