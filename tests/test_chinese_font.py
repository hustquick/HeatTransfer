"""字体回退的基础测试：可在无图形界面的 CI 环境运行。"""
import unittest
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager

from Functions.Plotting import configure_chinese_font, _supports_chinese


class TestChineseFont(unittest.TestCase):
    def test_missing_font_reports_actionable_error(self):
        with patch.object(font_manager.fontManager, "ttflist", []), \
             patch("Functions.Plotting._BUNDLED_FONT") as bundled:
            bundled.is_file.return_value = False
            with self.assertRaisesRegex(RuntimeError, "install_chinese_font.py"):
                configure_chinese_font()

    def test_configure_returns_chinese_font_when_available(self):
        try:
            name = configure_chinese_font()
        except RuntimeError:
            self.skipTest("当前机器没有中文字体；可运行安装脚本后重试")
        self.assertIsInstance(name, str)
        self.assertTrue(name)

    def test_glyph_check_rejects_invalid_font(self):
        self.assertFalse(_supports_chinese("/path/that/does/not/exist.otf"))


if __name__ == "__main__":
    unittest.main()
