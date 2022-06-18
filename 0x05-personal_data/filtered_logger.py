#!/usr/bin/env python3
"""_summary_
"""
import re


def filter_datum(fields, redaction, message, separator):
    """_summary_

    Args:
        fields (_type_): _description_
        redaction (_type_): _description_
        message (_type_): _description_
        separator (_type_): _description_

    Returns:
        _type_: _description_
    """
    for data in fields:
        log_message = re.sub(fr'{data}=.+?{separator}',
                             f'{data}={redaction}{separator}', message)
    return log_message
