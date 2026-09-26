from django.contrib import admin
from .models import (
    Subject, GradeOption, Interest, Hobby, School, Career,
    Course, Roadmap, RoadmapStep, Student, Assessment,
    AssessmentGrade, Recommendation
)

class RoadmapStepInline(admin.TabularInline):
    model = RoadmapStep
    extra = 1

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'average_salary')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('relevant_subjects', 'relevant_interests', 'relevant_hobbies')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'school', 'duration_years')
    list_filter = ('school',)
    search_fields = ('title', 'school__name')
    filter_horizontal = ('related_careers',)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'career')
    inlines = [RoadmapStepInline]

admin.site.register(Subject)
admin.site.register(GradeOption)
admin.site.register(Interest)
admin.site.register(Hobby)
admin.site.register(Student)
admin.site.register(Assessment)
admin.site.register(Recommendation)