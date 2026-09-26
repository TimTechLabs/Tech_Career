from django.core.management.base import BaseCommand
from careers.models import (
    Subject, GradeOption, Interest, Hobby, School,
    Career, Course, Roadmap, RoadmapStep
)

class Command(BaseCommand):
    help = 'Seeds database with 5 core careers, courses, schools, and roadmaps'

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # 1. Core Subjects
        math, _ = Subject.objects.get_or_create(name="Mathematics")
        cs, _ = Subject.objects.get_or_create(name="Computer Studies / ICT")
        eng, _ = Subject.objects.get_or_create(name="English Language")
        phy, _ = Subject.objects.get_or_create(name="Physics")

        # 2. Grade Options
        GradeOption.objects.get_or_create(label="A (Excellent)", weight=1.0)
        GradeOption.objects.get_or_create(label="B (Very Good)", weight=0.85)
        GradeOption.objects.get_or_create(label="C (Good)", weight=0.70)
        GradeOption.objects.get_or_create(label="D (Pass)", weight=0.50)

        # 3. Interests
        i_prog, _ = Interest.objects.get_or_create(name="Software & Programming")
        i_data, _ = Interest.objects.get_or_create(name="Data & Analytics")
        i_sec, _ = Interest.objects.get_or_create(name="Cybersecurity & Networks")
        i_sys, _ = Interest.objects.get_or_create(name="IT Infrastructure & Support")

        # 4. Hobbies
        h_code, _ = Hobby.objects.get_or_create(name="Coding / Building Apps")
        h_puzzle, _ = Hobby.objects.get_or_create(name="Solving Logic Puzzles / Math")
        h_hardware, _ = Hobby.objects.get_or_create(name="PC Building & Hardware")
        h_security, _ = Hobby.objects.get_or_create(name="Ethical Hacking / CTFs")

        # 5. Schools
        s1, _ = School.objects.get_or_create(name="Tech University", location="Main Campus")
        s2, _ = School.objects.get_or_create(name="National Institute of Technology", location="City Campus")

        # 6. Careers Data Definition
        careers_data = [
            {
                'title': 'Computer Science',
                'category': 'Core Computing',
                'description': 'Study computation, algorithms, data structures, and computer theory.',
                'overview': 'Deep dive into computational systems and algorithms.',
                'what_students_study': 'Algorithms, Data Structures, Operating Systems, AI, Discrete Math.',
                'who_suits_course': 'Logically driven students who love problem-solving and mathematical abstraction.',
                'practical_projects': 'Building compilers, graph traversal engines, AI classifiers.',
                'career_opportunities': 'Algorithm Engineer, AI Research, Software Architect.',
                'job_roles': 'CS Engineer, Research Scientist, System Engineer.',
                'tools_technologies': 'C++, Python, Java, Linux, Git.',
                'real_world_apps': 'Search engines, autonomous navigation, machine learning systems.',
                'average_salary': '$95,000 / year',
                'required_skills': 'Algorithms, Problem Solving, Mathematics, C++, Python',
                'subjects': [math, cs],
                'interests': [i_prog, i_data],
                'hobbies': [h_code, h_puzzle]
            },
            {
                'title': 'Software Engineering',
                'category': 'Software Development',
                'description': 'Design, build, scale, and maintain production-grade software applications.',
                'overview': 'Focus on practical software architecture, lifecycle, and engineering principles.',
                'what_students_study': 'Full Stack Web Dev, Mobile Apps, System Design, Testing, Agile.',
                'who_suits_course': 'Builders who want to turn ideas into scalable digital products.',
                'practical_projects': 'Building SaaS platforms, mobile apps, RESTful microservices.',
                'career_opportunities': 'Full Stack Developer, Backend Engineer, Mobile Developer.',
                'job_roles': 'Software Engineer, DevOps Specialist, Tech Lead.',
                'tools_technologies': 'Django, React, PostgreSQL, Docker, Git.',
                'real_world_apps': 'E-commerce platforms, social media networks, mobile banking apps.',
                'average_salary': '$105,000 / year',
                'required_skills': 'Python, Web Frameworks, SQL, Git, API Design',
                'subjects': [math, cs, eng],
                'interests': [i_prog],
                'hobbies': [h_code]
            },
            {
                'title': 'Information Technology',
                'category': 'IT & Operations',
                'description': 'Manage, deploy, and maintain corporate IT systems, cloud systems, and networks.',
                'overview': 'Focus on technology administration, network operations, and enterprise infrastructure.',
                'what_students_study': 'Networking, Systems Admin, Cloud Computing, Database Admin, Security.',
                'who_suits_course': 'Hands-on problem solvers who enjoy systems, networks, and technical support.',
                'practical_projects': 'Configuring enterprise Active Directory, Cloud deployments, VLAN setup.',
                'career_opportunities': 'IT Administrator, Systems Analyst, Cloud Support Engineer.',
                'job_roles': 'Network Admin, Systems Admin, IT Support Manager.',
                'tools_technologies': 'AWS, Linux, Windows Server, Cisco IOS, PowerShell.',
                'real_world_apps': 'Corporate infrastructure management, cloud migration, network security.',
                'average_salary': '$78,000 / year',
                'required_skills': 'Networking, Linux Systems, AWS Cloud, Hardware, Troubleshooting',
                'subjects': [cs, phy],
                'interests': [i_sys],
                'hobbies': [h_hardware]
            },
            {
                'title': 'Data Science',
                'category': 'Analytics & AI',
                'description': 'Extract actionable business insights from large datasets using statistical modeling and AI.',
                'overview': 'Combine statistics, machine learning, and domain knowledge to decode complex data.',
                'what_students_study': 'Statistics, Machine Learning, Data Visualization, SQL, Python.',
                'who_suits_course': 'Analytical minds who like finding hidden trends in data.',
                'practical_projects': 'Predictive customer analytics models, recommendation systems.',
                'career_opportunities': 'Data Scientist, ML Engineer, Business Intelligence Analyst.',
                'job_roles': 'Data Analyst, Machine Learning Specialist, Analytics Lead.',
                'tools_technologies': 'Python, Pandas, NumPy, Scikit-Learn, Tableau, SQL.',
                'real_world_apps': 'Fraud detection systems, recommendation engines, market analysis.',
                'average_salary': '$100,000 / year',
                'required_skills': 'Python, Statistics, Machine Learning, SQL, Data Viz',
                'subjects': [math, cs],
                'interests': [i_data],
                'hobbies': [h_puzzle]
            },
            {
                'title': 'Cybersecurity',
                'category': 'Security & Defense',
                'description': 'Protect digital networks, cloud infrastructure, and databases from cyber threats.',
                'overview': 'Master offensive defense, vulnerability assessments, and security compliance.',
                'what_students_study': 'Network Defense, Ethical Hacking, Cryptography, Digital Forensics.',
                'who_suits_course': 'Curious, detail-oriented individuals who enjoy security challenges.',
                'practical_projects': 'Penetration testing labs, malware analysis, SOC monitoring setup.',
                'career_opportunities': 'Security Analyst, Ethical Hacker, Security Consultant.',
                'job_roles': 'SOC Analyst, Penetration Tester, Cybersecurity Specialist.',
                'tools_technologies': 'Wireshark, Metasploit, Nmap, Linux, Burp Suite.',
                'real_world_apps': 'Securing financial transactions, threat hunting, infrastructure defense.',
                'average_salary': '$102,000 / year',
                'required_skills': 'Ethical Hacking, Wireshark, Linux, Networking, Security Protocols',
                'subjects': [math, cs, phy],
                'interests': [i_sec],
                'hobbies': [h_security]
            }
        ]

        for data in careers_data:
            subjects_list = data.pop('subjects')
            interests_list = data.pop('interests')
            hobbies_list = data.pop('hobbies')

            career, _ = Career.objects.update_or_create(
                title=data['title'],
                defaults=data
            )
            career.relevant_subjects.set(subjects_list)
            career.relevant_interests.set(interests_list)
            career.relevant_hobbies.set(hobbies_list)

            # Map Courses
            Course.objects.get_or_create(
                title=f"BSc {career.title}",
                school=s1,
                defaults={'duration_years': 4}
            )[0].related_careers.add(career)

            Course.objects.get_or_create(
                title=f"Bachelor of {career.title} (Hons)",
                school=s2,
                defaults={'duration_years': 4}
            )[0].related_careers.add(career)

            # Map Visual Roadmap Steps
            rm, _ = Roadmap.objects.get_or_create(career=career, defaults={'title': f'{career.title} Roadmap'})
            
            steps = [
                ('beginner', 1, 'Programming Fundamentals', 'Learn core syntax, variables, conditionals, loops.'),
                ('intermediate', 2, 'Data Structures & Tools', 'Master Git, SQL, arrays, hash maps, and object-oriented programming.'),
                ('advanced', 3, 'Specialized Frameworks & Systems', 'Build full-scale applications using modern frameworks and databases.'),
                ('project', 4, 'Projects & Portfolio', 'Build 2-3 real-world projects and publish code to GitHub.'),
                ('progression', 5, 'Internship & Career Entry', 'Prepare technical resume, master interview algorithms, land entry role.')
            ]
            for lvl, ord_num, st_title, desc in steps:
                RoadmapStep.objects.update_or_create(
                    roadmap=rm, order=ord_num,
                    defaults={'level': lvl, 'title': st_title, 'description': desc}
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))