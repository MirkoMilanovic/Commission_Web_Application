from django.test import SimpleTestCase
from ReportApp.forms import RatesForm


class TestForms(SimpleTestCase):
    def test_rates_form_validator(self):
        form = RatesForm(data={'city': 'LONDON'})

        self.assertTrue(form.is_valid())


    def test_rates_form_no_data(self):
        form = RatesForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
