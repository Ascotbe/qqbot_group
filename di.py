import json
from tianqi import *
import re
from QGame import *
import time

from TuLin import *
bangzhu="""
@me  在线基情聊天（关闭了骂人功能)
@me  -help or --help查看帮助文档
@me  签到
@me  查询积分
@me  翻译功能呢(由于各大翻译网站做了反爬取功能暂时关闭)
Weather  天气查询 城市
"""

city_file = 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\CityCodes.txt'
with open(city_file) as file_obj:
    city = json.load(file_obj)
    print('已写入天气')


def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):#最高优先级，判断是否自己说的话
        pass
    else:
        masterFlag = MasterCommands(bot, contact, member, content)#第二优先级，判断是否主人命令，如果是1继续才能继续执行文件
        if masterFlag=='1':
            
            if '@ME' in content:#第三优先级判断是否是艾特了我，如果不是不处理
                if '-help' in content or '--hlep' in content:#第三优先级的子集，判断是否查看帮助文档
                    bot.SendTo(contact,bangzhu,resendOn1202=False)
                    pass
                #elif '天气' in content:
                #elif content[7:9] == '天气':#[@ME]外加2个空格一共7个字符
                    #GetWeather(bot, contact, member, content, city)
                elif '签到' in content[7:9] or '冒泡' in content[7:9]:#第三优先级的子集，签到功能
                    IntSignIn(bot, contact, member)
                    pass
                elif '抢劫' in content[7:9]:#第三优先级的子集，抢劫功能
                    IntegralRob(bot, contact, member, content)
                    pass
                elif '查询' in content[7:9]:  #第三优先级的子集，查询功能
                    InquireIntegral(bot ,contact, member, content)
                    pass 	
                #if '翻译' in content[7:9]:#第三优先级的子集，翻译功能
                    #BaiDuFanYi(bot ,contact, member, content)
                elif content =='@ME':#第三优先级的子集查看是不是捣乱
                    bot.SendTo(contact,member.name+'你他喵能不能看hlpe??',resendOn1202=False)
                else :#第三优先级的子集聊天功能
                    answers =answer(content)
                    bot.SendTo(contact,answers,resendOn1202=False)
                    
            elif content[0:4]=='天气查询':#第三优先级，天气查询
                GetWeather(bot, contact, member, content, city)
         




def MasterCommands(bot, contact, member, content):
    '''!-------不反应或者反应-------!'''
    masterFlagFile_name = 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\MasterFlag.txt'
    if member != None:
        if member.uin=='1298802985':#设置好主人uin数字好关闭和开启机器人(好像会每天更新)
            if content == '退下吧':                               #关闭机器人
                bot.SendTo(contact, '臣妾告退~')
                with open(masterFlagFile_name, 'w') as file_obj:
                    json.dump('0', file_obj)
                    print('已修改为0')
            elif content == '爱妃':                               #开启查询机器人/聊天机器人
                bot.SendTo(contact, '臣妾来了~')                         
                with open(masterFlagFile_name, 'w') as file_obj:
                    json.dump('1', file_obj)
                    print('已修改为1')

    with open(masterFlagFile_name) as file_obj:
        flag = json.load(file_obj)
        print('已读取', flag)
    return flag

