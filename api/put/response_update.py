from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResponseUpdate:
    id: str
    name: str
    job: str
    createdAt: str
