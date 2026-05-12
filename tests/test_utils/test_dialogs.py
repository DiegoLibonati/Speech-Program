from typing import Any
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
    @pytest.mark.unit
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    @pytest.mark.unit
    def test_default_message_is_error_app_constant(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    @pytest.mark.unit
    def test_custom_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom message")

        assert dialog.message == "Custom message"

    @pytest.mark.unit
    def test_message_none_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)

        assert dialog.message == MESSAGE_ERROR_APP

    @pytest.mark.unit
    def test_title_returns_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    @pytest.mark.unit
    def test_to_dict_contains_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == BaseDialog.ERROR

    @pytest.mark.unit
    def test_to_dict_contains_title(self) -> None:
        dialog: BaseDialog = BaseDialog()

        result: dict[str, Any] = dialog.to_dict()

        assert result["title"] == "Error"

    @pytest.mark.unit
    def test_to_dict_contains_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test message")

        result: dict[str, Any] = dialog.to_dict()

        assert result["message"] == "test message"

    @pytest.mark.unit
    def test_open_calls_showerror_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="err")
        mock_fn: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_fn}):
            dialog.open()

        mock_fn.assert_called_once_with("Error", "err")

    @pytest.mark.unit
    def test_open_calls_showwarning_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        dialog: WarningDialog = WarningDialog(message="warn")
        mock_fn: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            dialog.open()

        mock_fn.assert_called_once_with("Warning", "warn")

    @pytest.mark.unit
    def test_open_calls_showinfo_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        dialog: InfoDialog = InfoDialog(message="info")
        mock_fn: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            dialog.open()

        mock_fn.assert_called_once_with("Information", "info")

    @pytest.mark.unit
    def test_open_falls_back_to_showerror_for_unknown_type(self) -> None:
        class UnknownDialog(BaseDialog):
            dialog_type = "unknown_type"

        dialog: UnknownDialog = UnknownDialog()

        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()

        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    @pytest.mark.unit
    def test_is_instance_of_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, Exception)

    @pytest.mark.unit
    def test_is_instance_of_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, BaseDialog)

    @pytest.mark.unit
    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert error.dialog_type == BaseDialog.ERROR


class TestValidationDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_exception(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError(message="field required")

    @pytest.mark.unit
    def test_message_is_set(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="field required")

        assert error.message == "field required"

    @pytest.mark.unit
    def test_is_instance_of_base_dialog_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError()

        assert isinstance(error, BaseDialogError)


class TestAuthenticationDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(AuthenticationDialogError):
            raise AuthenticationDialogError(message="invalid credentials")

    @pytest.mark.unit
    def test_message_is_set(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError(message="invalid credentials")

        assert error.message == "invalid credentials"


class TestNotFoundDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(NotFoundDialogError):
            raise NotFoundDialogError(message="resource not found")

    @pytest.mark.unit
    def test_is_instance_of_base_dialog_error(self) -> None:
        assert isinstance(NotFoundDialogError(), BaseDialogError)


class TestConflictDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError(message="duplicate entry")

    @pytest.mark.unit
    def test_is_instance_of_base_dialog_error(self) -> None:
        assert isinstance(ConflictDialogError(), BaseDialogError)


class TestBusinessDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BusinessDialogError):
            raise BusinessDialogError(message="rule violated")

    @pytest.mark.unit
    def test_is_instance_of_base_dialog_error(self) -> None:
        assert isinstance(BusinessDialogError(), BaseDialogError)


class TestInternalDialogError:
    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(InternalDialogError):
            raise InternalDialogError(message="unexpected failure")

    @pytest.mark.unit
    def test_message_is_set(self) -> None:
        error: InternalDialogError = InternalDialogError(message="crash")

        assert error.message == "crash"


class TestSuccessDialogInformation:
    @pytest.mark.unit
    def test_dialog_type_is_info(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()

        assert dialog.dialog_type == BaseDialog.INFO

    @pytest.mark.unit
    def test_open_calls_showinfo(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation(message="Done")
        mock_fn: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            dialog.open()

        mock_fn.assert_called_once_with("Information", "Done")

    @pytest.mark.unit
    def test_is_not_an_exception(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()

        assert not isinstance(dialog, Exception)


class TestDeprecatedDialogWarning:
    @pytest.mark.unit
    def test_dialog_type_is_warning(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert dialog.dialog_type == BaseDialog.WARNING

    @pytest.mark.unit
    def test_open_calls_showwarning(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning(message="Deprecated feature")
        mock_fn: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            dialog.open()

        mock_fn.assert_called_once_with("Warning", "Deprecated feature")

    @pytest.mark.unit
    def test_is_not_an_exception(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert not isinstance(dialog, Exception)
