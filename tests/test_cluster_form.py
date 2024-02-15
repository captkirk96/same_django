from django.db import models
from django.test import TestCase
from modelcluster.forms import ClusterForm


class MockChildModel(models.Model):
    name = models.CharField(max_length=255)

class MockParentModel(models.Model):
    children = models.ManyToManyField(MockChildModel, related_name='mock_children')

class MockClusterForm(ClusterForm):
    class Meta:
        model = MockParentModel
        fields = ['children']

class ClusterFormCustomFormsetNameTests(TestCase):
    def test_default_formset_name(self):
        form = MockClusterForm()
        self.assertIn('mock_children', form.formsets)

    def test_custom_formset_name(self):
        form = MockClusterForm(formset_names={'mock_children': 'custom_children'})
        self.assertNotIn('mock_children', form.formsets)
        self.assertIn('custom_children', form.formsets)

    def test_nonexistent_relation_formset_name(self):
        form = MockClusterForm(formset_names={'nonexistent_relation': 'should_not_exist'})
        self.assertNotIn('should_not_exist', form.formsets)
        self.assertNotIn('nonexistent_relation', form.formsets)

    def test_existing_tests_update(self):
        # Assuming there's a hypothetical test that previously relied on hardcoded formset names
        # This is a placeholder to indicate where such updates would occur
        pass
