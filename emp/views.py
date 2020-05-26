from django.shortcuts import render,redirect

# Create your views here.
from . import models
from login.models import User

def crt(request):
    '''
    增操作
    '''
    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        nation = request.POST['nation']
        birthday = request.POST['birthday']
        politics = request.POST['politics']
        education = request.POST['education']
        marriage = request.POST['marriage']
        hometown = request.POST['hometown']
        id_card = request.POST['id_card']
        phone = request.POST['phone']
        place = request.POST['place']
        home_card = request.POST['home_card']
        '''
        工作信息
        '''

        num = request.POST['num']
        in_time = request.POST['in_time']
        pos = request.POST['pos']
        duty = request.POST['duty']
        pre_num = request.POST['pre_num']
        status = request.POST['status']
        dep_id = request.POST['dep_id']

        models.staff.objects.create(
            name=name,
            sex = sex,
            nation = nation,
            birthday = birthday,
            politics = politics,
            education = education,
            marriage = marriage,
            hometown = hometown,
            id_card = id_card,
            phone = phone,
            place = place,
            home_card = home_card,
            num = num,
            in_time = in_time,
            pos = pos,
            duty = duty,
            pre_num = pre_num,
            status = status,
            dep_id = dep_id,
            account_id = request.session['user_id']
        )
        '''
        增加成功后显示表
        '''
        info = models.staff.objects.filter(name = name)
        return render(request, 'show.html', {'info': info})
    return render(request, 'crt.html')



def update(request):
    if request.method == 'POST':
        del_id = request.session['id']
        op = models.staff.objects.filter(sid=del_id)
        for i in range(len(op)):
            op[i].name = request.POST['name']
            op[i].sex = request.POST['sex']
            op[i].nation = request.POST['nation']
            op[i].birthday = request.POST['birthday']
            op[i].politics = request.POST['politics']
            op[i].education = request.POST['education']
            op[i].marriage = request.POST['marriage']
            op[i].hometown = request.POST['hometown']
            op[i].id_card = request.POST['id_card']
            op[i].phone = request.POST['phone']
            op[i].place = request.POST['place']
            op[i].home_card = request.POST['home_card']
            '''
            工作信息
            '''

            op[i].num = request.POST['num']
            op[i].in_time = request.POST['in_time']
            op[i].pos = request.POST['pos']
            op[i].duty = request.POST['duty']
            op[i].pre_num = request.POST['pre_num']
            op[i].status = request.POST['status']
            op[i].save()
        '''
        修改成功后显示表
        '''
        print(models.staff.objects.values('name').filter(sid=del_id))
        info = models.staff.objects.filter(sid = del_id)

        return render(request, 'show.html', {'info': info})
    return render(request, 'update.html')

def show(request):
    '''
    查操作
    '''
    username = request.session['user_name']
    userid = request.session['user_id']
    person = User.objects.filter(name=username).first()
    info = models.staff.objects.filter(account__name=username)
    request.session['id'] = models.staff.objects.values("sid").get(account__id=userid)['sid']
    return render(request, 'show.html', {'info': info})