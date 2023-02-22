from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson, Payment
from users.models import User


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


# В сериалайзер курсов добавил поле уроков для отражения при выводе курса
class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, source='lesson_set')

    class Meta:
        model = Course
        fields = '__all__'


# Сериализатор для вывода курса и кол-ва уроков в нем
class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_of_course = SerializerMethodField()

    def get_lessons_of_course(self, course):
        return course.lesson_set.filter(crss=course.id).count()

    class Meta:
        model = Course
        fields = ('name', 'lessons_of_course')


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserPaySerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, source='payment_set')

    class Meta:
        model = User
        fields = (
            'email',
            'town',
            'payment'
        )
