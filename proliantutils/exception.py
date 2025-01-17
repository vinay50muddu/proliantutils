# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Exception Class for proliantutils module."""


class ProliantUtilsException(Exception):
    """Parent class for all Proliantutils exceptions."""
    pass


class InvalidInputError(Exception):

    message = "Invalid Input: %(reason)s"


class IloError(ProliantUtilsException):
    """Base Exception.

    This exception is used when a problem is encountered in
    executing an operation on the iLO.
    """
    def __init__(self, message, errorcode=None):
        super(IloError, self).__init__(message)


class IloClientInternalError(IloError):
    """Internal Error from IloClient.

    This exception is raised when iLO client library fails to
    communicate properly with the iLO.
    """
    def __init__(self, message, errorcode=None):
        super(IloClientInternalError, self).__init__(message)


class IloCommandNotSupportedError(IloError):
    """Command not supported on the platform.

    This exception is raised when iLO client library fails to
    communicate properly with the iLO
    """
    def __init__(self, message, errorcode=None):
        super(IloCommandNotSupportedError, self).__init__(message)


class IloCommandNotSupportedInBiosError(IloCommandNotSupportedError):
    """Command not supported on the bios boot mode.

    This exception is raised when iLO client library fails to
    communicate properly with the iLO
    """
    def __init__(self, message, errorcode=None):
        super(IloCommandNotSupportedInBiosError, self).__init__(message)


class IloLoginFailError(IloError):
    """iLO Login Failed.

    This exception is used to communicate a login failure to
    the caller.
    """
    messages = ['User login name was not found',
                'Login failed', 'Login credentials rejected']
    statuses = [0x005f, 0x000a]
    message = 'Authorization Failed'

    def __init__(self, message, errorcode=None):
        super(IloLoginFailError, self).__init__(message)


class IloConnectionError(IloError):
    """Cannot connect to iLO.

    This exception is used to communicate an HTTP connection
    error from the iLO to the caller.
    """
    def __init__(self, message):
        super(IloConnectionError, self).__init__(message)

# This is not merged with generic InvalidInputError because
# of backward-compatibility reasons. If we changed this,
# use-cases of excepting 'IloError' to catch 'IloInvalidInputError'
# will be broken.


class IloInvalidInputError(IloError):
    """Invalid Input passed.

    This exception is used when invalid inputs are passed to
    the APIs exposed by this module.
    """
    def __init__(self, message):
        super(IloInvalidInputError, self).__init__(message)


class HPSSAException(ProliantUtilsException):

    message = "An exception occured in hpssa module"

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message

        message = message % kwargs
        super(HPSSAException, self).__init__(message)


class PhysicalDisksNotFoundError(HPSSAException):

    message = ("Not enough physical disks were found to create logical disk "
               "of size %(size_gb)s GB and raid level %(raid_level)s")


class HPSSAOperationError(HPSSAException):

    message = ("An error was encountered while doing hpssa configuration: "
               "%(reason)s.")
