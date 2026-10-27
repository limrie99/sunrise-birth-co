"""The required inquiry email uses the same label and span as the other fields."""

import pathlib
import re
import unittest

HTML = pathlib.Path(__file__).with_name("index.html").read_text(encoding="utf-8")
FORM = HTML.split('id="inquiryForm"', 1)[1].split("</form>", 1)[0]


class InquiryEmailLabelTest(unittest.TestCase):
    def test_required_email_uses_the_field_label_pattern(self):
        self.assertIsNotNone(
            re.search(
                r"<label>\s*"
                r"<span>Email</span>\s*"
                r'<input type="email" placeholder="Email" required name="email">\s*'
                r"</label>",
                FORM,
            )
        )
        bare = re.sub(r"<label>.*?</label>", "", FORM, flags=re.S)
        self.assertIsNone(re.search(r'<input type="email"', bare))


if __name__ == "__main__":
    unittest.main()
