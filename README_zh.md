
[English](README.md) | [简体中文](README_zh.md)

PC：推荐python3.8
    print("用法:")
    print("  python3 controller.py ENTER_SYNC")
    print("  python3 controller.py dance_x|dance_y|dance_a|dance_b")
    print("  python3 controller.py EXIT_SYNC")
    print("  python3 controller.py mode_stand_by")

机器人端
把opt目录开放权限
dance_agent复制到./opt目录下
添加系统启动项
WiFi设为默认连接
重启可以测试一下wifi是否连接，dance_agent有没有随系统启动

开始使用
确认PC和机器人在同一局域网下
机器人启动后断开物理手柄（关机即可）
PC端按照步骤创建虚拟手柄——操作——删除虚拟手柄——开机物理手柄（依次为完整的操作循环）
