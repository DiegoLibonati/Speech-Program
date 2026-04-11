from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE,
)


class TestMessages:
    def test_message_error_app_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)
        assert len(MESSAGE_ERROR_APP) > 0

    def test_message_not_valid_text_or_language_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE, str)
        assert len(MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE) > 0

    def test_message_not_found_dialog_type_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_distinct(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_TEXT_OR_LANGUAGE,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(messages) == len(set(messages))
