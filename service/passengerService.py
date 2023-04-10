import logging
from random import randint

from django.db import connection

from service.flightService import flService

logging.basicConfig(level=logging.INFO, format='%(asctime)s  - %(levelname)s - %(message)s')


class pasService:
    def __init__(self):
        self.cur = connection.cursor()

    def curClose(self):
        self.cur.close()

    def find_passenger(self, p_id=None):
        rmsg = {}
        if p_id:
            sql = "select * from passenger5074 where p_id='{}'".format(p_id)
        else:
            sql = "select * from passenger5074"
        try:
            self.cur.execute(sql)
            passenger = self.cur.fetchall()
            rmsg['object'] = passenger
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def add_passenger(self, u_id, p_name, p_idnumber, p_sex='男',
                      p_nation='汉族', workplace='无', telephone='无'):
        rmsg = {}
        try:
            while True:
                # p_id随机生成
                p_id = 'P' + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                sql = "select * from passenger5074 where p_id='{}'".format(p_id)
                self.cur.execute(sql)
                result = self.cur.fetchall()
                if not result:
                    break
            sql = "insert into passenger5074 values('{}','{}','{}','{}','{}','{}','{}')".format(
                p_id, p_name, p_sex, p_nation, p_idnumber, workplace, telephone
            )
            self.cur.execute(sql)

            # 绑定用户和乘客
            sql = "insert into up5074 value('{}','{}')".format(u_id, p_id)
            self.cur.execute(sql)
            rmsg['msg'] = '添加成功'
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "添加乘客出错"

        return rmsg

    def buy_ticket(self, p_id, f_id, s_level):
        rmsg = {}
        f_service = flService()
        try:
            self.cur.execute("call is_exceed('{}','{}', @res)".format(p_id, f_id))
            self.cur.execute("select @res")
            data = self.cur.fetchall()
            if data:
                result = data[0][0]
            if result == '超额':
                rmsg['msg'] = '超额购买！'
            else:
                # 生成机票编号
                while True:
                    t_id = 'T'
                    for i in range(5):
                        t_id += str(randint(0, 9))
                    sql = "select * from pticket5074 where t_id='{}'".format(t_id)
                    self.cur.execute(sql)
                    result = self.cur.fetchall()
                    if not result:
                        break
                # 生成座位号
                max_seat = f_service.find_flight(f_id)['object'][0][5]
                # print(max_seat)
                f_service.curClose()
                while True:
                    seat = randint(1, max_seat)
                    # 座位号查重
                    sql = "select * from pticket5074 where f_id='{}' and s_no='{}'".format(f_id, seat)
                    self.cur.execute(sql)
                    res = self.cur.fetchall()
                    if not res:
                        break
                de_gate = chr(randint(65, 90))
                print(de_gate)
                sql = "insert into pticket5074 values('{}','{}','{}','{}','{}','{}','有效')".format(
                    t_id, p_id, f_id, s_level, seat, de_gate
                )
                self.cur.execute(sql)
                rmsg['msg'] = '购买成功'

        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "购买功能出错"

        return rmsg

    def refund_ticket(self, t_id):
        rmsg = {}
        sql = "delete from pticket5074 where t_id='{}'".format(t_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "退票成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "退票功能出错"

        return rmsg

    def find_all_ticket(self):
        rmsg = {}
        try:
            self.cur.execute('select * from pticket5074')
            tickets = self.cur.fetchall()
            rmsg['object'] = tickets
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def find_passenger_ticket(self, p_id, f_id=None, dest_station=None, dep_time=None):
        rmsg = {}
        sql = "select * from tic_total where p_id='{}'".format(p_id)
        if f_id:
            sql += "and f_id='{}'".format(f_id)
        if dest_station:
            sql += "and dest_station like '%{}%'".format(dest_station)
        if dep_time:
            sql += "and dep_time like '%{}%'".format(dep_time)
        try:
            self.cur.execute(sql)
            tickets = self.cur.fetchall()
            rmsg['object'] = tickets
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def buy_record(self, p_id):
        rmsg = {}
        sql = "select p_id, p.f_id, p.s_level, price from pticket5074 as p, seat5074 as s " \
              "where p.f_id=s.f_id and p.s_level=s.s_level and p_id='{}'".format(p_id)
        try:
            self.cur.execute(sql)
            record = self.cur.fetchall()
            rmsg['object'] = record
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def update_passenger(self, p_id, p_name=None, p_sex=None, p_nation=None,
                         p_idnumber=None, workplace=None, telephone=None):
        rmsg = {}
        sql = "update passenger5074 set "
        is_first = True
        if p_name:
            sql += "p_name='{}' ".format(p_name)
            is_first = False
        if p_sex:
            if not is_first:
                sql += ','
            sql += "p_sex='{}' ".format(p_sex)
            is_first = False
        if p_nation:
            if not is_first:
                sql += ','
            sql += "p_nation='{}' ".format(p_nation)
            is_first = False
        if p_idnumber:
            if not is_first:
                sql += ','
            sql += "p_idnumber='{}' ".format(p_idnumber)
            is_first = False
        if workplace:
            if not is_first:
                sql += ','
            sql += "workplace='{}' ".format(workplace)
            is_first = False
        if telephone:
            if not is_first:
                sql += ','
            sql += "telephone='{}' ".format(telephone)
        sql += "where p_id='{}'".format(p_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "修改成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "修改出错"
        return rmsg

