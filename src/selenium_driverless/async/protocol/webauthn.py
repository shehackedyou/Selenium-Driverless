# Copyright 2017 Robert Charles Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# modified by kaliiiiiiiiii | Aurin Aegerter

# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# AuthenticatorId: 
AuthenticatorId = str

# AuthenticatorProtocol: 
AuthenticatorProtocol = str

# AuthenticatorTransport: 
AuthenticatorTransport = str

# VirtualAuthenticatorOptions: 
class VirtualAuthenticatorOptions(ChromeTypeBase):
    def __init__(self,
                 protocol: Union['AuthenticatorProtocol'],
                 transport: Union['AuthenticatorTransport'],
                 hasResidentKey: Union['bool'],
                 hasUserVerification: Union['bool'],
                 automaticPresenceSimulation: Optional['bool'] = None,
                 ):

        self.protocol = protocol
        self.transport = transport
        self.hasResidentKey = hasResidentKey
        self.hasUserVerification = hasUserVerification
        self.automaticPresenceSimulation = automaticPresenceSimulation


# Credential: 
class Credential(ChromeTypeBase):
    def __init__(self,
                 credentialId: Union['str'],
                 isResidentCredential: Union['bool'],
                 privateKey: Union['str'],
                 signCount: Union['int'],
                 rpId: Optional['str'] = None,
                 userHandle: Optional['str'] = None,
                 ):

        self.credentialId = credentialId
        self.isResidentCredential = isResidentCredential
        self.rpId = rpId
        self.privateKey = privateKey
        self.userHandle = userHandle
        self.signCount = signCount


class WebAuthn(PayloadMixin):
    """ This domain allows configuring virtual authenticators to test the WebAuthn
API.
    """
    @classmethod
    def enable(cls):
        """Enable the WebAuthn domain and start intercepting credential storage and
retrieval with a virtual authenticator.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disable the WebAuthn domain.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def addVirtualAuthenticator(cls,
                                options: Union['VirtualAuthenticatorOptions'],
                                ):
        """Creates and adds a virtual authenticator.
        :param options: 
        :type options: VirtualAuthenticatorOptions
        """
        return (
            cls.build_send_payload("addVirtualAuthenticator", {
                "options": options,
            }),
            cls.convert_payload({
                "authenticatorId": {
                    "class": AuthenticatorId,
                    "optional": False
                },
            })
        )

    @classmethod
    def removeVirtualAuthenticator(cls,
                                   authenticatorId: Union['AuthenticatorId'],
                                   ):
        """Removes the given authenticator.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        """
        return (
            cls.build_send_payload("removeVirtualAuthenticator", {
                "authenticatorId": authenticatorId,
            }),
            None
        )

    @classmethod
    def addCredential(cls,
                      authenticatorId: Union['AuthenticatorId'],
                      credential: Union['Credential'],
                      ):
        """Adds the credential to the specified authenticator.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        :param credential: 
        :type credential: Credential
        """
        return (
            cls.build_send_payload("addCredential", {
                "authenticatorId": authenticatorId,
                "credential": credential,
            }),
            None
        )

    @classmethod
    def getCredential(cls,
                      authenticatorId: Union['AuthenticatorId'],
                      credentialId: Union['str'],
                      ):
        """Returns a single credential stored in the given virtual authenticator that
matches the credential ID.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        :param credentialId: 
        :type credentialId: str
        """
        return (
            cls.build_send_payload("getCredential", {
                "authenticatorId": authenticatorId,
                "credentialId": credentialId,
            }),
            cls.convert_payload({
                "credential": {
                    "class": Credential,
                    "optional": False
                },
            })
        )

    @classmethod
    def getCredentials(cls,
                       authenticatorId: Union['AuthenticatorId'],
                       ):
        """Returns all the credentials stored in the given virtual authenticator.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        """
        return (
            cls.build_send_payload("getCredentials", {
                "authenticatorId": authenticatorId,
            }),
            cls.convert_payload({
                "credentials": {
                    "class": [Credential],
                    "optional": False
                },
            })
        )

    @classmethod
    def removeCredential(cls,
                         authenticatorId: Union['AuthenticatorId'],
                         credentialId: Union['str'],
                         ):
        """Removes a credential from the authenticator.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        :param credentialId: 
        :type credentialId: str
        """
        return (
            cls.build_send_payload("removeCredential", {
                "authenticatorId": authenticatorId,
                "credentialId": credentialId,
            }),
            None
        )

    @classmethod
    def clearCredentials(cls,
                         authenticatorId: Union['AuthenticatorId'],
                         ):
        """Clears all the credentials from the specified device.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        """
        return (
            cls.build_send_payload("clearCredentials", {
                "authenticatorId": authenticatorId,
            }),
            None
        )

    @classmethod
    def setUserVerified(cls,
                        authenticatorId: Union['AuthenticatorId'],
                        isUserVerified: Union['bool'],
                        ):
        """Sets whether User Verification succeeds or fails for an authenticator.
The default is true.
        :param authenticatorId: 
        :type authenticatorId: AuthenticatorId
        :param isUserVerified: 
        :type isUserVerified: bool
        """
        return (
            cls.build_send_payload("setUserVerified", {
                "authenticatorId": authenticatorId,
                "isUserVerified": isUserVerified,
            }),
            None
        )

