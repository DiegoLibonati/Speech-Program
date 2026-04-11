from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_error_constant_value(self) -> None:
        assert BaseDialog.ERROR == "Error"

    def test_warning_constant_value(self) -> None:
        assert BaseDialog.WARNING == "Warning"

    def test_info_constant_value(self) -> None:
        assert BaseDialog.INFO == "Info"

    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_is_error_app_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_init_with_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom message")
        assert dialog.message == "Custom message"

    def test_init_without_message_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_property_returns_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_title_property_returns_error_for_unknown_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        assert dialog.title == "Error"

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, str] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_values_are_correct(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Test msg")
        result: dict[str, str] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "Test msg"

    def test_open_calls_correct_handler_for_error(self) -> None:
        mock_handler: MagicMock = MagicMock()
        dialog: BaseDialog = BaseDialog(message="Test error")
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Error", "Test error")

    def test_open_with_unknown_dialog_type_shows_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()
        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_base_dialog_subclass(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, BaseDialog)

    def test_is_exception_subclass(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, Exception)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR

    def test_is_raiseable(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert error.message == "Validation error"

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="Invalid input")
        assert error.message == "Invalid input"

    def test_is_raiseable(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError(message="test")

    def test_is_base_dialog_error_subclass(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert isinstance(error, BaseDialogError)


class TestAuthenticationDialogError:
    def test_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()
        assert error.message == "Authentication error"

    def test_is_raiseable(self) -> None:
        with pytest.raises(AuthenticationDialogError):
            raise AuthenticationDialogError()


class TestNotFoundDialogError:
    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error.message == "Resource not found"

    def test_is_raiseable(self) -> None:
        with pytest.raises(NotFoundDialogError):
            raise NotFoundDialogError()


class TestConflictDialogError:
    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error.message == "Conflict error"

    def test_is_raiseable(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError()


class TestBusinessDialogError:
    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error.message == "Business rule violated"

    def test_is_raiseable(self) -> None:
        with pytest.raises(BusinessDialogError):
            raise BusinessDialogError()


class TestInternalDialogError:
    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()
        assert error.message == "Internal error"

    def test_custom_message(self) -> None:
        error: InternalDialogError = InternalDialogError(message="Something broke")
        assert error.message == "Something broke"

    def test_is_raiseable(self) -> None:
        with pytest.raises(InternalDialogError):
            raise InternalDialogError()


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.message == "This feature is deprecated"

    def test_title_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.title == "Warning"

    def test_open_calls_warning_handler(self) -> None:
        mock_handler: MagicMock = MagicMock()
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            warning.open()
        mock_handler.assert_called_once()

    def test_is_base_dialog_subclass(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert isinstance(warning, BaseDialog)


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.message == "Operation completed successfully"

    def test_title_is_information(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.title == "Information"

    def test_open_calls_info_handler(self) -> None:
        mock_handler: MagicMock = MagicMock()
        info: SuccessDialogInformation = SuccessDialogInformation()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            info.open()
        mock_handler.assert_called_once()

    def test_is_base_dialog_subclass(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert isinstance(info, BaseDialog)
