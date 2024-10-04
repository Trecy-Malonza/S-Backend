from django.test import TestCase
from .models import Teacher

class TeacherModelTest(TestCase):

    def setUp(self):
        # This method is called before each test
        self.teacher = Teacher.objects.create(
            first_name="John",
            last_name="Doe",
            tsc_number="123456",
            email="john.doe@example.com",
            region="Nairobi",
            school="Nairobi High School",
            teachers_id=1
        )

    def test_teacher_creation(self):
        # Test that the teacher was created successfully
        self.assertIsInstance(self.teacher, Teacher)
        self.assertEqual(self.teacher.first_name, "John")
        self.assertEqual(self.teacher.last_name, "Doe")
        self.assertEqual(self.teacher.tsc_number, "123456")
        self.assertEqual(self.teacher.email, "john.doe@example.com")
        self.assertEqual(self.teacher.region, "Nairobi")
        self.assertEqual(self.teacher.school, "Nairobi High School")
        self.assertEqual(self.teacher.teachers_id, 1)

    def test_teacher_string_representation(self):
        # Test the string representation of the teacher
        self.assertEqual(str(self.teacher), "John Doe")

    def test_email_uniqueness(self):
        # Test that the email field must be unique
        with self.assertRaises(Exception):
            Teacher.objects.create(
                first_name="Jane",
                last_name="Smith",
                tsc_number="654321",
                email="john.doe@example.com",  # Same email as the first teacher
                region="Mombasa",
                school="Mombasa High School",
                teachers_id=2
            )
