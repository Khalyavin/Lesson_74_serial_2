# Generated by Django 4.1.5 on 2023-02-21 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="crss",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.course",
                verbose_name="Урок курса",
            ),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата оплаты"),
                ),
                ("summa", models.SmallIntegerField(verbose_name="Сумма")),
                (
                    "payment_form",
                    models.CharField(max_length=50, verbose_name="Форма оплаты"),
                ),
                (
                    "course_link",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "lesson_link",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={"verbose_name": "Оплата", "verbose_name_plural": "Оплата",},
        ),
    ]
