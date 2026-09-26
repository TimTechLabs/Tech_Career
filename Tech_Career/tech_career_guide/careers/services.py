from .models import Career, Course, Recommendation

def calculate_career_recommendations(assessment):
    """
    Calculates dynamic match percentage scores for careers based on:
    - Subject grades
    - Field interests
    - Personal hobbies
    """
    careers = Career.objects.all()
    student_interests = list(assessment.interests.all())
    student_hobbies = list(assessment.hobbies.all())
    student_grades = assessment.grades.all()

    recommendations = []

    for career in careers:
        score = 0.0
        max_score = 0.0
        reasons = []

        # 1. Evaluate Interests (40% Weight)
        career_interests = career.relevant_interests.all()
        for interest in career_interests:
            max_score += 40
            if interest in student_interests:
                score += 40
                reasons.append(f"Strong interest in {interest.name}")

        # 2. Evaluate Hobbies (30% Weight)
        career_hobbies = career.relevant_hobbies.all()
        for hobby in career_hobbies:
            max_score += 30
            if hobby in student_hobbies:
                score += 30
                reasons.append(f"Matching hobby/style: {hobby.name}")

        # 3. Evaluate Core Subject Performance (30% Weight)
        career_subjects = career.relevant_subjects.all()
        for sub in career_subjects:
            max_score += 30
            matching_grade = student_grades.filter(subject=sub).first()
            if matching_grade:
                # Weight score based on GradeOption weight
                earned = 30 * matching_grade.grade.weight
                score += earned
                reasons.append(f"Good performance in {sub.name} ({matching_grade.grade.label})")

        # Fallback calculation if no specific prerequisites defined
        if max_score == 0:
            match_percentage = 50.0
        else:
            match_percentage = round((score / max_score) * 100, 1)

        # Cap between 45% and 98%
        match_percentage = min(98.0, max(45.0, match_percentage))

        # Save or update recommendation model
        rec, _ = Recommendation.objects.update_or_create(
            assessment=assessment,
            career=career,
            defaults={
                'match_percentage': match_percentage,
                'reasons': "\n".join(reasons) if reasons else "General baseline tech compatibility."
            }
        )
        recommendations.append(rec)

    recommendations.sort(key=lambda x: x.match_percentage, reverse=True)
    return recommendations