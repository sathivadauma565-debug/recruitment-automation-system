from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application

# 🔥 Skills list (customize cheyochu)
SKILLS = ['python', 'django', 'rest api', 'html', 'css', 'javascript', 'react', 'sql']

# 📄 PDF nundi text extract function
def extract_text_from_pdf(file):
    text = ""
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        return ""
    return text


# 🏠 Dashboard (Job List)
def dashboard(request):
    jobs = Job.objects.all()

    total = Application.objects.count()
    selected = Application.objects.filter(status="Selected").count()
    rejected = Application.objects.filter(status="Rejected").count()

    return render(request, 'dashboard.html', {
        'jobs': jobs,
        'total': total,
        'selected': selected,
        'rejected': rejected
    })
# 📝 Apply Job
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        if application.objects.filter(email=email, job=job).exists():
            return HttpResponse("You have already applied for this job.")

        resume_text = extract_text_from_pdf(resume)

        # ✅ skills check
        if resume_text:
            skills_found = [skill for skill in SKILLS if skill in resume_text.lower()]
        else:
            skills_found = []

        print("Skills Found:", skills_found)

        # ✅ score calculate
        score = len(skills_found) * 10
        print("Score:", score)

        # ✅ status decide
        if score >= 50:
            status = "Selected"
        else:
            status = "Rejected"

        print("Status:", status)
        

        # ✅ save
        Application.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume,
            score=score,
            status=status
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'job': job})
def selected_candidates(request):
    selected = Application.objects.filter(status="Selected").order_by('-score')
    return render(request, 'selected.html', {'applications': selected})
def rejected_candidates(request):
    rejected_apps = Application.objects.filter(status="Rejected")
    return render(request, 'rejected.html', {'apps': rejected_apps})