from django import forms
from .models import Subject, GradeOption, Interest, Hobby


class StudentStep1Form(forms.Form):
    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg-custom',
            'placeholder': 'e.g. Jane Doe',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg-custom',
            'placeholder': 'e.g. jane@example.com',
            'required': 'required'
        })
    )
    education_level = forms.CharField(
        label="Education Level",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg-custom',
            'placeholder': 'e.g. High School, Undergraduate'
        })
    )


class Step2GradesForm(forms.Form):
    """Dynamically creates a select field for every Subject created in Admin."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Build choices tuple list: [('', '-- Select Grade --'), ('1', 'A'), ...]
        grade_choices = [('', '-- Select Grade --')] + [
            (str(g.id), g.label) for g in GradeOption.objects.all()
        ]
        
        # Fetch all subjects dynamically from database
        subjects = Subject.objects.all()
        for subject in subjects:
            # Prefixed with sub_ to align directly with views.py parsing logic
            field_name = f"sub_{subject.id}"
            self.fields[field_name] = forms.ChoiceField(
                choices=grade_choices,
                label=subject.name,
                required=False,
                widget=forms.Select(attrs={
                    'class': 'form-select form-control'
                })
            )


class Step3InterestsForm(forms.Form):
    """Displays dynamically queried interests from admin as multiple checkboxes."""
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False,
        label="Select Fields of Interest"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure latest database records from admin are refreshed on every form render
        self.fields['interests'].queryset = Interest.objects.all()


class Step4HobbiesForm(forms.Form):
    """Displays dynamically queried hobbies from admin as multiple checkboxes."""
    hobbies = forms.ModelMultipleChoiceField(
        queryset=Hobby.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False,
        label="Select Your Hobbies & Activities"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure latest database records from admin are refreshed on every form render
        self.fields['hobbies'].queryset = Hobby.objects.all()