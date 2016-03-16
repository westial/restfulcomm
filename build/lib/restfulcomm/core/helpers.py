# -*- coding: utf-8 -*-
"""Helpers for common uses
"""
import re


class HttpHelper(object):

    @classmethod
    def is_plain_content_type(cls, content_type):
        """Return True if the given content type is plain text

        Args:
                content_type: str

        Return:
                bool
        """
        return bool(re.match("text/[^\s]+", content_type, re.I))
