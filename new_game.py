# =============================================================================
# 项目名称: 石头剪刀布游戏
# 作者: Mr.Lv Jing
# 创建日期: 2023-10-25

# 描述: 一个简单的石头剪刀布游戏，使用Tkinter构建GUI界面
# 联系方式: 1790980968@qq.com
# =============================================================================



# 导入Tkinter模块，这是Python的标准GUI（图形用户界面）软件包
# Tkinter是Python的内置库，无需额外安装，可用于创建桌面应用程序界面[1,5](@ref)
# 使用"as tk"为模块设置别名，方便后续代码中引用[1,4](@ref)
import tkinter as tk
import random  # 导入random模块用于生成电脑的随机选择

# 创建Tkinter应用程序的主窗口（根窗口）
# Tk()是Tkinter的核心类构造函数，调用它会初始化一个GUI应用程序的主窗口[1,5](@ref)
# 这个窗口是其他所有GUI组件的容器，通常称为"根窗口"或"主窗口"[1,4](@ref)
root = tk.Tk()

# 设置窗口的几何属性（大小和位置）
# geometry()方法用于设置窗口的尺寸和显示位置[1,5](@ref)
# 参数格式为"宽度x高度±X偏移±Y偏移"
# - "400x150"：设置窗口宽度为400像素，高度为150像素
# - "+800+400"：设置窗口距离屏幕左边界800像素，距离屏幕上边界400像素
# 如果只设置大小不设置位置，窗口将出现在默认位置（通常是屏幕中心）[1,5](@ref)
root.geometry("400x250+800+400")

# 设置窗口标题栏中显示的文本
# title()方法接受一个字符串参数，该文本将显示在窗口的标题栏中[1,5](@ref)
# 如果不设置标题，默认会显示"tk"[1](@ref)
root.title("石头剪刀布游戏")

# 创建一个标签(Label)组件，用于在窗口中显示静态文本或图像
# 参数说明：
# - root: 指定此标签的父容器为主窗口root
# - text="一起来玩吧!": 设置标签显示的文本内容
# - bg="#102030": 设置背景颜色，使用十六进制RGB颜色代码（深蓝色）
# - fg="#ffffff": 设置前景色（即文字颜色），这里为白色
# - font=('Microsoft YaHei', 20, 'bold italic'): 设置文本的字体样式[2](@ref)
#   * 'Microsoft YaHei': 字体家族（微软雅黑）
#   * 20: 字体大小（20磅）
#   * 'bold italic': 字体样式（粗体和斜体）
text = tk.Label(root, text="一起来玩吧!", bg="#102030", fg="#ffffff",
                font=('Microsoft YaHei', 20, 'bold italic'))

# 使用pack布局管理器将标签放置到主窗口中
# pack()是Tkinter三种布局管理器之一（另外两种是grid和place）[1,5](@ref)
# 它按照添加顺序自动排列组件，默认从上到下垂直排列
# padx=20, pady=20: 设置组件在水平和垂直方向上的外边距为20像素[1](@ref)
text.pack(padx=20, pady=20)

# 创建第二个标签组件，显示规则提示文字
# 这个标签使用较小的字体（10磅）显示辅助信息
text = tk.Label(root, text="<规则> 石头胜剪刀，剪刀胜布，布胜石头", font=('Microsoft YaHei', 10))
text.pack()


# 定义游戏逻辑函数
def determine_winner(user_choice, computer_choice):
    """判断游戏结果"""
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == "石头" and computer_choice == "剪刀") or \
            (user_choice == "剪刀" and computer_choice == "布") or \
            (user_choice == "布" and computer_choice == "石头"):
        return "你赢了！"
    else:
        return "你输了！"


def show_result_window(user_choice, computer_choice, result):
    """显示游戏结果窗口"""
    # 创建结果窗口
    result_window = tk.Toplevel(root)
    result_window.geometry("300x250+850+450")
    result_window.title("游戏结果")
    result_window.configure(bg="#f0f0f0")

    # 设置窗口无边框（可选）
    #result_window.overrideredirect(True)

    # 显示选择结果
    tk.Label(result_window, text=f"你的选择: {user_choice}",
             font=('Microsoft YaHei', 14, 'bold'), bg="#f0f0f0").pack(pady=10)

    tk.Label(result_window, text=f"我的选择: {computer_choice}",
             font=('Microsoft YaHei', 14, 'bold'), bg="#f0f0f0").pack(pady=10)

    # 根据结果设置不同颜色
    result_color = "green" if "赢" in result else ("red" if "输" in result else "blue")
    tk.Label(result_window, text=result,
             font=('Microsoft YaHei', 16, 'bold'),
             fg=result_color,
             bg="#f0f0f0").pack(pady=15)

    # 创建按钮框架
    button_frame = tk.Frame(result_window, bg="#f0f0f0")
    button_frame.pack(pady=10)

    # 再来一次按钮
    tk.Button(button_frame, text="再来一次", font=('KaiTi', 12),
              command=result_window.destroy, width=10).pack(side="left", padx=10)

    # 退出游戏按钮
    tk.Button(button_frame, text="退出游戏", font=('KaiTi', 12),
              command=root.quit, width=10).pack(side="right", padx=10)


# 定义"石头"按钮的点击事件处理函数
def on_shitou_click():
    # 电脑随机选择
    computer_choice = random.choice(["石头", "剪刀", "布"])
    # 判断结果
    result = determine_winner("石头", computer_choice)
    # 显示结果窗口
    show_result_window("石头", computer_choice, result)


def on_jiandao_click():
    # 电脑随机选择
    computer_choice = random.choice(["石头", "剪刀", "布"])
    # 判断结果
    result = determine_winner("剪刀", computer_choice)
    # 显示结果窗口
    show_result_window("剪刀", computer_choice, result)


def on_bu_click():
    # 电脑随机选择
    computer_choice = random.choice(["石头", "剪刀", "布"])
    # 判断结果
    result = determine_winner("布", computer_choice)
    # 显示结果窗口
    show_result_window("布", computer_choice, result)


# 创建三个按钮组件，分别代表"石头"、"剪刀"和"布"
# Button参数说明：
# - root: 指定按钮的父容器为主窗口root
# - text: 按钮上显示的文本
# - font=('KaiTi', 13): 设置按钮文字的字体和大小（楷体，13磅）[2](@ref)
# - command: 按钮点击时触发的回调函数（只有"石头"按钮当前绑定了函数）[1](@ref)
button_jiandao = tk.Button(root, text="剪刀", font=('KaiTi', 13), command=on_jiandao_click)
button_shitou = tk.Button(root, text="石头", font=('KaiTi', 13), command=on_shitou_click)
button_bu = tk.Button(root, text="布", font=('KaiTi', 13), command=on_bu_click)

# 使用place布局管理器精确定位三个按钮的位置
# place参数说明：
# - relx: 相对于父容器宽度的水平位置（0.0-1.0）
# - rely: 相对于父容器高度的垂直位置（0.0-1.0）
# - width, height: 设置按钮的宽度和高度（像素）
# - anchor="center": 以组件中心为参考点进行定位[1,5](@ref)
button_jiandao.place(relx=0.1, rely=0.5, width=50, height=25, anchor="center")  # 左侧：relx=0.1 (10%位置)
button_shitou.place(relx=0.5, rely=0.5, width=50, height=25, anchor="center")  # 中间：relx=0.5 (50%位置)
button_bu.place(relx=0.9, rely=0.5, width=50, height=25, anchor="center")  # 右侧：relx=0.9 (90%位置)

# 创建一个"关闭"按钮组件
# command=root.quit: 设置按钮点击时触发root.quit方法，用于退出应用程序[1,5](@ref)
button = tk.Button(root, text="关闭", command=root.quit)

# 使用pack布局管理器将关闭按钮放置到主窗口底部
# side="bottom"参数指定按钮停靠在父容器的底部[1,5](@ref)
button.pack(side="bottom", pady=10)


def show_about():
    about_window = tk.Toplevel(root)
    about_window.geometry("300x200+850+450")
    about_window.title("关于")
    tk.Label(about_window, text="石头剪刀布游戏", font=("Microsoft YaHei", 16, "bold")).pack(pady=10)
    tk.Label(about_window, text="版本: 1.0.0").pack()
    tk.Label(about_window, text="作者: Mr.Lv Jing").pack()
    tk.Label(about_window, text="邮箱: 1790980968@qq.com").pack(pady=10)
    tk.Button(about_window, text="关闭", command=about_window.destroy).pack(pady=5)

# 在菜单栏添加"关于"选项
menu = tk.Menu(root)
root.config(menu=menu)
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="帮助", menu=help_menu)
help_menu.add_command(label="关于", command=show_about)



# 在主窗口底部添加版权信息
#status_bar = tk.Label(root, text="© 2023 你的名字 | 石头剪刀布游戏 v1.0.0",
#                    bd=1, relief=tk.SUNKEN, anchor=tk.W)
#status_bar.pack(side=tk.BOTTOM, fill=tk.X)


# 启动Tkinter的主事件循环，使窗口保持显示状态
# mainloop()方法会进入一个无限循环，监听用户的操作（如点击、按键等）[1,5](@ref)
# 程序会一直阻塞在这里，直到主窗口被关闭（如点击关闭按钮或调用root.quit()）
# 这是Tkinter应用程序的必要部分，没有它窗口会一闪而过[1](@ref)
root.mainloop()
