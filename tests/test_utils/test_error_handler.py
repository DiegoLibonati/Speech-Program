from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_calls_open_on_base_dialog_instance(self) -> None:
        dialog: ValidationDialogError = ValidationDialogError(message="Validation failed")
        with patch.object(dialog, "open") as mock_open:
            error_handler(type(dialog), dialog, None)
        mock_open.assert_called_once()

    def test_wraps_plain_exception_in_internal_dialog_error(self) -> None:
        exc: Exception = Exception("Some unexpected error")
        with patch("src.utils.error_handler.InternalDialogError") as mock_class:
            error_handler(type(exc), exc, None)
        mock_class.assert_called_once_with(message="Some unexpected error")
        mock_class.return_value.open.assert_called_once()

    def test_internal_error_receives_exception_message(self) -> None:
        exc: Exception = Exception("exact error text")
        captured_kwargs: list[dict[str, str]] = []

        def capture(*args: object, **kwargs: str) -> MagicMock:
            captured_kwargs.append(dict(kwargs))
            instance: MagicMock = MagicMock()
            return instance

        with patch("src.utils.error_handler.InternalDialogError", side_effect=capture):
            error_handler(type(exc), exc, None)

        assert captured_kwargs == [{"message": "exact error text"}]

    def test_does_not_wrap_base_dialog_in_internal_error(self) -> None:
        dialog: ValidationDialogError = ValidationDialogError(message="test")
        with patch("src.utils.error_handler.InternalDialogError") as mock_class:
            with patch.object(dialog, "open"):
                error_handler(type(dialog), dialog, None)
        mock_class.assert_not_called()
