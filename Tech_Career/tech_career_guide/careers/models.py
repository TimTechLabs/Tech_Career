

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GradeOption(models.Model):
    name = models.CharField(max_length=10)  # e.g., A, B, C, D, E

    def __str__(self):
        return self.name


class Interest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Hobby(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
class Career(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    average_salary = models.CharField(max_length=100, blank=True, null=True)

    relevant_subjects = models.ManyToManyField(Subject, blank=True, related_name='careers')
    relevant_interests = models.ManyToManyField(Interest, blank=True, related_name='careers')
    relevant_hobbies = models.ManyToManyField(Hobby, blank=True, related_name='careers')

    def __str__(self):
        return self.title


class School(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    description = models.TextField()
    duration_years = models.IntegerField(default=4)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')
    related_careers = models.ManyToManyField(Career, related_name='courses')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Roadmap(models.Model):
    title = models.CharField(max_length=255)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='roadmaps')

    def __str__(self):
        return f"{self.title} ({self.career.title})"


class RoadmapStep(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='steps')
    step_title = models.CharField(max_length=255)
    step_description = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order}: {self.step_title}"


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    education_level = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Assessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assessments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment {self.id} ({self.created_at.strftime('%Y-%m-%d')})"


class AssessmentGrade(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeOption, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name}: {self.grade.grade}"


class Recommendation(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='recommendations')
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = ('assessment', 'career')

    def __str__(self):
        return f"{self.career.title} ({self.score}%) for Assessment {self.assessment.id}"