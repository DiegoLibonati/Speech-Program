import pytest

from src.configs.development_config import DevelopmentConfig


class TestDevelopmentConfig:
    @pytest.mark.unit
    def test_debug_is_true(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()

        assert config.DEBUG is True

    @pytest.mark.unit
    def test_env_is_development(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()

        assert config.ENV == "development"

    @pytest.mark.unit
    def test_testing_is_false(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()

        assert config.TESTING is False
