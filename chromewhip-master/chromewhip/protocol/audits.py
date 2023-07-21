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

