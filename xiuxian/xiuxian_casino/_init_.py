import re
import random

from typing import Any, Tuple

from nonebot.params import RegexGroup
from nonebot.adapters import Message, Bot
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    PRIVATE_FRIEND,
    GROUP,
    Message,
    GroupMessageEvent,
    MessageSegment
)

from nonebot_plugin_guild_patch import (
    GUILD,
    GUILD_OWNER,
    GUILD_ADMIN,
    GUILD_SUPERUSER,
    GuildMessageEvent
)

from ..utils import data_check_conf, get_msg_pic
from ..command import dufang
from ..cd_manager import add_cd, check_cd, cd_msg
from ..xiuxian_config import XiuConfig, JsonConfig
from ..xiuxian2_handle import XiuxianDateManage


sql_message = XiuxianDateManage()  # sql类


@dufang.handle()
async def _(bot: Bot, event: MessageEvent, args: Tuple[Any, ...] = RegexGroup()):
    await data_check_conf(bot, event)
    
    try:
        user_id, group_id, mess = await data_check(bot, event)
    except MsgError:
        return

    if cd := check_cd(event, '金银阁'):
        # 如果 CD 还没到 则直接结束
        await dufang.finish(cd_msg(cd), at_sender=True)

    user_message = sql_message.get_user_message(user_id)

    add_cd(event, XiuConfig().dufang_cd, '金银阁')

    if args[2] is None:
        msg = f"请输入正确的指令，例如金银阁10大、金银阁10奇、金银阁10猜3"
        

    price = args[1]  # 300
    mode = args[2]  # 大、小、奇、偶、猜
    mode_num = 0
    if mode == '猜':
        mode_num = args[3]  # 猜的数值
        if str(mode_num) not in ['1', '2', '3', '4', '5', '6']:
            msg = f"请输入正确的指令，例如金银阁10大、、金银阁10奇、金银阁10猜3"


    price_num = int(price)
    if int(user_message.stone) < price_num:
        msg = "道友的金额不足，请重新输入！"
    elif price_num == 0:
        msg = "走开走开，0块钱也赌！"

    value = random.randint(1, 6)
    msg = Message("[CQ:dice,value={}]".format(value))

    if value >= 4 and str(mode) == "大":
        sql_message.update_ls(user_id, price_num, 1)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜对了，收获灵石{}块".format(value, price_num)
        
    elif value <= 3 and str(mode) == "小":
        sql_message.update_ls(user_id, price_num, 1)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜对了，收获灵石{}块".format(value, price_num)
    elif value %2==1 and str(mode) == "奇":
        sql_message.update_ls(user_id, price_num, 1)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜对了，收获灵石{}块".format(value, price_num)
    elif value %2==0 and str(mode) == "偶":
        sql_message.update_ls(user_id, price_num, 1)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜对了，收获灵石{}块".format(value, price_num)

    elif str(value) == str(mode_num) and str(mode) == "猜":
        sql_message.update_ls(user_id, price_num * 5, 1)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜对了，收获灵石{}块".format(value, price_num * 5)

    else:
        sql_message.update_ls(user_id, price_num, 2)
        await dufang.send(msg)
        msg = "最终结果为{}，你猜错了，损失灵石{}块".format(value, price_num)




async def data_check(bot, event):
    """
    判断用户信息是否存在
    """
    conf_data = JsonConfig().read_data()
    if isinstance(event, GroupMessageEvent):
        user_qq = event.get_user_id()
        group_id = await get_group_id(event.get_session_id())
        msg = sql_message.get_user_message(user_qq)
        if msg:
            try:
                if group_id in conf_data["group"]:
                    print('当前存在禁用数据')
                    msg = f"本群已关闭修仙模组，请联系管理员开启！"
                    pic = await get_msg_pic(msg)#
                    await bot.send(event=event, message=MessageSegment.image(pic))
                    raise ConfError
                else:
                    pass
            except KeyError:
                pass
        else:
            await bot.send(event=event, message=f"没有您的信息，输入【我要修仙】加入！")
            raise MsgError
    elif isinstance(event, GuildMessageEvent):
        tiny_id = event.get_user_id()
        group_id = f"{event.guild_id}@{event.channel_id}"
        msg = sql_message.get_user_message3(tiny_id)
        if msg:
            user_qq = msg.user_id
            try:
                if group_id in conf_data["group"]:
                    print('当前存在禁用数据')
                    msg = f"本群已关闭修仙模组，请联系管理员开启！"
                    pic = await get_msg_pic(msg)#
                    await bot.send(event=event, message=MessageSegment.image(pic))
                    raise ConfError
                else:
                    pass
            except KeyError:
                pass
        else:
            await bot.send(event=event, message=f"没有您的QQ绑定信息，输入【绑定QQ+QQ号码】进行绑定后再输入【我要修仙】加入！")
            raise MsgError
    else:
        user_qq = event.get_user_id()
        group_id = None
        msg = sql_message.get_user_message(user_qq)
        if msg:
            pass
        else:
            await bot.send(event=event, message=f"没有您的信息，输入【我要修仙】加入！")
            raise MsgError
    return user_qq, group_id, msg



async def get_group_id(session_id):
    """获取group_id"""
    res = re.findall("_(.*)_", session_id)
    group_id = res[0]
    return group_id

    

class MsgError(ValueError):
    pass


class ConfError(ValueError):
    pass