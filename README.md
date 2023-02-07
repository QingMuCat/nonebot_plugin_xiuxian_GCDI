# nonebot_plugin_xiuxian_GCDI

_:tada::tada::tada:修仙模拟器！:tada::tada::tada:_<br>
_:tada::tada::tada:群与频道数据互通:tada::tada::tada:_<br>
## 简介

本插件主要为实现群聊修仙功能,最近经常封号，请自行判断后再使用，已默认转成图片模式，如需关闭，可在config.py处调整img字段为false
并适配了频道与群聊数据互通

## 特色功能

  指令较多，具体查看指令 修仙帮助<br>
  1、悬赏令系统：发送指令 悬赏令帮助 获取信息<br>
  2、宗门系统：发送指令 宗门帮助 获取信息<br>
  3、世界boss系统：发送 世界boss帮助 获取信息<br>
  4、坊市：查询商店信息，当前商品为用户自行上架拍卖，发送指令 背包帮助 获取信息<br>
  5、灵庄：银行系统，发送 灵庄帮助 获取信息<br>
  6、功法：功法系统，发送指令 功法帮助<br>
  7、炼丹：发送 炼丹帮助 获取对应操作指令，需要炼丹炉，可在世界boss处获取。<br>
  8、秘境：发送 秘境帮助 获取对应操作指令。<br>

## 安装
1、下载插件文件

- 使用github处拉取源码使用
无镜像：
```
git clone https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI
```
镜像：https://ghproxy.com/
```
git clone https://ghproxy.com/https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI
```

2、安装依赖：

```
pip install -r requirements.txt
```

3、如果遇到问题，请先百度和查看下方的 【一些问题】

4、如解决不了进交流群：588907147 提问，提问请贴上完整的日志

## 配置文件
配置文件下载地址：- [xiuxianres](https://github.com/QingMuCat/xiuxianres/tree/master)：修仙插件资源库
1、配置文件下载后，放置BOT主目录<br>
2、子插件的配置会在插件运行后在子插件文件中生成config.json文件，该文件字段含义在同级目录的xxxconfig.py有备注。注意：修改配置只需要修改json即可，修改.py文件的话需要删除json文件才会生效，任何修改都需要重启bot

## 更新
使用github处拉取源码使用的
进入插件目录执行命令：
```
git pull
```


## 群聊与频道部分功能展示

![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E7%BE%A4%E8%81%8A%E7%B4%A0%E6%9D%901.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E7%BE%A4%E8%81%8A%E7%B4%A0%E6%9D%902.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E9%A2%91%E9%81%93%E7%B4%A0%E6%9D%901.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E9%A2%91%E9%81%93%E7%B4%A0%E6%9D%902.png)
## 一些问题

- 当前首次使用，未自动创建json文件及sql文件，请在[github](https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI)处，目录data -> xiuxian
处下载的文件，放置于bot目录，data -> xiuxian文件夹处
- 当为放置为plugins目录使用时，请修改根目录下__init__.py文件中的42行：src=''中的内容，填写的是存放插件的目录，一般情况下 src='src.plugins.'  如有不同请按照格式修改
## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架，NB天下第一可爱。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [nonebot_plugin_xiuxian](https://github.com/s52047qwas/nonebot_plugin_xiuxian)：原版修仙

## 插件依赖

- nonebot2
- nonebot-adapter-onebot
- go-cqhttp

## 支持

大家喜欢的话可以给这个项目点个star

有bug、意见和建议都欢迎提交 [Issues](https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI/issues) 
或者联系进入QQ交流群：588907147

## 许可证
本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证

## 饼（不知多久会实现）
TODO：<br>
1.重构本项目，不影响数据情况下，使用户完美迁移；<br>
2.一套代码跑所有BOT平台；<br>
3.增加功能，有想法的直接加群588907147<br>
4.云端计划（遥遥无期）：大概就是把数据搬上云端，这样让所有bot链接数据库，共用数据库<br>