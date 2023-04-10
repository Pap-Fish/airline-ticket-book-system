from random import randint
from django.db import connection
import logging


class flService:
    def __init__(self):
        self.cur = connection.cursor()

    def curClose(self):
        self.cur.close()

    def find_flight(self, f_id=None, dep_station=None, dest_station=None, airline=None, dep_time=None):
        if f_id:
            sql = "select f_id,dep_station,dest_station,dep_time,arr_time," \
                  "seat,a_name,status from flight5074 as f, airline5074 as a " \
                  "where f.a_id=a.a_id and f_id='{}'".format(f_id)

        else:
            sql = "select f_id,dep_station,dest_station,dep_time,arr_time," \
                  "seat,a_name,status from flight5074 as f, airline5074 as a where f.a_id=a.a_id "
            if airline:
                sql += "and a_name like '%{}%' ".format(airline)
            if dep_station:
                sql += "and dep_station like '%{}%' ".format(dep_station)
            if dest_station:
                sql += "and dest_station like '%{}%' ".format(dest_station)
            if dep_time:
                sql += "and dep_time like '%{}%'".format(dep_time)
        rmsg = {}
        try:
            self.cur.execute(sql)
            flight = self.cur.fetchall()
            rmsg['object'] = flight
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def find_airline(self, a_name=None):
        rmsg = {}
        sql = "select * from airline5074 "
        if a_name:
            sql += "where a_name like '%{}%'".format(a_name)
        try:
            self.cur.execute(sql)
            airlines = self.cur.fetchall()
            rmsg['object'] = airlines
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def find_fligt_seat(self, f_id):
        sql = "select * from seat5074 where f_id='{}'".format(f_id)
        rmsg = {}
        try:
            self.cur.execute(sql)
            seats = self.cur.fetchall()
            rmsg['object'] = seats
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def add_airline(self, **kwargs):
        rmsg = {}
        sql = "insert into airline5074 values('{}','{}','{}','{}')".format(
            kwargs['a_id'], kwargs['a_name'], kwargs['a_place'], kwargs['ser_phone']
        )
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "添加成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "添加出错"
        return rmsg

    def update_airline(self, a_id, a_name=None, a_place=None, ser_phone=None):
        rmsg = {}
        sql = "update airline5074 set "
        is_first = True
        if a_name:
            sql += "a_name='{}' ".format(a_name)
            is_first = False
        if a_place:
            if not is_first:
                sql += ','
            sql += "a_place='{}' ".format(a_place)
            is_first = False
        if ser_phone:
            if not is_first:
                sql += ','
            sql += "ser_phone='{}' ".format(ser_phone)
        sql += "where a_id='{}'".format(a_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "修改成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "修改出错"
        return rmsg

    def delete_airline(self, a_id):
        rmsg = {}
        sql = "delete from airline5074 where a_id='{}'".format(a_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "删除成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "删除出错"
        return rmsg

    def add_flight(self, **kwargs):
        rmsg = {}
        try:
            while True:
                f_id = kwargs['a_id']
                for i in range(4):
                    f_id += str(randint(0, 9))
                sql = "select * from flight5074 where f_id='{}'".format(f_id)
                self.cur.execute(sql)
                result = self.cur.fetchall()
                if not result:
                    break
            sql = "insert into flight5074 values('{}','{}','{}','{}','{}',{},'{}','待机')".format(
                f_id, kwargs['dep_station'], kwargs['dest_station'], kwargs['dep_time'], kwargs['arr_time'],
                kwargs['seat'], kwargs['a_id']
            )
            self.cur.execute(sql)
            rmsg['msg'] = "添加成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "添加出错"
        return rmsg

    def update_flight(self, f_id, dep_station=None, dest_station=None, dep_time=None,
                      arr_time=None, seat=None, status=None):
        rmsg = {}
        sql = "update flight5074 set "
        is_first = True
        if dep_station:
            sql += "dep_station='{}' ".format(dep_station)
            is_first = False
        if dest_station:
            if not is_first:
                sql += ','
            sql += "dest_station='{}' ".format(dest_station)
            is_first = False
        if dep_time:
            if not is_first:
                sql += ','
            sql += "dep_time='{}' ".format(dep_time)
            is_first = False
        if arr_time:
            if not is_first:
                sql += ','
            sql += "arr_time='{}' ".format(arr_time)
            is_first = False
        if seat:
            if not is_first:
                sql += ','
            sql += "seat={} ".format(seat)
            is_first = False
        if status:
            if not is_first:
                sql += ','
            sql += "status='{}' ".format(status)
        sql += "where f_id='{}'".format(f_id)
        print(sql)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "修改成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "修改出错"
        return rmsg

    def delete_flight(self, f_id):
        rmsg = {}
        sql = "delete from flight5074 where f_id='{}'".format(f_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "删除成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "删除出错"
        return rmsg

    def add_seat(self, **kwargs):
        rmsg = {}
        sql = "insert into seat5074 values('{}','{}',{},{})".format(
            kwargs['f_id'], kwargs['s_level'], kwargs['price'], kwargs['s_number']
        )
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "添加成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "添加出错"
        return rmsg

    def update_seat(self, f_id, s_level, price=None, s_number=None):
        rmsg = {}
        sql = "update seat5074 set "
        is_first = True
        if price:
            sql += "price={} ".format(price)
            is_first = False
        if s_number:
            if not is_first:
                sql += ','
            sql += "s_number={} ".format(s_number)
        sql += "where f_id='{}' and s_level".format(f_id, s_level)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "修改成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "修改出错"
        return rmsg

    def delete_seat(self, f_id, s_level):
        rmsg = {}
        sql = "delete from seat5074 where f_id='{}' and s_level-'{}'".format(f_id, s_level)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "删除成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "删除出错"
        return rmsg
