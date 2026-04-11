from tkinter import CENTER, FLAT

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#5800FF"

    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_roboto_base_name(self) -> None:
        assert Styles.FONT_ROBOTO == "Roboto"

    def test_font_roboto_12_contains_roboto_and_size(self) -> None:
        assert "Roboto" in Styles.FONT_ROBOTO_12
        assert "12" in Styles.FONT_ROBOTO_12

    def test_font_roboto_14_contains_roboto_and_size(self) -> None:
        assert "Roboto" in Styles.FONT_ROBOTO_14
        assert "14" in Styles.FONT_ROBOTO_14

    def test_font_roboto_20_contains_roboto_and_size(self) -> None:
        assert "Roboto" in Styles.FONT_ROBOTO_20
        assert "20" in Styles.FONT_ROBOTO_20

    def test_center_equals_tkinter_center(self) -> None:
        assert Styles.CENTER == CENTER

    def test_anchor_center_equals_center(self) -> None:
        assert Styles.ANCHOR_CENTER == Styles.CENTER

    def test_relief_flat_equals_tkinter_flat(self) -> None:
        assert Styles.RELIEF_FLAT == FLAT

    def test_all_font_sizes_are_distinct(self) -> None:
        fonts: list[str] = [
            Styles.FONT_ROBOTO_12,
            Styles.FONT_ROBOTO_13,
            Styles.FONT_ROBOTO_14,
            Styles.FONT_ROBOTO_15,
            Styles.FONT_ROBOTO_20,
        ]
        assert len(fonts) == len(set(fonts))
