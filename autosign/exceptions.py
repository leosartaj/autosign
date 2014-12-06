"""
Contains various exceptions
"""

class TemplateError(Exception):
    """
    Raise when there is an error with the Template
    """
    pass

class UnsignedError(Exception):
    """
    Raise when file is unsigned, and sign is required
    for the operation
    """
    pass
