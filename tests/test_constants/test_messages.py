import pytest

from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE,
)


class TestMessages:
    @pytest.mark.unit
    def test_error_app_message(self) -> None:
        assert MESSAGE_ERROR_APP == "Internal error. Contact a developer."

    @pytest.mark.unit
    def test_not_valid_text_or_language_message(self) -> None:
        assert MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE == (
            "You must enter a text and a language to be able to reproduce."
        )

    @pytest.mark.unit
    def test_not_found_dialog_type_message(self) -> None:
        assert MESSAGE_NOT_FOUND_DIALOG_TYPE == "The type of dialog to display is not found."
