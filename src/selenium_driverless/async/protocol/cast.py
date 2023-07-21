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

# Sink: 
class Sink(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 id: Union['str'],
                 session: Optional['str'] = None,
                 ):

        self.name = name
        self.id = id
        self.session = session


class Cast(PayloadMixin):
    """ A domain for interacting with Cast, Presentation API, and Remote Playback API
functionalities.
    """
    @classmethod
    def enable(cls,
               presentationUrl: Optional['str'] = None,
               ):
        """Starts observing for sinks that can be used for tab mirroring, and if set,
sinks compatible with |presentationUrl| as well. When sinks are found, a
|sinksUpdated| event is fired.
Also starts observing for issue messages. When an issue is added or removed,
an |issueUpdated| event is fired.
        :param presentationUrl: 
        :type presentationUrl: str
        """
        return (
            cls.build_send_payload("enable", {
                "presentationUrl": presentationUrl,
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Stops observing for sinks and issues.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def setSinkToUse(cls,
                     sinkName: Union['str'],
                     ):
        """Sets a sink to be used when the web page requests the browser to choose a
sink via Presentation API, Remote Playback API, or Cast SDK.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("setSinkToUse", {
                "sinkName": sinkName,
            }),
            None
        )

    @classmethod
    def startTabMirroring(cls,
                          sinkName: Union['str'],
                          ):
        """Starts mirroring the tab to the sink.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("startTabMirroring", {
                "sinkName": sinkName,
            }),
            None
        )

    @classmethod
    def stopCasting(cls,
                    sinkName: Union['str'],
                    ):
        """Stops the active Cast session on the sink.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("stopCasting", {
                "sinkName": sinkName,
            }),
            None
        )



class SinksUpdatedEvent(BaseEvent):

    js_name = 'Cast.sinksUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 sinks: Union['[Sink]', dict],
                 ):
        if isinstance(sinks, dict):
            sinks = [Sink](**sinks)
        self.sinks = sinks

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class IssueUpdatedEvent(BaseEvent):

    js_name = 'Cast.issueUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 issueMessage: Union['str', dict],
                 ):
        if isinstance(issueMessage, dict):
            issueMessage = str(**issueMessage)
        self.issueMessage = issueMessage

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
