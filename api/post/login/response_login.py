from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResponseLoginSuccess:
    token: str


@dataclass_json
@dataclass
class ResponseLoginUnsuccess:
    error: str
