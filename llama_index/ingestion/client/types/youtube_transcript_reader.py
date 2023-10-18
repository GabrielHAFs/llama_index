# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.core.datetime_utils import serialize_datetime


class YoutubeTranscriptReader(pydantic.BaseModel):
    """
    Youtube Transcript reader.
    """

    is_remote: typing.Optional[bool]
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
