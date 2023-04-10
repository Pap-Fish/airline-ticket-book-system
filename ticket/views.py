# coding=utf-8

from django.shortcuts import render, redirect
from service import userService, flightService, passengerService


# Create your views here.


# 元组转字典
def tuple_to_dict(t):
    res = []
    for data in t:
        res.append({index: key for index, key in enumerate(data)})
    return res


# 渲染登录页面
def default_view(request):
    return render(request, 'login.html', {'msg': ''})


def index_view(request):
    if request.method == 'GET':
        f_service = flightService.flService()
        rec = f_service.find_flight()['object']
        flights = tuple_to_dict(rec)
        f_service.curClose()
        for fl in flights:
            fl[3] = fl[3].strftime('%Y-%m-%d %H:%M:%S')
            fl[4] = fl[4].strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'index.html', {'u_name': request.session['u_name'], 'flights': flights})
    else:
        f_service = flightService.flService()
        f_id = request.POST['f_id'] if request.POST['f_id'] != '' else None
        if f_id:
            rec = f_service.find_flight(f_id)['object']
        else:
            dep_station = request.POST['dep_station'] if request.POST['dep_station'] != '' else None
            dest_station = request.POST['dest_station'] if request.POST['dest_station'] != '' else None
            dep_time = request.POST['dep_time'] if request.POST['dep_time'] != '' else None
            a_name = request.POST['a_name'] if request.POST['a_name'] != '' else None
            rec = f_service.find_flight(dep_station=dep_station, dest_station=dest_station,
                                        dep_time=dep_time, airline=a_name)['object']
        f_service.curClose()
        flights = tuple_to_dict(rec)
        for fl in flights:
            fl[3] = fl[3].strftime('%Y-%m-%d %H:%M:%S')
            fl[4] = fl[4].strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'index.html', {'u_name': request.session['u_name'], 'flights': flights})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'msg': ''})
    else:
        u_service = userService.userService()
        # 接收请求参数
        u_name = request.POST['uname']
        pwd = request.POST['pwd']
        result = u_service.login(u_name, pwd)
        if result['msg'] is 'success':
            request.session['u_name'] = u_name

            res = u_service.find_passenger(u_id=u_name)['object']
            p_id = res[0][1] if res else 'None'
            # 设置默认绑定的身份
            request.session['p_id'] = p_id
            # 设置默认修改信息时选用的身份
            request.session['up_pid'] = p_id
            f_service = flightService.flService()
            rec = f_service.find_flight()['object']
            f_service.curClose()
            u_service.curClose()
            flights = tuple_to_dict(rec)
            for fl in flights:
                fl[3] = fl[3].strftime('%Y-%m-%d %H:%M:%S')
                fl[4] = fl[4].strftime('%Y-%m-%d %H:%M:%S')
            return render(request, 'index.html', {'u_name': u_name, 'flights': flights, 'msg': '登陆成功'})
        else:
            u_service.curClose()
            return render(request, 'login.html', {'msg': result['msg']})


def logout_view(request):
    # 1. 将session中的用户名、昵称删除
    request.session.flush()
    # 2. 重定向到 登录界面
    return redirect('/airticket/')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u_service = userService.userService()
        u_name = request.POST['uname']
        pwd = request.POST['pwd']

        # 非空判断
        if u_name and pwd:
            result = u_service.register(u_name, pwd)
            msg = result['msg']
            u_service.curClose()
            if msg is 'success':
                return render(request, 'login.html', {'msg': '注册成功'})
        else:
            msg = '用户名为空'
        return render(request, 'login.html', {'msg': msg})


def buy_view(request):
    f_service = flightService.flService()
    if request.method == "GET":
        f_id = request.GET['f_id']
        request.session['f_id'] = f_id
        # 返回舱位信息
        res = f_service.find_fligt_seat(f_id)['object']
        seats = tuple_to_dict(res)
        f_service.curClose()
        return render(request, 'buy.html', {'f_id': f_id, 'seats': seats,
                                            'u_name': request.session['u_name'], 'msg': ''})
    else:
        p_service = passengerService.pasService()
        f_id = request.session['f_id']
        s_level = request.POST.get('s_level', '')
        p_id = request.session['p_id']
        msg = p_service.buy_ticket(p_id=p_id, f_id=f_id, s_level=s_level)['msg']
        # 返回舱位信息
        res = f_service.find_fligt_seat(f_id)['object']
        seats = tuple_to_dict(res)
        f_service.curClose()
        return render(request, 'buy.html', {'f_id': f_id, 'u_name': request.session['u_name'],
                                            'msg': msg, 'seats': seats})


def user_view(request):
    u_service = userService.userService()
    p_service = passengerService.pasService()
    u_name = request.session['u_name']
    p_id = request.session['p_id']
    res = p_service.find_passenger(p_id)['object']
    p_name = res[0][1] if res else '暂无旅客身份'
    # 刷新信息
    res = u_service.find_passenger(u_id=u_name)['object']
    passengers = tuple_to_dict(res)
    u_service.curClose()
    p_service.curClose()
    return render(request, 'user.html', {'u_name': u_name, 'passengers': passengers, 'p_name': p_name})


def journey_view(request):
    p_service = passengerService.pasService()
    u_service = userService.userService()
    msg = ''
    if request.POST.get("t_id", ""):
        t_id = request.POST.get("t_id", "")
        msg = p_service.refund_ticket(t_id)['msg']
    u_name = request.session['u_name']
    p_id = request.session['p_id']
    res = p_service.find_passenger(p_id)['object']
    p_name = res[0][1] if res else ''

    rec = p_service.find_passenger_ticket(p_id=p_id)['object']
    journey = tuple_to_dict(rec)
    u_service.curClose()
    p_service.curClose()
    return render(request, 'journey.html', {'u_name': u_name, 'journey': journey, 'p_name': p_name, 'msg': msg})


def update_view(request):
    u_name = request.session['u_name']
    if request.method == 'GET':
        return render(request, 'update.html', {'u_name': u_name})
    else:
        p_service = passengerService.pasService()
        u_service = userService.userService()
        if request.POST.get("update", ""):
            p_id = request.POST.get("update", "")
            request.session['up_pid'] = p_id
            return render(request, 'update.html', {'u_name': u_name})
        elif request.POST.get("select", ""):
            p_id = request.POST.get("select", "")
            # 转换旅客身份
            request.session['p_id'] = p_id
            request.session['up_pid'] = p_id
            msg = ''
        elif request.POST.get("delete", ""):
            p_id = request.POST.get("delete", "")
            msg = u_service.delete_passenger(u_id=u_name, p_id=p_id)['msg']
        else:
            p_name = request.POST['p_name']
            p_sex = request.POST['p_sex']
            p_nation = request.POST['p_nation']
            p_idnumber = request.POST['p_idnumber']
            workplace = request.POST['workplace']
            telephone = request.POST['telephone']
            order = request.POST['sub']
            if order == 'update':
                p_id = request.session['up_pid']
                msg = p_service.update_passenger(p_id=p_id, p_name=p_name, p_sex=p_sex, p_nation=p_nation,
                                                 p_idnumber=p_idnumber, workplace=workplace, telephone=telephone)['msg']
            else:
                p_id = request.session['p_id']
                if p_name and p_sex and p_nation and p_idnumber and workplace and telephone:
                    msg = p_service.add_passenger(u_id=u_name, p_name=p_name, p_sex=p_sex, p_nation=p_nation,
                                                  p_idnumber=p_idnumber, workplace=workplace, telephone=telephone)[
                        'msg']
                else:
                    msg = '字段必须全部填写！'
                    return render(request, 'update.html', {'u_name': u_name, 'msg': msg})
        # 刷新信息
        res = u_service.find_passenger(u_id=u_name)['object']
        passengers = tuple_to_dict(res)
        p_name = p_service.find_passenger(p_id)['object'][0][1]
        u_service.curClose()
        p_service.curClose()
        return render(request, 'user.html', {'u_name': u_name, 'passengers': passengers,
                                             'msg': msg, 'p_name': p_name})


def change_pwd_view(request):
    u_name = request.session['u_name']
    if request.method == "GET":
        return render(request, 'cpwd.html', {'u_name': u_name})
    else:
        pwd = request.POST['password']
        old_pwd = request.POST['oldPassword']
        u_service = userService.userService()
        exist_pwd = u_service.find_user(u_name)['object'][0][2]
        if exist_pwd != old_pwd:
            msg = '当前密码错误！'
        else:
            msg = u_service.update_pwd(u_name, pwd)['msg']
        return render(request, 'cpwd.html', {'msg': msg})


def airline_view(request):
    u_name = request.session['u_name']
    f_service = flightService.flService()
    rec = f_service.find_airline()['object']
    airlines = tuple_to_dict(rec)
    return render(request, 'airline.html', {'u_name': u_name, 'airlines': airlines})
