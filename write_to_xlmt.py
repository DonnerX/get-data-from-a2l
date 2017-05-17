#!/usr/bin/env python
import xlwt        #导入xlwt模块，用于进行Excel操作
import dealmeas as me  #导入之前编写的dealmeas.py 命名为me
import cmdict as cm    #导入之前编写的cmdict.py 命名为cm

meas,name=me.findmeas()  #返回两个List变量，当中存有a2l文件中的所有measurement的内容和名字，
d=cm.findcm()            #返回一个字典变量，其中含有每个Compus method对应的单位
unit=me.findunit(meas,d) #输入为单位字典和measurement的内容，根据measurement中引用的Compus method，查找到measurement中使用的单位
upn,upn_text=me.findupn(meas) #根据measurement中的内容返回两个List变量，当中存有每个measurement是否有upn和upn的内容
VN,VN_text=me.findVN(meas) #根据measurement中的内容返回两个List变量，VN当中存有每个measurement是否包含Variable Note字段，VN_text中存有Variable Note字段内容

wb = xlwt.Workbook()  #返回一个Excel对象，中间有Excel操作的各种方法
ws = wb.add_sheet('A Test Sheet') #返回一个sheet的对象，中间有Excel中sheet带有的方法

ws.write(0, 0,'name') #向第一行，第一列写入‘name’
ws.write(0, 1,'unit') #向第一行，第二列写入‘unit’
ws.write(0, 2,'upn')  #向第一行，第三列写入‘upn’
ws.write(0, 3,'upn_text') #向第一行，第四列写入‘upn_text’
ws.write(0, 4,'Variable Note') #向第一行，第五列写入‘Variable Note’
ws.write(0, 5,'VN_text') #向第一行，第六列写入‘VN_text’
i=0 #用于计数
print len(name),len(unit),len(upn),len(upn_text) #确认是否每个measurement都找到了unit ，upn 和upn_text

for u in unit:  #以行为单位写入各列的值
    ws.write(i+1,0,name[i])
    ws.write(i+1,1,unit[i])
    ws.write(i+1,2,upn[i])
    ws.write(i+1,3,upn_text[i])
    ws.write(i+1,4,VN[i])
    ws.write(i+1,5,VN_text[i])
    i+=1
#ws.write(2, 2, xlwt.Formula("A3+B3"))

print d['CM_T_VOLT_SW_08']
wb.save('Demo.xls')  #保存Excel文件
