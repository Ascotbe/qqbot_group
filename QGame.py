import time
import json
import random

int_file = 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\Integral_users.txt'
def IntSignIn(bot, contact, member):
    if member != None:
        with open(int_file) as file_obj:
            #字典，值为列表[今天打卡状态1215, 积分总值]
            integral_users = json.load(file_obj)
        
        #记录今天时间
        time_today = str(time.localtime(time.time()).tm_mon)+str(time.localtime(time.time()).tm_mday)
        integral_users['today'] = time_today

        if integral_users.__contains__(member.uin) == False:
            integral_users[member.uin] = ['0', 0]
        state_users = integral_users[member.uin]
        state_today = integral_users['today']

        #如果打卡时间不是今天，则打卡
        if state_users[0] != state_today:
            score = random.randint(1, 30)
            state_users[0] = state_today
            state_users[1] += score
            users_str = '恭喜'+member.name+'打卡成功！获得积分'+str(score)+'\n目前拥有积分'+str(state_users[1])+'\n up!up！'
            bot.SendTo(contact, users_str, resendOn1202=False)
        else:
            score = random.randint(1, 15)
            state_users[1] -= score
            users_str = member.name+',皮痒啦？想再白嫖一次？\n说话的同时拿起了菜刀你花了'+str(score)+'分破财消灾\n目前只剩下'+str(state_users[1])+'分'
            bot.SendTo(contact, users_str, resendOn1202=False)
        integral_users[member.uin] = state_users

        with open(int_file, 'w') as file_obj:
            json.dump(integral_users, file_obj)
            print('已写入积分系统')
    return True

def IntegralRob(bot, contact, member, content):
    '''-------积分抢劫-------'''
    if member != None:
        #更新名字
        update = bot.List('group', contact.name)
        if update:
            up = update[0]
            bot.Update(up)
        #得到抢劫者与被抢劫者的名字与qq
        robber = member.uin
        beRobbeder_name = content.strip('抢劫@')
        beRobbeder_name = beRobbeder_name.strip(' ')
        if random.random() < 0.3:
            #没能抢劫成功
            bot.SendTo(contact, member.name+'，你被'+beRobbeder_name+'摁在地上♂，没能抢到积分。')
        else:
            #抢劫成功
            beRobbeder_qq = ''
            liveFlag = True
            gList = bot.List('group', contact.name)[0]
            for item in bot.List(gList):
                if item.name == beRobbeder_name:
                    beRobbeder_qq = item.uin
                    break
            else:
                liveFlag = False
                bot.SendTo(contact, member.name+', '+beRobbeder_name+'喵喵喵人家在吗？')
            if liveFlag:
                #得到每个人的积分
                int_file = 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\Integral_users.txt'
                with open(int_file) as file_obj:
                    integral_users = json.load(file_obj)
                
                #判断两人是否存在积分库中
                if integral_users.__contains__(robber) == False:
                    integral_users[robber] = ['0', 10] 
                if integral_users.__contains__(beRobbeder_qq) == False:
                    integral_users[beRobbeder_qq] = ['0', 10] 
                
                #抢劫得到的积分
                range_high = int(int(integral_users[beRobbeder_qq][1])/4*0.08)
                range_low = 1
                
                #判断被抢劫者有没有积分
                if int(integral_users[beRobbeder_qq][1]) <= 0:
                    bot.SendTo(contact, member.name+'，'+beRobbeder_name+'对方积分为0呐！')
                else:
                    if range_high < range_low:
                        range_high, range_low = range_low, range_high
                    score_rob = random.randint(range_low, range_high)
                    integral_users[robber][1] += score_rob
                    integral_users[beRobbeder_qq][1] -= score_rob
                    bot.SendTo(contact, member.name+'，'+beRobbeder_name+'被你摁在了地上♂，从某地方掉出了'+str(score_rob)+'点积分，你发出了啊♂的声音拍拍对方的屁股走了')
                    with open(int_file, 'w') as file_obj:
                        json.dump(integral_users, file_obj)
                        print('抢劫完成')
    else:
        bot.SendTo(contact, '喵喵喵喵？？对方在群了吗？？？')


def InquireIntegral(bot ,contact, member, content):
    '''-------查询积分-------'''
    with open(int_file) as file_obj:
        integral_users = json.load(file_obj)
    if contact.ctype == 'buddy':
         man_qq = contact.uin
         man_name = contact.name
    else:
        man_qq = member.uin
        man_name = member.name
    man_integral = integral_users[man_qq][1]
    bot.SendTo(contact, man_name+', 你的积分现在有'+str(man_integral)+'！')