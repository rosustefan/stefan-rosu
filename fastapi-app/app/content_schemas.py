from pydantic import BaseModel, ConfigDict, Field, field_validator


class PostFrontMatter(BaseModel):
    title: str = Field(min_length=1)
    description: str | None = None
    tags: list[str] = Field(default_factory=list)

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    @field_validator("tags", mode="before")
    @classmethod
    def normalize_string_or_list(cls, value: str | list[str] | None) -> list[str]:
        if value is None:
            return []
        if isinstance(value, str):
            return [item for item in value.split() if item]
        return [str(item).strip() for item in value if str(item).strip()]
