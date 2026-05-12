from tkinter import CENTER, FLAT

import pytest

from src.ui.styles import Styles


class TestStyles:
    @pytest.mark.unit
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#5800FF"

    @pytest.mark.unit
    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    @pytest.mark.unit
    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    @pytest.mark.unit
    def test_font_roboto_12(self) -> None:
        assert Styles.FONT_ROBOTO_12 == "Roboto 12"

    @pytest.mark.unit
    def test_font_roboto_13(self) -> None:
        assert Styles.FONT_ROBOTO_13 == "Roboto 13"

    @pytest.mark.unit
    def test_font_roboto_14(self) -> None:
        assert Styles.FONT_ROBOTO_14 == "Roboto 14"

    @pytest.mark.unit
    def test_font_roboto_15(self) -> None:
        assert Styles.FONT_ROBOTO_15 == "Roboto 15"

    @pytest.mark.unit
    def test_font_roboto_20(self) -> None:
        assert Styles.FONT_ROBOTO_20 == "Roboto 20"

    @pytest.mark.unit
    def test_center_matches_tkinter_constant(self) -> None:
        assert Styles.CENTER == CENTER

    @pytest.mark.unit
    def test_anchor_center_matches_tkinter_constant(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    @pytest.mark.unit
    def test_relief_flat_matches_tkinter_constant(self) -> None:
        assert Styles.RELIEF_FLAT == FLAT
