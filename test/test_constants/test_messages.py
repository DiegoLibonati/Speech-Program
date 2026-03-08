from src.constants.messages import MESSAGE_ERROR_NOT_TEXT_OR_LANGUAGE, MESSAGE_TEXT_YOUR_MSG


class TestMessages:
    def test_message_text_your_msg_is_string(self) -> None:
        assert isinstance(MESSAGE_TEXT_YOUR_MSG, str)

    def test_message_text_your_msg_is_not_empty(self) -> None:
        assert len(MESSAGE_TEXT_YOUR_MSG) > 0

    def test_message_error_not_text_or_language_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_NOT_TEXT_OR_LANGUAGE, str)

    def test_message_error_not_text_or_language_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_NOT_TEXT_OR_LANGUAGE) > 0
