# coding:utf-8
#!/usr/bin/env python3

import pygame

# 白底黑字
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class information:
    def __int__(self):
        self.steer = ""
        self.accelerate = ""
        self.decelerate = ""
        self.left_lighting = ""
        self.right_lighting = ""
        self.trumpet = ""
        self.headlight = ""
        self.P = ""
        self.R = ""
        self.D = ""
        self.N = ""
        self.increase_speedlimit = ""
        self.decrease_speedlimit = ""
        self.list = []
    def update(self):
        self.list = [self.steer,self.accelerate,self.decelerate,self.left_lighting,self.right_lighting,self.trumpet,self.headlight,self.P,self.R,self.D,self.N,self.increase_speedlimit,self.decrease_speedlimit]
    def date(self):
        return self.list

moza_information = information()

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def defprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

class joystick_steer:
    def __init__(self,textPrint):
        self.joystick = pygame.joystick.Joystick(1)
        self.textPrint = textPrint
    def joystick_init(self):
        self.joystick.init()  # 初始化 joystick 模块

        self.textPrint.defprint(screen, "Joystick steer")
        self.textPrint.indent()  # 初始化 joystick 模块
        name = self.joystick.get_name()  # 获得 Joystick 系统名称
        self.textPrint.defprint(screen, "Joystick name: {}".format(name))

    def get_date(self):
        axes = self.joystick.get_numaxes()  # 获得 Joystick 操纵轴的数量
        self.textPrint.defprint(screen, "Number of axes: {}".format(axes))
        self.textPrint.indent()
        #方向盘数据
        axis = self.joystick.get_axis(0)  # 获得操纵轴的当前坐标
        self.textPrint.defprint(screen, "Axis steer value: {:>6.3f}".format(axis))
            #:>6.3f ：总长度为6位,精确到小数点后三位的浮点类型
        self.textPrint.unindent()  # 不缩进
        axis = float(axis)
        axis = round(axis,3)
        moza_information.steer = axis
        buttons = self.joystick.get_numbuttons()  # 获得 Joystick 上追踪球的数量
        self.textPrint.defprint(screen, "Number of buttons: {}".format(buttons))

        #速度上限提高
        button = self.joystick.get_button(13)  # 获得当前按钮的状态。
        moza_information.increase_speedlimit = button
        self.textPrint.defprint(screen, " increase_speedlimit value: {}".format( button))

        #速度上限降低
        button = self.joystick.get_button(12)  # 获得当前按钮的状态。
        moza_information.decrease_speedlimit = button
        self.textPrint.defprint(screen, "decrease_speedlimit value: {}".format( button))

        #左转
        button = self.joystick.get_button(18)  # 获得当前按钮的状态。
        moza_information.left_lighting = button
        self.textPrint.defprint(screen, "left_lighting value: {}".format( button))

        #右转
        button = self.joystick.get_button(31)  # 获得当前按钮的状态。
        moza_information.right_lighting = button
        self.textPrint.defprint(screen, "right_lighting value: {}".format(button))

        #喇叭
        button = self.joystick.get_button(20)  # 获得当前按钮的状态。
        moza_information.trumpet = button
        self.textPrint.defprint(screen, "trumpet value: {}".format(button))

        #示廓灯
        button = self.joystick.get_button(33)  # 获得当前按钮的状态。
        moza_information.headlight = button
        self.textPrint.defprint(screen, "headlight value: {}".format(button))

        #P档
        button = self.joystick.get_button(21)  # 获得当前按钮的状态。
        moza_information.P = button
        self.textPrint.defprint(screen, "P value: {}".format(button))

        #R档
        button = self.joystick.get_button(22)  # 获得当前按钮的状态。
        moza_information.R = button
        self.textPrint.defprint(screen, "R value: {}".format(button))

        #D档
        button = self.joystick.get_button(34)  # 获得当前按钮的状态。
        moza_information.D = button
        self.textPrint.defprint(screen, "D value: {}".format(button))

        #N档
        button = self.joystick.get_button(35)  # 获得当前按钮的状态。
        moza_information.N = button
        self.textPrint.defprint(screen, "N value: {}".format(button))
        self.textPrint.unindent()


class joystick_pedal:
    def __init__(self,textPrint):
        self.joystick = pygame.joystick.Joystick(0)
        self.textPrint = textPrint

    def joystick_init(self):
        self.joystick.init()  # 初始化 joystick 模块

        self.textPrint.defprint(screen, "Joystick pedal")
        self.textPrint.indent()  # 初始化 joystick 模块

        name = self.joystick.get_name()  # 获得 Joystick 系统名称
        self.textPrint.defprint(screen, "Joystick name: {}".format(name))

    def get_date(self):
        axes = self.joystick.get_numaxes()  # 获得 Joystick 操纵轴的数量
        self.textPrint.defprint(screen, "Number of axes: {}".format(axes))
        self.textPrint.indent()

        #油门
        axis = self.joystick.get_axis(0)  # 获得操纵轴的当前坐标
        axis = float(axis)
        axis = round(axis, 3)
        moza_information.accelerate = axis
        self.textPrint.defprint(screen, "accelerate value: {:>6.3f}".format(axis))

        #刹车
        axis = self.joystick.get_axis(1)  # 获得操纵轴的当前坐标
        axis = float(axis)
        axis = round(axis, 3)
        moza_information.decelerate = axis
        self.textPrint.defprint(screen, "decelerate value: {:>6.3f}".format(axis))
        self.textPrint.unindent()




pygame.init()


size = [500, 500]
screen = pygame.display.set_mode(size)  # 屏幕、显示、样式

pygame.display.set_caption("joy test")  # 标题

done = False

clock = pygame.time.Clock()

pygame.joystick.init()


textPrint = TextPrint()

joystick_0 = joystick_steer(textPrint)
joystick_0.joystick_init()
joystick_1 = joystick_pedal(textPrint)
joystick_1.joystick_init()

# -------- Main Program Loop 主循环程序-----------
while done == False:

    for event in pygame.event.get():  # User did something用户做了什么
        if event.type == pygame.QUIT:  # If user clicked close如果用户点击关闭
            done = True  # Flag that we are done so we exit this loop


        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        # 可能的操纵杆动作:             轴              球           按钮                      帽子
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")  # 操纵杆按钮按下
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")  # 操纵杆按钮解除


    screen.fill(WHITE)
    textPrint.reset()


    joystick_count = pygame.joystick.get_count()  # 数量

    textPrint.defprint(screen, "Number of joysticks: {}".format(joystick_count))  # 格式
    textPrint.indent()  # 缩进

    joystick_0.get_date()
    joystick_1.get_date()
    moza_information.update()
    DATE = moza_information.date()
    print(DATE)
    pygame.display.flip()


    clock.tick(20)


pygame.quit()  # 卸载 joystick 模块



