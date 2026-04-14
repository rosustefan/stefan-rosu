import pytest
from pydantic import ValidationError

from app.content_schemas import PostFrontMatter


def test_post_front_matter_accepts_string_tags():
    metadata = PostFrontMatter.model_validate(
        {
            "title": "Example",
            "description": "Short summary",
            "tags": "python fastapi",
        }
    )

    assert metadata.tags == ["python", "fastapi"]


def test_post_front_matter_requires_title():
    with pytest.raises(ValidationError):
        PostFrontMatter.model_validate({"description": "Missing title"})
