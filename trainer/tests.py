from django.test import TestCase
from .models import Trainer
from django.core.exceptions import ValidationError

class TrainerModelTest(TestCase):

    def setUp(self):
        # This method is called before each test
        self.trainer = Trainer.objects.create(
            first_name="Alice",
            last_name="Johnson",
            tsc_number=987654,
            email="alice.johnson@example.com",
            region="Nairobi",
            teachers_id=1
        )

    def test_trainer_creation(self):
        # Test that the trainer was created successfully
        self.assertIsInstance(self.trainer, Trainer)
        self.assertEqual(self.trainer.first_name, "Alice")
        self.assertEqual(self.trainer.last_name, "Johnson")
        self.assertEqual(self.trainer.tsc_number, 987654)
        self.assertEqual(self.trainer.email, "alice.johnson@example.com")
        self.assertEqual(self.trainer.region, "Nairobi")
        self.assertEqual(self.trainer.teachers_id, 1)

    def test_trainer_string_representation(self):
        # Test the string representation of the trainer
        self.assertEqual(str(self.trainer), "Alice Johnson")

    def test_email_validation(self):
        # Test that an invalid email raises a ValidationError
        trainer_with_invalid_email = Trainer(
            first_name="Bob",
            last_name="Smith",
            tsc_number=123456,
            email="invalid-email",  # Invalid email format
            region="Mombasa",
            teachers_id=2
        )
        
        with self.assertRaises(ValidationError):
            trainer_with_invalid_email.full_clean()  # This will validate the instance
