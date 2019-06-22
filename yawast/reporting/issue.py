import uuid
from typing import Union, List, cast

from yawast.reporting.enums import Vulnerabilities, VulnerabilityInfo
from yawast.scanner.plugins.result import Result


class Issue(dict):
    def __init__(
        self,
        vuln: Vulnerabilities,
        url: str,
        evidence: Union[str, List[str], None] = None,
    ):
        val = cast(VulnerabilityInfo, vuln.value)

        self.vulnerability = vuln
        self.severity = val.severity
        self.url = url
        self.evidence = evidence
        self.id = uuid.uuid4().hex

        dict.__init__(self, id=self.id, url=self.url, evidence=evidence)

    def __repr__(self):
        return f"Result: {self.id} - {self.vulnerability.name} - {self.url}"

    @classmethod
    def from_result(cls, result: Result):
        iss = cls(result.vulnerability, result.url, result.evidence)

        return iss