from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateView, LessonDeleteView, \
    LessonListView, LessonDetailView, LessonUpdateView, \
    PaymentListView, UserPaymentDetailView, CourseLessonDetailView

urlpatterns = [
    path('create/', LessonCreateView.as_view()),
    path('delete/<int:pk>/', LessonDeleteView.as_view()),
    path('', LessonListView.as_view()),
    path('detail/<int:pk>/', LessonDetailView.as_view()),
    path('update/<int:pk>/', LessonUpdateView.as_view()),

    path('<int:pk>/', CourseLessonDetailView.as_view()),  # По УРЛу вывожу № курса и количество уроков в нем

    path('pay/', PaymentListView.as_view()),  # По УРЛу идет вывод всех платежей
    path('pay/user/<int:pk>/', UserPaymentDetailView.as_view()),  # По УРЛу идет вывод юзера и всех его платежей
]

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls
