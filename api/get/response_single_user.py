from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Data:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


@dataclass_json
@dataclass
class Support:
    url: str
    text: str


@dataclass_json
@dataclass
class SingleUser:
    data: Data
    support: Support
