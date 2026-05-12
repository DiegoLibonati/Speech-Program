import logging

import pytest

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    @pytest.mark.unit
    def test_returns_logger_with_given_name(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-name-check")

        assert logger.name == "test-logger-name-check"

    @pytest.mark.unit
    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-handler-check")

        assert len(logger.handlers) >= 1

    @pytest.mark.unit
    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        name: str = "test-logger-no-dup"
        setup_logger(name)
        logger: logging.Logger = setup_logger(name)

        assert len(logger.handlers) == 1

    @pytest.mark.unit
    def test_default_name_is_tkinter_app(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    @pytest.mark.unit
    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-level-check")

        assert logger.level == logging.DEBUG
