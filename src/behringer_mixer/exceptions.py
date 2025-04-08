"""
Module for Exceptions in the Behringer Mixer Context
"""
class BehringerMixerException(Exception):
    """
    Base Exception Class for anything in the Behringer Mixer Context.
    """
    pass


class ComponentOutOfBoundsException(BehringerMixerException):
    """

    """
    pass


class ClientException(BehringerMixerException):
    """
    Base Exception Class for exceptions in the context of the mixer clients.
    """
    path: str | None

    def __init__(self, message = "", path: str | None = None):
        """

        :param message:
        :param path:
        """
        self.path = path
        super().__init__(message)

    def __str__(self):
        """

        :return:
        """
        if self.path is not None:
            return f"{self.path} :: {super().__str__()}"
        return super().__str__()


class EndpointException(ClientException):
    """

    :param ClientException:
    :return:
    """
    pass


class NoResponseException(ClientException):
    """
    Exception that gets raised when trying to access a client response that is not there (yet).
    """
    pass


class QueryException(ClientException):
    """

    """
    pass


class IllegalQueryException(QueryException):
    """

    """
    pass


class InvalidResponseException(QueryException):
    """
    Exception that gets raised when receiving a response that is not valid for the endpoint.
    """
    pass
