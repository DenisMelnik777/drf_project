from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'preview', 'description')


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = IntegerField()

    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'lessons_count')


class CourseDetailSerializer(serializers.ModelSerializer):
    this_course_lessons = SerializerMethodField()

    def get_this_course_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course_lesson=course)]

    class Meta:
        model = Course
        fields = ('pk', 'title', 'preview', 'description', 'this_course_lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'preview', 'course_lesson')


class LessonListSerializer(serializers.ModelSerializer):
    course_lesson = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'preview', 'course_lesson')


class LessonDetailSerializer(serializers.ModelSerializer):
    course_lesson = CourseSerializer()
    count_lesson_with_same_course = SerializerMethodField()

    def get_count_lesson_with_same_course(self, lesson):
        return Lesson.objects.filter(course_lesson=lesson.course_lesson).count()

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'preview', 'description', 'link', 'course_lesson', 'count_lesson_with_same_course')
