from typing import TypedDict

class HeartbeatResponse(TypedDict):
    status: str
    timestamp: str
    version: str

class AppInfo(TypedDict):
    id: int
    title: str
    description: int
    original_author: str
    slogan: str
    screenshot_urls: list[str]
    developer_site: str
    is_demo: bool
    is_under_dmca: bool
    icon_url: str

class Distribution(TypedDict):
    id: int
    app: int # App ID
    version: str
    link: str
    url: str
    has_download: bool
    published: str # Datetime of publishing

class KunyakinResponse(TypedDict):
    answer: str