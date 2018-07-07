from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.http import JsonResponse
import time

from .models import Schedule
from .forms import CustomerForm


class IndexView(View):
    def get(self, request):
        return render(request, 'teacher/index.html')


class ClassActive(LoginRequiredMixin, View):
    # login_url = '/login/'
    def get(self, request):
        return render(request, 'teacher/classactive.html')


class CourseTableView(LoginRequiredMixin, View):
    # login_url = '/login/'
    def get(self, request):
        courses = Schedule.objects.all()
        ones = courses.filter(order='一')
        twos = courses.filter(order='二')
        threes = courses.filter(order='三')
        fours = courses.filter(order='四')
        fives = courses.filter(order='五')
        sixes = courses.filter(order='六')

        weekday = time.strftime("%w")
        weekdict = {'0': '星期日',
                    '1': '星期一',
                    '2': '星期二',
                    '3': '星期三',
                    '4': '星期四',
                    '5': '星期五',
                    '6': '星期六'
                    }
        today = weekdict[weekday]
        today_courses = courses.filter(week=today)
        today_courses = self.modify_day_courses(today_courses)

        ones = self.modify_courses(ones)
        twos = self.modify_courses(twos)
        threes = self.modify_courses(threes)
        fours = self.modify_courses(fours)
        fives = self.modify_courses(fives)
        sixes = self.modify_courses(sixes)
        return render(request, 'teacher/coursetable.html', {'ones': ones,
                                                            'twos': twos,
                                                            'threes': threes,
                                                            'fours': fours,
                                                            'fives': fives,
                                                            'sixes': sixes,
                                                            'today_courses': today_courses,
                                                            })

    def modify_courses(self, ones):
        all_ones = [None, None, None, None, None, None, None]
        for c in ones:
            if c.week == '星期一':
                all_ones[0] = c
            elif c.week == '星期二':
                all_ones[1] = c
            elif c.week == '星期三':
                all_ones[2] = c
            elif c.week == '星期四':
                all_ones[3] = c
            elif c.week == '星期五':
                all_ones[4] = c
            elif c.week == '星期六':
                all_ones[5] = c
            else:
                all_ones[6] = c
        return all_ones

    def modify_day_courses(self, ones):
        all_day = [None, None, None, None, None, None]
        for c in ones:
            if c.order == '一':
                all_day[0] = c
            elif c.order == '二':
                all_day[1] = c
            elif c.order == '三':
                all_day[2] = c
            elif c.order == '四':
                all_day[3] = c
            elif c.order == '五':
                all_day[4] = c
            else:
                all_day[5] = c

        return all_day


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('teacher:index')


class CustomerAskView(View):
    def post(self, request):
        customerask_form = CustomerForm(request.POST)
        if customerask_form.is_valid():
            customerask_form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '提交出错了'})