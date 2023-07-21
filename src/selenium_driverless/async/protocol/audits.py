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
from chromewhip.protocol import network as Network

class Audits(PayloadMixin):
    """ Audits domain allows investigation of page violations and possible improvements.
    """
    @classmethod
    def getEncodedResponse(cls,
                           requestId: Union['Network.RequestId'],
                           encoding: Union['str'],
                           quality: Optional['float'] = None,
                           sizeOnly: Optional['bool'] = None,
                           ):
        """Returns the response body and size if it were re-encoded with the specified settings. Only
applies to images.
        :param requestId: Identifier of the network request to get content for.
        :type requestId: Network.RequestId
        :param encoding: The encoding to use.
        :type encoding: str
        :param quality: The quality of the encoding (0-1). (defaults to 1)
        :type quality: float
        :param sizeOnly: Whether to only return the size information (defaults to false).
        :type sizeOnly: bool
        """
        return (
            cls.build_send_payload("getEncodedResponse", {
                "requestId": requestId,
                "encoding": encoding,
                "quality": quality,
                "sizeOnly": sizeOnly,
            }),
            cls.convert_payload({
                "body": {
                    "class": str,
                    "optional": True
                },
                "originalSize": {
                    "class": int,
                    "optional": False
                },
                "encodedSize": {
                    "class": int,
                    "optional": False
                },
            })
        )

