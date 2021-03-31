# 公寓出租屋管理系统

## 1 简介

本管理系统基于Django前后端混合开发，使用Bootstrap构建前端页面，基本实现公寓出租屋管理系统功能。

## 2 模块功能划分

### 2.1 用户模块

模块以app划分，功能封装成类实现，方法通过定义get或post函数调用

<table>
<caption>管理员模块/功能</caption>
<thead>
<tr>
<th>模块/app</td>
  <th>功能/views</th>
  <th>方法/method</th>
  <th>备注</th>
 </tr>
</thead>
 <tbody>
 <tr>
  <td rowspan="7">Manager</td>
  <td>用户注册/Register</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>用户登录/Login</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>密码重置/ResetPassword</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>用户登出/Logout</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>主页/MainPage</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>管理页面框架/UserMgrBase</td>
  <td>get</td>
  <td>用户管理功能主体页面以iframe接入</td>
 </tr>
 <tr>
  <td>404页面/page_not_found</td>
  <td colspan="2"></td>
 </tr>
 <tr>
  <td rowspan="9">iframe_api</td>
  <td>首页/Home</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>用户帐号管理/Account</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>用户信息管理/UserDetail</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>公寓信息查询/HouseInfo</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>房间信息查询/RoomInfo</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>房型信息查询/TypeInfo</td>
  <td>get</td>
  <td></td>
 </tr>
 <tr>
  <td>新订单/NewOrder</td>
  <td>get/post</td>
  <td></td>
 </tr>
 <tr>
  <td>用户订单/UserOrder</td>
  <td>get/post</td>
  <td>预留支付功能</td>
 </tr>
 <tr>
  <td>合同/Contract</td>
  <td>get</td>
  <td></td>
 </tr>
</tbody></table>

### 2.2 管理员模块

管理模块基本由Django admin功能实现

<table>
<caption>管理员模块/功能</caption>
<thead>
<tr>
<th>模块</th>
<th>功能</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">管理员管理</td>
<td>管理员登录</td>
</tr>
<tr>
<td>添加管理员</td>
</tr>
<tr>
<td>管理员信息管理</td>
</tr>
<tr>
<td>管理员密码管理</td>
</tr>
<tr>
<td rowspan="3">公寓信息管理</td>
<td>查看公寓信息</td>
</tr>
<tr>
<td>维护公寓信息</td>
</tr>
<tr>
<td>添加公寓信息</td>
</tr>
<tr>
<td rowspan="3">预约管理</td>
<td>预约确认</td>
</tr>
<tr>
<td>查看预约</td>
</tr>
<tr>
<td>取消预约</td>
</tr>
<tr>
<td rowspan="4">房型管理</td>
<td>添加房型</td>
</tr>
<tr>
<td>修改房型</td>
</tr>
<tr>
<td>查看房型</td>
</tr>
<tr>
<td>删除房型</td>
</tr>
<tr>
<td rowspan="4">房间信息管理</td>
<td>添加房间信息</td>
</tr>
<tr>
<td>修改房间信息</td>
</tr>
<tr>
<td>查看房间信息</td>
</tr>
<tr>
<td>删除房间信息</td>
</tr>
<tr>
<td rowspan="3">合同管理</td>
<td>查看合同</td>
</tr>
<tr>
<td>修改合同</td>
</tr>
<tr>
<td>增加合同</td>
</tr>
<tr>
<td rowspan="4">用户管理</td>
<td>用户帐号管理</td>
</tr>
<tr>
<td>用户信息管理</td>
</tr>
<tr>
<td>添加/删除用户</td>
</tr>
<tr>
<td>用户权限管理</td>
</tr>
</tbody>
</table>

## 3 数据及表结构

通过Django ORM创建数据表结构，增删改查数据条目。本系统默认使用PyMySQL接入MySQL数据库，详细可通过RentalHouseManage文件夹下settings.py文件DATABASES条目进行配置。

<table>
  <caption>ORM类</caption>
<thead>
  <tr>
  <th>表/models</th>
  <th>字段</th>
  <th>类型</th>
  <th>备注</th>
 </tr>
 </thead>
 <tbody>
 <tr>
  <td rowspan="5">User(继承AbstractUser以实现admin功能,此处均为扩展字段)</td>
  <td>phone</td>
  <td>BigInt</td>
  <td></td>
 </tr>
 <tr>
  <td>wechat</td>
  <td>Char</td>
  <td></td>
 </tr>
 <tr>
  <td>detail</td>
  <td>外键</td>
  <td>外键-&gt;UserDetail</td>
 </tr>
 <tr>
  <td>room</td>
  <td>外键</td>
  <td>外键-&gt;Room</td>
 </tr>
 <tr>
  <td>createTime</td>
  <td>DateTime</td>
  <td>自动创建</td>
 </tr>
 <tr>
  <td rowspan="4">UserDetail</td>
  <td>realname</td>
  <td>Char</td>
  <td>最大8位</td>
 </tr>
 <tr>
  <td>gender</td>
  <td>SmallInt</td>
  <td>0隐藏 1男 2女</td>
 </tr>
 <tr>
  <td>idCard</td>
  <td>BigInt</td>
  <td>身份证号</td>
 </tr>
 <tr>
  <td>cardCopy</td>
  <td>File</td>
  <td>身份证复印件，存入文件地址</td>
 </tr>
 <tr>
  <td rowspan="6">HouseInfo(建议只存一条，多条数据取第一条）</td>
  <td>houseName</td>
  <td>Char</td>
  <td>最大8位</td>
 </tr>
 <tr>
  <td>houseDesc</td>
  <td>Char</td>
  <td>最大256位</td>
 </tr>
 <tr>
  <td>houseSlogan</td>
  <td>Char</td>
  <td>最大16位</td>
 </tr>
 <tr>
  <td>location</td>
  <td>Char</td>
  <td>最大32位</td>
 </tr>
 <tr>
  <td>brand</td>
  <td>File</td>
  <td></td>
 </tr>
 <tr>
  <td>houseImg</td>
  <td>File</td>
  <td></td>
 </tr>
 <tr>
  <td rowspan="6">Room</td>
  <td>roomId</td>
  <td>Int</td>
  <td>主键</td>
 </tr>
 <tr>
  <td>floor</td>
  <td>Int</td>
  <td></td>
 </tr>
 <tr>
  <td>state</td>
  <td>SmallInt</td>
  <td>0闲置 1预定 2使用</td>
 </tr>
 <tr>
  <td>type</td>
  <td>外键</td>
  <td>外键-&gt;RoomType</td>
 </tr>
 <tr>
  <td>roomDesc</td>
  <td>Char</td>
  <td>最大255位</td>
 </tr>
 <tr>
  <td>roomImg</td>
  <td>File</td>
  <td></td>
 </tr>
 <tr>
  <td rowspan="7">RoomType</td>
  <td>typeName</td>
  <td>Char</td>
  <td>最大16位</td>
 </tr>
 <tr>
  <td>typeImg</td>
  <td>File</td>
  <td></td>
 </tr>
 <tr>
  <td>area</td>
  <td>Float</td>
  <td>面积</td>
 </tr>
 <tr>
  <td>edayRent</td>
  <td>Float</td>
  <td>每日租金</td>
 </tr>
 <tr>
  <td>emonRent</td>
  <td>Float</td>
  <td>每月租金</td>
 </tr>
 <tr>
  <td>eDeposit</td>
  <td>Float</td>
  <td>押金</td>
 </tr>
 <tr>
  <td>TypeDesc</td>
  <td>Char</td>
  <td></td>
 </tr>
 <tr>
  <td rowspan="9">Order</td>
  <td>orderId</td>
  <td>Auto</td>
  <td>订单号，主键</td>
 </tr>
 <tr>
  <td>user</td>
  <td>外键</td>
  <td>外键-&gt;User</td>
 </tr>
 <tr>
  <td>room</td>
  <td>外键</td>
  <td>外键-&gt;Room</td>
 </tr>
 <tr>
  <td>inTime</td>
  <td>Date</td>
  <td></td>
 </tr>
 <tr>
  <td>outTime</td>
  <td>Date</td>
  <td></td>
 </tr>
 <tr>
  <td>createTime</td>
  <td>DateTime</td>
  <td>自动创建</td>
 </tr>
 <tr>
  <td>ePay</td>
  <td>Float</td>
  <td>预付金额</td>
 </tr>
 <tr>
  <td>payState</td>
  <td>Boolean</td>
  <td>True 已支付 False 未支付</td>
 </tr>
 <tr>
  <td>orderDesc</td>
  <td>Char</td>
  <td>最大255位</td>
 </tr>
 <tr>
  <td rowspan="10">Contract</td>
  <td>contractId</td>
  <td>Auto</td>
  <td>合同号，主键</td>
 </tr>
 <tr>
  <td>user</td>
  <td>外键</td>
  <td>外键-&gt;User</td>
 </tr>
 <tr>
  <td >room</td>
  <td>外键</td>
  <td>外键-&gt;Room</td>
 </tr>
 <tr>
  <td>inTime</td>
  <td>Date</td>
  <td></td>
 </tr>
 <tr>
  <td>outTime</td>
  <td>Date</td>
  <td></td>
 </tr>
 <tr>
  <td>createTime</td>
  <td>DateTime</td>
  <td>自动创建</td>
 </tr>
 <tr>
  <td>rPay</td>
  <td>Float</td>
  <td>实付金额</td>
 </tr>
 <tr>
  <td>payState</td>
  <td>Boolean</td>
  <td>True 已支付 False 未支付</td>
 </tr>
 <tr>
  <td>contract</td>
  <td>Text</td>
  <td>合同内容</td>
 </tr>
 <tr>
  <td>signature</td>
  <td>File</td>
  <td>合同复印件</td>
 </tr>
</tbody></table>

*未提及主键的model均自动创建主键（‘id’）

## 4 开发相关

开发使用环境为Python 3.6.8，Django 2.2.19，PyMySQL 1.0.2

使用ide为PyCharm 2020.3.4 (Community Edition)。

## 5 第一次运行

1. 运行前配置Python虚拟环境确保为3.6.8版本

2. 设置RentalHouseManage/settings.py中设置DEBUG为False

3. cd进入本系统文件根目录下以虚拟环境执行下面命令以获取正确的运行环境

   ```shell
   pip3 install -r requirement.txt
   ```

4. 在配置好数据库后，系统文件根目录下执行下面命令以完成数据模型构建

   ```shell
   pyhon3 manager.py makemigrations
   pyhon3 manager.py migrate
   ```

5. 以上完成后，系统文件根目录下执行下面命令，输入用户名，密码，邮箱以创建超级管理员

   ```shell
   pyhon3 manager.py createsuperuser
   ```

6. 最后输入以下命令运行系统(ip为ip地址，port为端口）

   ```shell
   pyhon3 manager.py runserver ip:port
   ```

7. 在浏览器中输入ip:port能进入主页即为正常运行

## 6 目前存在的不足

本系统为管理功能的基本实现，在摸索中开发，因此可能会存在某些不足，尽请在issue版面提交，谢谢