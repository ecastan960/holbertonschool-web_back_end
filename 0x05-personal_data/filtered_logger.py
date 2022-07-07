#!/usr/bin/env python3
"""_summary_
"""
import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """_summary_
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """_summary_

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
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
                             f'{data}={redaction}{separator}', log_message)
    return log_message
