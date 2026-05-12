import os
from unittest.mock import patch

import pytest

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    @pytest.mark.unit
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.DEBUG is False

    @pytest.mark.unit
    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.TESTING is False

    @pytest.mark.unit
    def test_tz_has_default_value_when_env_var_absent(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("TZ", None)
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "America/Argentina/Buenos_Aires"

    @pytest.mark.unit
    def test_env_name_has_default_value_when_env_var_absent(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("ENV_NAME", None)
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "template tkinter python"

    @pytest.mark.unit
    def test_tz_reads_from_env_var(self) -> None:
        with patch.dict(os.environ, {"TZ": "UTC"}):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "UTC"

    @pytest.mark.unit
    def test_env_name_reads_from_env_var(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "my-app"}):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "my-app"
