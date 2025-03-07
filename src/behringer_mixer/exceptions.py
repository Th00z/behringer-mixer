"""
Module for Exceptions in the Behringer Mixer Context
"""

class BehringerMixerException(Exception):
    """
    Base Exception Class for anything in the Behringer Mixer Context.
    """
    pass


class ClientException(BehringerMixerException):
    """
    Base Exception Class for exceptions in the context of the mixer clients.
    """
    pass


class NoResponseException(ClientException):
    """
    Exception that gets raised when trying to access a client response that is not there (yet).
    """
    pass
