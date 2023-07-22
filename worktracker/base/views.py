from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import theTask
from django.contrib.auth.views import LoginView
from base.models import Assessment
import pdftables_api
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
import os
from datetime import datetime, timedelta
# Create your views here.



class TaskLi(LoginRequiredMixin, ListView):
    context_object_name = 'tsk'
    template_name = 'base/listoftasks.html'
    
    def get_queryset(self):
        orderpriority = {'High Priority': 1,
                          'Medium Priority': 2,'Low Priority': 3}
        return sorted(theTask.objects.filter(user=self.request.user), key=lambda p_order: orderpriority[p_order.taskpriority])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prioritychoices'] = dict(theTask.priority)
        return context


def home(request):
    cxt = {}
    return render(request, 'base/home.html', cxt)


from .models import theTask

def dashboard(request):
    accomplished_count = theTask.objects.filter(
        user=request.user, accomplished=True).count()
    unaccomplished_count = theTask.objects.filter(
        user=request.user, accomplished=False).count()
    tsk = TaskLi.get_queryset(TaskLi(request=request))

    context = {
        'tsk': tsk,
        'accomplished_count': accomplished_count,
        'unaccomplished_count': unaccomplished_count,
    
    }

    return render(request, 'base/dashboard.html', context)

class TaskDe(DetailView):
    model = theTask
    template_name = 'base/thetaskinfo.html'


class TaskAdd(CreateView):
    model = theTask
    fields = ['title', 'desc', 'accomplished', 'taskpriority']
    template_name = 'base/theForm.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskEdit(UpdateView):
    model = theTask
    fields = ['title', 'desc', 'accomplished', 'taskpriority']
    success_url = reverse_lazy('dashboard')
    template_name = 'base/theForm.html'


class TaskDelete(DeleteView):
    model = theTask
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')
    template_name = 'base/deletethis.html'


class LoginVi(LoginView):
    template_name = 'base/theLogin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def pdf_csv():

    if os.path.exists('output.csv'):
        os.remove('output.csv')

    c = pdftables_api.Client('fd12p22l1tli')
    c.csv('Year 3 CS Assessment Map (1).pdf', 'output.csv')

    df = pd.read_csv('output.csv')

    for i, row in df.iterrows():
        a = Assessment()
        a.module = row['Module']
        a.title = row['Contribution % Title']
        a.type = row['Type']
        a.hand_out_date = row['Hand Out Date\n(week commencing)']
        a.hand_in_date = row['Hand In Date (week\ncommencing)']
        
        a.save()

@login_required
def assessment(request):
    pdf_csv()
    assessments = Assessment.objects.all()

    for assessment in assessments:
        none = 'nan'
        clean = assessment.hand_in_date.rsplit('and', 1)[-1].strip()
        if assessment.hand_in_date != none:
            hand_in_date = datetime.strptime(clean, "%d %B %Y").date()
            highercontribution = timedelta(weeks=2)
            lowercontribution = timedelta(weeks=1)
            highercontributiondeadline = hand_in_date - highercontribution
            lowercontributiondeadline = hand_in_date - lowercontribution
            if assessment.contribution and int(assessment.contribution) > 50:
                assessment.suggesteddeadline = highercontributiondeadline
            else:
                assessment.suggesteddeadline = lowercontributiondeadline
            assessment.save()

    context = {'assessments': assessments}
    return render(request, 'base/assessment.html', context)

class Register(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    template_name = 'base/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)


def show_assessments(request):
    assessments = Assessment.objects.all()
    return render(request, 'base/assessment.html', {'assessments': assessments})

