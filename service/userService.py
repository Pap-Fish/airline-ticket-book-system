from django.db import connection
import django
import os
import logging
from service.passengerService import pasService
logging.basicConfig(level=logging.INFO, format='%(asctime)s  - %(levelname)s - %(message)s')


class userService:
    def __init__(self):
        self.cur = connection.cursor()

    def curClose(self):
        self.cur.close()

    def find_user(self, u_id=None):
        rmsg = {}
        if u_id:
            sql = "select * from user5074 where u_id='{}'".format(u_id)
        else:
            sql = "select * from user5074"
        try:
            self.cur.execute(sql)
            user = self.cur.fetchall()
            rmsg['object'] = user
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "系统出错"
        return rmsg

    # 登录
    def login(self, u_id, pwd):
        rmsg = {}
        sql = "select * from user5074 where u_id='{}'".format(str(u_id))
        try:
            self.cur.execute(sql)
            user = self.cur.fetchone()
            if user is None:
                rmsg['msg'] = '用户名不存在！'
            elif pwd != user[2]:
                rmsg['msg'] = '密码错误！'
            else:
                rmsg['msg'] = 'success'
                rmsg['object'] = user
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "系统出错"
        return rmsg

    # 注册
    def register(self, u_id, pwd):
        rmsg = {}
        sql = "select u_id from user5074"
        try:
            self.cur.execute(sql)
            users = self.cur.fetchall()
            for u in users:
                if u_id in u:
                    rmsg['msg'] = '用户名已存在！'
                    return rmsg
            sql = "insert into user5074 values('{u_id}','user','{pwd}')".format(u_id=u_id, pwd=pwd)
            self.cur.execute(sql)
            rmsg['msg'] = 'success'
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "系统出错"
        return rmsg

    # 绑定旅客身份
    def user_bind_pas(self, u_id, p_id):
        rmsg = {}
        p_service = pasService()
        try:
            user = self.find_user(u_id)['object']
            passenger = p_service.find_passenger(p_id)['object']
            p_service.curClose()
            if user and passenger:
                sql = "insert into user5074 values('{}','{}')".format(u_id, p_id)
                self.cur.execute(sql)
                rmsg['msg'] = "绑定成功"
            else:
                rmsg['msg'] = "查找不到用户和乘客"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "绑定出错"
        return rmsg

    def update_pwd(self, u_id, pwd):
        rmsg = {}
        sql = "update user5074 set u_password='{}' where u_id='{}'".format(pwd, u_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "修改成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "修改出错"
        return rmsg

    def find_passenger(self, u_id):
        rmsg = {}
        sql = "select u_id,p.* from up5074 as up,passenger5074 as p where up.p_id=p.p_id and u_id='{}'".format(u_id)
        try:
            self.cur.execute(sql)
            passengers = self.cur.fetchall()
            rmsg['object'] = passengers
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "查找出错"
        return rmsg

    def delete_passenger(self, u_id, p_id):
        rmsg = {}
        sql = "delete from up5074 where u_id='{}' and p_id='{}'".format(u_id, p_id)
        try:
            self.cur.execute(sql)
            rmsg['msg'] = "解绑成功"
        except Exception as e:
            logging.warning(e)
            rmsg['msg'] = "删除出错"
        return rmsg




