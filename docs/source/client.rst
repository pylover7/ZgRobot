Client
==============================================

微信 API 操作类，有部分接口暂未实现，可自行调用微信接口。

.. module:: zgrobot.client

开始开发
------------

获取 access token
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Get_access_token.html

.. automethod:: Client.grant_token
.. automethod:: Client.get_access_token

.. note:: Client 的操作都会自动进行 `access token` 的获取和过期刷新操作，如果有特殊需求（如多进程部署）可重写 ``get_access_token``。

获取微信服务器IP地址
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Get_the_WeChat_server_IP_address.html

.. automethod:: Client.get_ip_list

自定义菜单
------------

自定义菜单创建接口
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Custom_Menus/Creating_Custom-Defined_Menu.html

.. automethod:: Client.create_menu

自定义菜单获取自定义菜单配置
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Custom_Menus/Getting_Custom_Menu_Configurations.html

.. automethod:: Client.get_menu

自定义菜单删除接口
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Custom_Menus/Deleting_Custom-Defined_Menu.html

.. automethod:: Client.delete_menu

自定义菜单个性化菜单接口
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Custom_Menus/Personalized_menu_interface.html

.. automethod:: Client.create_custom_menu
.. automethod:: Client.delete_custom_menu
.. automethod:: Client.match_custom_menu

获取自定义菜单配置接口
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Custom_Menus/Querying_Custom_Menus.html

.. automethod:: Client.get_custom_menu_config

消息管理
------------

客服接口
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Customer_Service/Customer_Service_Management.html

发送卡券接口暂时未支持。可自行实现。

.. automethod:: Client.add_custom_service_account
.. automethod:: Client.update_custom_service_account
.. automethod:: Client.delete_custom_service_account
.. automethod:: Client.upload_custom_service_account_avatar
.. automethod:: Client.get_custom_service_account_list
.. automethod:: Client.get_online_custom_service_account_list
.. automethod:: Client.send_text_message
.. automethod:: Client.send_image_message
.. automethod:: Client.send_voice_message
.. automethod:: Client.send_video_message
.. automethod:: Client.send_music_message
.. automethod:: Client.send_article_message
.. automethod:: Client.send_news_message
.. automethod:: Client.send_miniprogrampage_message

群发接口
``````````````````````````````

.. automethod:: Client.send_mass_msg
.. automethod:: Client.delete_mass_msg
.. automethod:: Client.send_mass_preview_to_user
.. automethod:: Client.get_mass_msg_status
.. automethod:: Client.get_mass_msg_speed

用户管理
------------

用户分组管理
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html

.. automethod:: Client.create_group
.. automethod:: Client.get_groups
.. automethod:: Client.get_group_by_id
.. automethod:: Client.update_group
.. automethod:: Client.move_user
.. automethod:: Client.move_users
.. automethod:: Client.delete_group

设置备注名
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/User_Management/Configuring_user_notes.html

.. automethod:: Client.remark_user

获取用户基本信息
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/User_Management/Get_users_basic_information_UnionID.html#UinonId

.. automethod:: Client.get_user_info
.. automethod:: Client.get_users_info

账户管理
------------
长链接转短链接接口和微信认证事件推送暂未添加，可自行实现。

生成带参数的二维码
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Account_Management/Generating_a_Parametric_QR_Code.html

.. automethod:: Client.create_qrcode
.. automethod:: Client.show_qrcode

获取用户列表
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/User_Management/Getting_a_User_List.html

.. automethod:: Client.get_followers

素材管理
------------

新增临时素材
``````````````````````````````

详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html

.. automethod:: Client.upload_media

获取临时素材
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_temporary_materials.html

.. automethod:: Client.download_media

新增永久素材
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Adding_Permanent_Assets.html

.. automethod:: Client.add_news
.. automethod:: Client.upload_news_picture
.. automethod:: Client.upload_permanent_media
.. automethod:: Client.upload_permanent_video

获取永久素材
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Getting_Permanent_Assets.html

.. automethod:: Client.download_permanent_media

删除永久素材
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Deleting_Permanent_Assets.html

.. automethod:: Client.delete_permanent_media

上传图文消息素材
``````````````````````````````

.. automethod:: Client.upload_news

修改永久图文素材
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Editing_Permanent_Rich_Media_Assets.html

.. automethod:: Client.update_news

获取素材总数
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_the_total_of_all_materials.html

.. automethod:: Client.get_media_count

获取素材列表
``````````````````````````````
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_materials_list.html


.. automethod:: Client.get_media_list

用户标签管理
------------
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/User_Management/User_Tag_Management.html

创建标签
``````````````````````````````
.. automethod:: Client.create_tag

获取公众号已创建的标签
``````````````````````````````
.. automethod:: Client.get_tags

编辑标签
``````````````````````````````
.. automethod:: Client.update_tag

删除标签
``````````````````````````````
.. automethod:: Client.delete_tag

获取标签下粉丝列表
``````````````````````````````
.. automethod:: Client.get_users_by_tag

批量为用户打标签
``````````````````````````````
.. automethod:: Client.tag_users

批量为用户取消标签
``````````````````````````````
.. automethod:: Client.untag_users

获取用户身上的标签列表
``````````````````````````````
.. automethod:: Client.get_tags_by_user

模板消息
------------
.. automethod:: Client.send_template_message


返回码都是什么意思？
--------------------------
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Global_Return_Code.html

48001 -- API Unauthorized
---------------------------

如果你遇到了这个错误，请检查你的微信公众号是否有调用该接口的权限。
详细请参考 `微信开放文档`__

.. __: https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Explanation_of_interface_privileges.html
