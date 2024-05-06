# quark_auto_sign
夸克网盘自动签到
本项目基于https://github.com/mushichou/quark_auto_sign

注意，如果只需要自动签到不需要发送签到成功的通知消息，只需要cookie即可,通知目前支持
    - tg机器人
    - Server酱

1. fork本项目

2. 在设置里面设置环境变量（Setting -> Secrets and variables -> Actions）：
    - Variables（必选）:
        - COOKIE；
    - Secrets（可选）:
        - CHAT_ID （tg机器人的chat_id）；
        - TOKEN（tg机器人的token）；
        - SEND_KEY（Server酱的send key）；

3. 设置完成后可以点击 Actions -> quark_auto_sign_in -> run workflow


COOKIE获取方法：[Alist获取夸克网盘cookie](https://alist.nn.ci/zh/guide/drivers/quark.html)

