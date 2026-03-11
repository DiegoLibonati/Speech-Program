from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE,
)


class TestMessages:
    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_not_valid_text_or_language_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE, str)

    def test_not_valid_text_or_language_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
