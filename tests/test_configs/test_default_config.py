import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_tz_default_value(self) -> None:
        filtered_env: dict[str, str] = {k: v for k, v in os.environ.items() if k != "TZ"}
        with patch.dict(os.environ, filtered_env, clear=True):
            config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_tz_from_environment_variable(self) -> None:
        with patch.dict(os.environ, {"TZ": "Europe/Madrid"}):
            config: DefaultConfig = DefaultConfig()
        assert config.TZ == "Europe/Madrid"

    def test_env_name_default_value(self) -> None:
        filtered_env: dict[str, str] = {k: v for k, v in os.environ.items() if k != "ENV_NAME"}
        with patch.dict(os.environ, filtered_env, clear=True):
            config: DefaultConfig = DefaultConfig()
        assert config.ENV_NAME == "template tkinter python"

    def test_env_name_from_environment_variable(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "my-app"}):
            config: DefaultConfig = DefaultConfig()
        assert config.ENV_NAME == "my-app"
