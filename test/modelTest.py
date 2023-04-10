import os
import django

from service.flightService import flService
from service.userService import userService
from service.passengerService import pasService
from django.conf import settings


def addPas_test():
    p_service = pasService()
    u_id = 'super'
    p_name = '杰尼龟'
    p_sex = '女'
    p_nation = '龟族'
    workplace = '亚斯兰迪'
    phone = '12345678'
    p_idnumber = '44021254654'
    # msg = p_service.add_passenger(u_id, p_name, p_idnumber,
    #                               p_sex, p_nation, workplace, phone)['msg']
    msg = p_service.add_passenger(u_id, p_name, p_idnumber)['msg']
    p_service.curClose()
    print(msg)


def buyTicket_test():
    p_id = 'P0001'
    f_id = 'WH0001'
    s_level = 'E'
    p_service = pasService()

    msg = p_service.buy_ticket(p_id, f_id, s_level)['msg']
    p_service.curClose()
    print(msg)


def find_fuction(service):
    # res = service.find_user()['object']
    # res = service.find_passenger(p_id='P0002')['object']
    # res = service.buy_record('P0001')['object']
    # res = service.find_flight(airline="四川")['object']
    res = service.find_passenger(u_id='bbz')['object']
    res2 = []
    print(res)
    for data in res:
        print(data)
        res2.append({index: key for index, key in enumerate(data)})

    print(res2)
    service.curClose()


def add_function(service):
    # res = service.add_airline(a_id='CC', a_name='哈哈公司', a_place='苏格兰', ser_phone='14546231')
    # res = service.add_flight(dep_station='大连', dest_station='广西', dep_time='2021-09-05 13:00',
    #                          arr_time='2021-09-05 17:00', seat=300, a_id='CC')
    # res = service.add_seat(f_id='CC0432', s_level='F', price=5200, s_number=30)
    res = service.buy_ticket('P0001', 'CC0432', 'F')['msg']
    print(res)
    service.curClose()


def delete_function(service):
    res = service.delete_airline('CC')
    print(res['msg'])
    service.curClose()


def update_function(service):
    # res = service.update_airline(a_id='CC', a_place='台北')
    # res = service.update_passenger(p_id='P3242', p_idnumber='440789521', workplace='清河东路')
    # res = service.update_pwd('bbz', 'a12387')
    # res = service.update_flight(f_id='CC0432', dest_station='贵州', seat=320)
    res = service.update_seat(f_id='CC0432', s_level='F', price=5000)
    print(res['msg'])
    service.curClose()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airticket.settings")
    django.setup()
    # addPas_test()
    # buyTicket_test()
    # find_fuction(userService())
    add_function(pasService())
    # update_function(flService())
    # delete_function(flService())
