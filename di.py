import json
from tianqi import *
import re
from QGame import *
import time
from TuLin import *
from qqbot import qqbotsched
from ss_pythonic_spider import *
from FanYi import *
from XiaoHua import *
bangzhu="""
/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳
@me  在线基情聊天（关闭了骂人功能)
@me  -help or --help查看帮助文档
@me  签到
@me  查询积分
@me  ssr帐号/SSR帐号
@me  ssr下载/SSR下载
@me  SSR全部帐号/ssr全部帐号(会刷屏)
@me  讲个笑话
@me  翻译(可以翻译中文和英文)
Weather  天气查询 城市
Master   仅限主人使用开始关闭功能
/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳/太阳
"""

SSR_DiZi=""" 
/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心
1. Windows客户端：https://github.com/shadowsocksrr/shadowsocksr-csharp/releases                            
2. Mac客户端：https://github.com/flyzy2005/ss-ssr-clients/raw/master/ssr/SS-X-R.zip                        
3. Linux客户端：https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation                           
4. Android/安卓客户：https://github.com/flyzy2005/ss-ssr-clients/raw/master/ssr/ShadowsocksR-3.4.0.8.apk
/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心/爱心
"""



# SSR列表
def ssr_work(file_name):
    ssr_list = []
    with open(file_name, 'r') as f:
        for i in f.readlines():
            ssr_list.append(i)
    return ssr_list
#笑话列表
def Xiao_work(file_name):#转换成列表
    XiaoHua_list = []
    with open(file_name, 'r') as f:
        for i in f.readlines():
            XiaoHua_list.append(i)
    return XiaoHua_list


#天气文件    
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
                elif 'ssr帐号' in content[7:] or 'SSR帐号' in content[7:]:#第三优先级的子集，ssr帐号功能
                    ssr_list = ssr_work("C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\ss_ssr.txt")
                    random.shuffle(ssr_list)  #打乱列表顺序
                    iRandom = ssr_list[0:1] #取出打乱数据的第一个值
                    lib_d=" ".join(iRandom)#把列表转换成字符串
                    bot.SendTo(contact,lib_d)
                elif 'ssr全部帐号' in content[7:] or 'SSR全部帐号' in content[7:]:#第三优先级的子集，ssr全部帐号功能
                    ssr_list = ssr_work("C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\ss_ssr.txt")
                    lib_d=" ".join(ssr_list)#把列表转换成字符串
                    bot.SendTo(contact,lib_d)
                     #BaiDuFanYi(bot ,contact, member, content)
                elif 'SSR下载' in content[7:]  or 'ssr下载' in content[7:]:#第三优先级的子集，提供下载SSR地址
                    bot.SendTo(contact,SSR_DiZi)
                elif '翻译' in content[7:9]:#第三优先级的子集，翻译功能
                    FanYiHS(bot, contact, member, content)
                #elif '扫描' in content[7:9]:#第三优先级的子集，扫描端口功能
                    #DuanKouScan(bot, contact, member, content)
                elif '讲个笑话' in content[7:]:#第三优先级的子集，讲笑话功能
                    XiaoHua_list=Xiao_work("C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\XiaoHua_ssr.txt")
                    random.shuffle(XiaoHua_list)
                    iRandom = XiaoHua_list[0:1] #取出打乱数据的第一个值
                    XiaoHua_de=" ".join(iRandom)#把列表转换成字符串
                    bot.SendTo(contact,XiaoHua_de)
                elif '钓鱼岛' in content or '台湾' in content or '南海' in content or '南沙群岛' in content:#关键字过滤
                    bot.SendTo(contact,'/爱心永远是中国的,我爱中国~/爱心')
                elif '习近平'in content or '江泽民'in content or  '胡锦涛' in content or '周恩来' in content or '毛泽东' in content or '邓小平' in content or '刘少奇' in content or '李先念' in content or '杨尚昆' in content or '李克强' in content:#关键字过滤
                    bot.SendTo(contact,'/爱心心系国家~/爱心')
                elif '中国' in content or '共产党' in content or '共青团' in content or '中共' in content:#关键字过滤
                    bot.SendTo(contact,'/爱心我的心里只有党/爱心')
                elif '更新文件' in content[7:]:#第三优先级子集，更新一些爬取文件，以后爬取功能都可以放在这里
                    XiaoHua()
                    bot.SendTo(contact,'陛下吩咐的事情已完成~')
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
        if member.uin=='517383724':#设置好主人uin数字好关闭和开启机器人(好像会每天更新)
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


@qqbotsched(hour='12,13,14,15,23,0', minute='0')
def mytask(bot):#单独的定时爬取SSR帐号然后写入功能，需要开VPN
    Ssr_DinSiPaQu()
    gl = bot.List('group', 'te1')
    if gl is not None:
        for group in gl:
    #Ssr_DinSiPaQu()
            bot.SendTo(group, '任务执行完毕')