from django.shortcuts import render, redirect, get_object_or_404
from .models import Interest, Hobby, GradeOption, Subject, Career, Course, School 

def home(request):
    """Renders the landing page."""
    return render(request, 'home.html')

def admin_dashboard(request):
    """Renders the custom admin dashboard page."""
    return render(request, 'admin/dashboard.html')

# --- Career & Course Views ---

def career_list(request):
    """Displays all available careers."""
    careers = Career.objects.all()
    return render(request, 'careers/career_list.html', {'careers': careers})

from django.shortcuts import render, get_object_or_404
from .models import Career

def career_detail(request, slug=None, pk=None):
    # Lookup by pk or slug depending on what was passed
    if pk:
        career = get_object_or_404(Career, pk=pk)
    else:
        career = get_object_or_404(Career, pk=slug) # or Career.objects.get(slug=slug)
        
    return render(request, 'careers/career_detail.html', {'career': career})

def course_list(request):
    """Displays available courses."""
    courses = Course.objects.all()
    return render(request, 'careers/course_list.html', {'courses': courses})

def course_detail(request, pk):
    """Displays details for a specific course."""
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'careers/course_detail.html', {'course': course})

# --- School Views ---

def school_list(request):
    """Displays available schools."""
    schools = School.objects.all()
    return render(request, 'careers/school_list.html', {'schools': schools})

def school_detail(request, pk):
    """Displays details for a specific school."""
    school = get_object_or_404(School, pk=pk)
    return render(request, 'careers/school_detail.html', {'school': school})

# --- Assessment Views ---

def assessment_step1(request):
    """Step 1: Personal Info."""
    if request.method == 'POST':
        return redirect('careers:assessment_step2')
    return render(request, 'assessment/step1_personal.html')

from django.shortcuts import render, redirect
from .models import Subject, GradeOption, Interest, Hobby
from django.shortcuts import render, redirect
from .models import Subject, GradeOption

def assessment_step2(request):
    subjects = Subject.objects.all()
    grades = GradeOption.objects.all()

    if request.method == 'POST':
        selected_grades = {}
        for subject in subjects:
            # Capture selected grade for each subject
            grade_id = request.POST.get(f'subject_{subject.id}')
            if grade_id:
                selected_grades[str(subject.id)] = grade_id

        # Store in session
        request.session['selected_grades'] = selected_grades
        
        # Make sure the redirect URL name matches your urls.py exactly
        return redirect('careers:assessment_step3')

    context = {
        'subjects': subjects,
        'grades': grades,
    }
    return render(request, 'assessment/step2_grades.html', context)
from django.shortcuts import render, redirect
from .models import Subject, GradeOption, Interest, Hobby, Career

# --- STEP 3: INTERESTS ---
def assessment_step3(request):
    interests = Interest.objects.all()

    if request.method == 'POST':
        # Collect selected interest IDs
        selected_interest_ids = request.POST.getlist('interests')
        request.session['selected_interests'] = selected_interest_ids
        return redirect('careers:assessment_step4')

    context = {'interests': interests}
    return render(request, 'assessment/step3_interests.html', context)


# --- STEP 4: HOBBIES ---
def assessment_step4(request):
    hobbies = Hobby.objects.all()

    if request.method == 'POST':
        # Collect selected hobby IDs
        selected_hobby_ids = request.POST.getlist('hobbies')
        request.session['selected_hobbies'] = selected_hobby_ids
        return redirect('careers:assessment_step5')

    context = {'hobbies': hobbies}
    return render(request, 'assessment/step4_hobbies.html', context)


# --- STEP 5: REVIEW & RESULTS ---
def assessment_step5(request):
    # Retrieve saved choices from session
    selected_grades_dict = request.session.get('selected_grades', {})
    selected_interest_ids = request.session.get('selected_interests', [])
    selected_hobby_ids = request.session.get('selected_hobbies', [])

    # Fetch corresponding objects from database
    selected_interests = Interest.objects.filter(id__in=selected_interest_ids)
    selected_hobbies = Hobby.objects.filter(id__in=selected_hobby_ids)

    # Format selected subject grades
    user_grades = []
    for subject_id, grade_id in selected_grades_dict.items():
        try:
            subj = Subject.objects.get(id=subject_id)
            grd = GradeOption.objects.get(id=grade_id)
            user_grades.append({'subject': subj.name, 'grade': grd.name})
        except (Subject.DoesNotExist, GradeOption.DoesNotExist):
            continue

    # Fetch recommended careers (or display top careers)
    recommended_careers = Career.objects.all()[:3]

    context = {
        'user_grades': user_grades,
        'selected_interests': selected_interests,
        'selected_hobbies': selected_hobbies,
        'recommended_careers': recommended_careers,
    }
    return render(request, 'assessment/step5_review.html', context)
def assessment_result(request, assessment_id):
    # Fetch the assessment results if saved in database
    return render(request, 'assessment/step5_review.html')
