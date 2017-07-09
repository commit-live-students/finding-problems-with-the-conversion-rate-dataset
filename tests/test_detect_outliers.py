from unittest import TestCase


class TestDetect_outliers(TestCase):
    def test_detect_outliers(self):
        from build import detect_outliers
        out = detect_outliers()
        self.assertListEqual(out, [123, 111])
