from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, \
    RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Lesson, Payment
from courses.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, CourseDetailSerializer, \
    UserPaySerializer
from users.models import User


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# class LessonViewSet(ModelViewSet):
#     serializer_class = lessonSerializer
#     queryset = Lesson.objects.all()


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class CourseLessonDetailView(RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


class PaymentListView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class UserPaymentDetailView(RetrieveAPIView):
    serializer_class = UserPaySerializer
    queryset = User.objects.all()

