#!/usr/bin/env python
import re   #导入re模块
import cmdict as cm  #导入cmdict模块，命名为cm
def findmeas():
    with open('Demo.a2l','r') as f:  #打开Demo.a2l，读出内容存入txt，关闭文件
        txt=f.read()
        f.close()
    ls=[]
    le=[]
    meas=[]
    name=[]
    for m in re.finditer('/begin MEASUREMENT\s*([\w|\[\]]*)',txt): #匹配measurement开始的位置，放入ls，将名字分组，放入name
        ls.append(m.start())
        name.append(m.group(1))
    ls.sort()  #从小到大排序
    for m in re.finditer('/end MEASUREMENT',txt):  #匹配measurement结束的位置，放入le
        le.append(m.end())
    le.sort()  #从小到大排序
    for i in range(len(ls)):  #把每个measurement内容放入meas
        meas.append(txt[ls[i]:le[i]])
   #print meas[0]
    return meas,name #返回


def findunit(meas,cm_unit):
    m_unit=[]
    for con in meas:  #将meas中的内容一个个放入con
        m=re.search('".*"\s*\w*\s*(\w*)',con) #匹配每个measurement中的CM
        if(m!=None):
            m_unit.append(cm_unit[m.group(1)])#如果CM存在，根据CM的名字查找其中的单位，放入m_unit
        else:
            m_unit.append('None')#如果CM不存在，在m_unit中写入'None'
    return m_unit  #返回

def findupn(meas): #同理找到是否有upn，和upn的内容
    upn=[]
    upn_text=[]
    for con in meas:
        m=re.search(r'ANNOTATION_LABEL\s*"(UPN)"',con)
        if m!=None:
            upn.append('y')
            m2=re.search('/begin ANNOTATION_TEXT\s*"(\w*)"',con[m.end():])
            if m2!=None:
                upn_text.append(m2.group(1))
            else:
                upn_text.append('')
        else:
            upn.append('n')
            upn_text.append('')
    return upn,upn_text

def findVN(meas):#找到是否有Variable Note，和Variable Note名
    VN=[]
    VN_text=[]
    for con in meas:
        m=re.search(r'ANNOTATION_LABEL\s*"(Variable Note)"',con)
        if m!=None:
            VN.append('y')
            m2=re.search('/begin ANNOTATION_TEXT\s*"(.*?)"',con[m.end():])
            if m2!=None:
                VN_text.append(m2.group(1))
            else:
                VN_text.append('')
        else:
            VN.append('n')
            VN_text.append('')
    return VN,VN_text













    
