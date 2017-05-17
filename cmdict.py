#该文件用于建立一个字典变量，用于一一对应的存储COMPU_METHOD的名字和当中的单位
import re

def findcm():
    with open('Demo.a2l','r') as f:  #以只读的模式打开‘Demo.a2l文件’，命名为f对象
        txt=f.read()  #读取文件中的全部内容
        f.close()     #关闭文件
    ls=[]#建立一个空List，用于存储COMPU_METHOD（CM）开始的位置
    le=[]#建立一个空List，用于存储CM结束的位置
    cm=[]#建立一个空List，用于存储每个CM中的内容
    name=[]#建立一个空List，用于存储每个CM中的名字
    unit=[]#建立一个空List，用于存储每个CM中的单位
    for m in re.finditer('/begin COMPU_METHOD\s*(\w*)',txt): #finditer会返回一个迭代变量
        #循环找到每个CM开始的位置和CM的名字，放入ls和name，括号中的内容会被单独分组
        ls.append(m.start())
        name.append(m.group(1))#group（1）可以提取分组中的内容
    ls.sort()#将ls按照从小到大排序
    for m in re.finditer('/end COMPU_METHOD',txt):
        #同样循环找到每个CM结束的位置，放入le
        le.append(m.end())
    le.sort()#将le从小到大排序
    for i in range(len(ls)):
        cm.append(txt[ls[i]:le[i]]) #将每个ls，le配对取出中间的内容，即为CM的内容
    i=0
    for con in cm: #每次循环将一个cm中的内容放入con变量中
        m=re.search('"%\d+\.\d+"\s*"(.*?)"',con)  #匹配CM中的单位
        if m!=None:
            unit.append(m.group(1)) #如果单位存在，放入unit中，此处没有考虑如果单位不存在的情况。

    d=dict(zip(name,unit))#通过name 和 unit 形成一个一一对应的字典
    return d #返回该字典



