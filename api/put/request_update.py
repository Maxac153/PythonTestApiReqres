from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RequestUpdate:
    name: str
    job: str
