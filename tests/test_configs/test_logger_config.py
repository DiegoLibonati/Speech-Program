import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name_is_tkinter_app(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name_is_used(self) -> None:
        logger: logging.Logger = setup_logger(name="custom-logger")
        assert logger.name == "custom-logger"

    def test_logger_has_handler(self) -> None:
        logger: logging.Logger = setup_logger()
        assert len(logger.handlers) > 0

    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.level == logging.DEBUG

    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger(name="no-duplicate-test")
        count_first: int = len(logger.handlers)
        setup_logger(name="no-duplicate-test")
        count_second: int = len(logger.handlers)
        assert count_first == count_second
