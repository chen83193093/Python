from tkinter import *
import tkinter.font as tkFont
import random
import sys
from time import sleep

class GuessNumberGenerator:
    def __init__(self):
        window = Tk()
        hi = window.title("猜数字游戏");


class QuestionGenerator:
    def __init__(self):
        window = Tk()
        hi = window.title("ARM期末考试")
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=15)
        window.option_add("*Font", default_font)

        self.width = 1200
        self.canvas = Canvas(window, bg="white", width=self.width, height=280)
        self.canvas.pack()
        myText = self.canvas.create_text(100, 50, text="猜数字区域")

        frame = Frame(window)
        frame.pack()
        btGenerator = Button(frame, text = "请猜数字", command = self.generatorQuestion)
        btGenerator.pack(side = LEFT)
        btGenerator2 = Button(frame, text = "答案", command = self.generatorAnswer)
        btGenerator2.pack(side = LEFT)
        # btGenerator3 = Button(frame, text="我要提示", command=self.generatorInfo)
        # btGenerator3.pack(side=LEFT)

        # self.isOK = False

        window.mainloop()

    def generatorQuestion(self, t = 0):
            # if self.isOK == True:
            global num
            num = random.randint(1, 40)
            self.canvas2.delete("text2")
            self.canvas.delete("pic")
            # while t == num:
            #     num = random.randint(1, 40)
            # t = num
            self.canvas.delete("text")
            self.canvas.create_text(300, 100, text = self.question(num), tags = "text", anchor = W, justify = LEFT)


            # self.canvas.select_from(txt, 2)
            # self.canvas.select_to(txt, 5)
            self.canvas.pack()


    def generatorAnswer(self):
            self.canvas2.delete("text2")
            self.canvas2.create_text(300, 180, text = self.answer(num), tags= "text2", justify=LEFT,anchor = W)
            self.canvas2.pack()

    def generatorInfo(self):
                self.canvas3.delete("text3")
                self.canvas3.create_text(500, 70, text=self.info(num), tags="text3", justify=LEFT, anchor=W)
                self.canvas3.pack()
            # text2 = Text(self.frame1, width = 200, height = 200, wrap = WORD, yscrollcommand = self.scrollbar.set)
            # text2.pack()
            # self.scrollbar.config(command = text2.yview)
            # self.canvas.delete("texts")
            # self.txt1['yscrollcommand'] = self.sl1.set

    def question(self, num):
            # self.isOK = True
                if num ==  1:
                    s =  '''
                    EPC的特点
                  '''
                elif num == 2:
                    s =  "国内物联网应用的典型案例"
                elif num == 3:
                    s = "物联网应用远景"
                elif num == 4:
                    s = "传感器概念"
                elif num == 5:
                    s = "信息安全通常分为哪4个层次"
                elif num == 6:
                    s = '''
                        技术架构上来看，物联网可分为哪3层？
                        最终实现：_____、_____、_____
                 '''
                elif num == 7:
                    s = '''
                    中国研究物联网的标准组织主要有________和________。
                 '''
                elif num == 8:
                    s = '''
                     中国物联网标准的制定工作还处于起步阶段，但发展迅速。
                     目前中国已有涉及______、______、______的众多标准正在制订中，
                     并且有相当一部分的标准项目已在相关国际标准组织立项。
                     中国研究物联网的标准组织主要有传感器网络标准工作组（WGSN）
                     和中国通讯标准化协会（CCSA）。
                '''
                elif num == 9:
                    s = '''
                     传感器按其结构原理不同可分为______、_______、_______
                '''
                elif num == 10:
                    s = '''
                               常用传感器有哪些？
                '''
                elif num == 11:
                    s = '''
                               传感接口有哪些？
                '''
                elif num == 12:
                    s = '''
                               传感器一般由______、______、______3部分组成。
                '''
                elif num == 13:
                    s = '''
                               RFID应用领域有________、________、________、
                               ________、________、________等。
                '''
                elif num == 14:
                    s = '''
                            简述读卡器的三个主要组成部分
                '''
                elif num == 15:
                    s = '''
                            读写器天线实现什么样的功能？
                '''
                elif num == 16:
                    s = '''
                           根据天线在系统中不同功能和作用，可以将RFID中天线分为
                           ________和________。
                  '''
                elif num == 17:
                    s = '''
                           简述对标签天线的四个要求
                 '''
                elif num == 18:
                    s = '''
                    与一般的通信总线相比，CAN总线的数据通信具有突出的
                    _____、_____和_____。
                 '''
                elif num == 19:
                    s = '''
                   CAN有两种不同的帧格式，不同之处为_____________。
                 '''
                elif num == 20:
                    s = '''
                   CAN有两种不同的帧格式，分别是？
                 '''
                elif num == 21:
                    s = '''
                    CAN报文有4种不同的帧类型，分别是：_______、_______、_______和________。
                               '''
                elif num == 22:
                    s = '''数据帧由7个不同的位场组成，分别是：_______、_______、_______、_______、_______、_______、_______。
                               '''
                elif num == 23:
                    s = '''
                   Cortex-M3处理器支持的数据类型有：_______、_______、_______。
                 '''
                elif num == 24:
                    s = '''
                   简述在Cortex-M3处理器中，哪4种情况会产生中止故障。
                 '''
                elif num == 25:
                    self.myImage = PhotoImage(file=r"E:\LED在传感板上的接线图.gif")
                    im = self.canvas.create_image(250, 0, anchor=NW, image=self.myImage, tags = "pic")  # 加载图片
                    s = '''
                   \t左图是LED在传感板上的接线图，请写出相应代码，并给出解释。
                 '''
                elif num == 26:
                    self.myImage = PhotoImage(file=r"E:\执行板上的蜂鸣器接线.gif")
                    im = self.canvas.create_image(250, 0, anchor=NW, image=self.myImage, tags = "pic")  # 加载图片
                    s = '''
                   \t左图是LED在传感板上的接线图，请写出相应代码，并给出解释。
                 '''
                elif num == 27:
                    self.myImage = PhotoImage(file=r"E:\烟雾传感器的接线.gif")
                    im = self.canvas.create_image(250, 0, anchor=NW, image=self.myImage, tags = "pic")  # 加载图片
                    s = '''
                     \t左图是LED在传感板上的接线图，请写出相应代码，并给出解释。
                                     '''
                elif num == 28:
                    self.myImage = PhotoImage(file=r"E:\电位器VR1的AD值采集接线.gif")
                    im = self.canvas.create_image(250, 0, anchor=NW, image=self.myImage, tags = "pic")  # 加载图片
                    s = '''
                      \t左图是LED在传感板上的接线图，请写出相应代码，并给出解释。
                                     '''
                elif num == 29:
                    s = '''
                   简述实时操作系统的基本特征。
                 '''
                elif num == 30:
                    s = '''
                   简述实时操作系统的关键技术指标。
                 '''
                elif num == 31:
                    s = '''
                   简述移植μC/OS-Ⅱ到处理器上必须满足的条件。
                 '''
                elif num == 32:
                    s = '''
                   分析启动码之前，需要了解C代码和汇编代码通过哪些步骤转化为可执行代码，
                   从而最终在硬件上运行。通常的流程分4步。
                   请简述这4步流程。
                 '''
                elif num == 33:
                    s = '''
                   IAR EWARM提供两种缺省的项目生产配置，即_______和________。
                 '''
                elif num == 34:
                    s = '''
                   IAR Embedded Workbench for ARM是IAR Systems公司
                   为ARM微处理器开发的一个集成开发环境（简称IAR EWARM）。
                   比较其他的ARM开发环境，IAR EWARM具有
                   ______、______、和______的特点。
                 '''
                elif num == 35:
                    s = '''
                    在计算机系统中，数据分为两类：_____和_____。
                 '''
                elif num == 36:
                    s = '''
                    在计算机系统中，数据分为两类：指令和地址。
                    ARM中指令的长度有____位ARM指令集和____位的Thumb指令集，
                    而地址是一个无符号的____位数值。
                 '''
                elif num == 37:
                    s = '''
                    Cortex-M3处理器支持两种工作模式——_______和_______。
                 '''
                elif num == 38:
                    s = '''
                    Cortex-M3处理器的两种工作状态是_______和________。
                 '''
                elif num == 39:
                    s = '''
                    简述RS-485总线的特点
                 '''
                elif num == 40:
                    s = '''
                    填空：
                     指令       操作                  作用
                     ADR     ______             产生一个地址
                      BX       Rm              ______________
                     CBZ      Rn,label           ______________
                     ____     Rn!{reglist}     从一片连续的地址空间中加载若干个字，
                                                    并选中相同数目的寄存器放进去
                     NOP     -{Rd,} Rn,Rm      ______________
                     ____     Reglist                 出栈         
                     ____     {Rd,}Rn,Rm          带符号除法
                     STM     Rn!,{reglist}        ______________
                 '''
                else:
                    s = ""
                return s

    def answer(self, num):
        if num == 1:
            s = '''
              （1）开放的结构体系 
              （2）独立的平台与高度的互动性 
              （3）灵活且可持续发展的体系
            '''
        elif num == 2:
            s = '''
               （1）广东虎门大桥组合式收费系统
               （2）烟台蔬菜大棚远程监控系统
               （3）中关村软件园智能楼宇系统
            '''
        elif num == 3:
            s = '''
              （1）物联网与智能家居
              （2）物联网与智能农业
              （3）物联网与智能物流
              （4）物联网与智能医疗
              （5）物联网与节能减排
            '''
        elif num == 4:
            s = '''
            是测量系统中直接作用于被测量（包括物理量、生物量、化学量等）的器件，通过它将
            被测量转换成容易处理、容易与标准量比较的物理量（如位移、频率、电流、电阻、
            电压等）。
            '''
        elif num == 5:
            s = '''
              （1）物理安全：即信息系统硬件方面，
               或者说是表现在信息系统电磁特性方面的安全问题。
              （2）运行安全：即信息系统的软件方面，
               或者说是表现在信息系统代码执行过程中的安全问题。
              （3）数据安全：即信息自身的安全问题。
              （4）内容安全：即信息利用方面的安全问题。
            '''
        elif num == 6:
            s = '''
              从技术架构上来看，物联网可分为3层：感知层、网络层和应用层。
              最终实现：全面感知、可靠传送、智能处理。
            '''
        elif num == 7:
            s = '''
                传感器网络标准工作组（WGSN）     
                中国通讯标准化协会（CCSA）
            '''
        elif num == 8:
            s = '''
            物联网总体架构
            无线传感网
            物联网应用层面
            '''
        elif num == 9:
            s = '''
            （1）结构型传感器
            （2）物性型传感器
            （3）智能型传感器
            '''
        elif num == 10:
            s = '''
               （1）电阻式传感器
               （2）电感式传感器
               （3）电容式传感器
               （4）电磁式传感器
               （5）压电式传感器
               （6）光电式传感器   
            '''
        elif num == 11:
            s = '''
                      （1）SPI接口  
                      （2）I^2C接口 
                      （3）串行接口
             '''
        elif num == 12:
            s = '''
                        敏感元件
                        转换元件
                        转换电路
            '''
        elif num == 13:
            s = '''
                        （1）车辆自动识别方面
                        （2）在高速公路收费及智能交通方面
                        （3）在货物的管理及监控方面
                        （4）在标签应用方面
                        （5）在生产线的自动化及过程控制方面
                        （6）在动物的跟踪及管理方面
            '''
        elif num == 14:
            s = '''
                 第一部分是发送和接收部分，用来与标签和分离的单个物品保持联系；
                 第二部分是对接收信息进行初始化处理；
                 第三部分是连接服务器，用来将信息传送到管理机构。
            '''
        elif num == 15:
            s = '''
                读写器天线发射电磁能量以激活标签，
                实现数据传输向标签发送指令，
                同时也要接受来自标签的信息。
        '''
        elif num == 16:
            s = '''
                 读写器天线
                 标签天线
        '''
        elif num == 17:
            s = '''
                （1）标签应答器的天线要将标签所储存的信息进行调制反射，
                 同时还要捕获读写器发射的电磁波，为标签应答器提供能量。
                （2）由于要使标签能够粘贴到被识别的物体上，就要求标签足够小，
                在大多数情况下需要标签天线的尺寸也足够小，
                在大多数情况下需要标签天线全方向或半球形覆盖物体。
                （3）由于标签天线的阻抗一般不足50欧，这就需要标签天线能够实现
                非50欧与芯片阻抗的共轭匹配，以提供最大功率给芯片。
                （4）在一般情况下，标签需要大规模使用，这就要求标签天线成本低，加工简单。
        '''
        elif num == 18:
            s = '''
                 可靠性、实时性和灵活性。
        '''
        elif num == 19:
            s = '''
                 识别符场的长度不同
        '''
        elif num == 20:
            s = '''
                 具有11位识别符的帧称为标准帧；而含有29位识别符的帧为扩展帧。
        '''
        elif num == 21:
            s = '''
                 （1）数据帧
                 （2）远程帧
                 （3）错误帧
                 （4）过载帧
        '''
        elif num == 22:
            s = '''
                 帧起始、仲裁场、控制场、数据场、CRC场、应答场、帧结尾。
        '''
        elif num == 23:
            s = '''
                （1）32位字类型；
                （2）16位半字类型；
                （3）8位字节类型。
         '''
        elif num == 24:
            s = '''
                （1）指令取址或向量表加载时的总线错误；
                （2）数据访问时的总线错误；
                （3）内部检测到的错误，如出现未定义的指令或使用BX指令来改变状态。
                      NVIC中的故障状态寄存器标识了故障的发生状态；
                （4）系统出现MPU故障。
         '''
        elif num == 25:
            s = '''
           void led_dis(void)
    {
      mdelay(500);
      gpio_set_pin_high(LED2_GPIO);     //关闭LED2
      gpio_set_pin_low(LED1_GPIO);      //点亮LED1
      mdelay(500);
      gpio_set_pin_high(LED1_GPIO);     //关闭LED1
      gpio_set_pin_low(LED2_GPIO);      //点亮LED2
    }
         '''
        elif num == 26:
            s = '''
           void BEER(void)
    {
      gpio_set_pin_high(PIN_BEER);
      mdelay(500);
      gpio_set_pin_LOW(PIN_BEER);
      mdelay(500);
    }
         '''
        elif num == 27:
            s = '''
             void Gas_test(unit8_t* gas_result)
                 {
                    unit32_t adc=0;
                    unit32_t adcs=0;
                    ADC_StartConversion(ADC);    //启动转换
                    adcs=0xfff & ADC_GetConvertedData(ADC,ADC_CHANNEL_7);                                      //利用第7通道获取AD转换值
                    adc=adcs * 3300 / 4095;    
                    //将AD采集的电压值转换到0~3300，对应0~3.3V（0~1里是多少V）
                    gas_result[0]=adc/1000;    //显示保留小数点后一位   （整数）
                    gas_result[1]=(adc%1000)/100;     （余数）
                }
                分辨率=3.3V/3300=0.001V
         '''
        elif num == 28:
            s = '''
           void ADC_test(unit8_t *adc_result)
            {
                unit32_t adc=0;
                unit32_t adcs=0;
                ADC_StartConversion(ADC);    //启动ADC采集
                adcs=0xfff & ADC_GetConvertedData(ADC,ADC_CHANNEL_9); //通道为AD9
                adc=adcs * 3300 / 4095;      //采集值转换为0~3.3V
                gas_result[0]=adc/1000;
                gas_result[1]=(adc%1000)/100;
            }
         '''
        elif num == 29:
            s = '''
             （1）实时性
             （2）抢占式调度
             （3）具有异步响应能力
             （4）内存锁定
             （5）具有优先级调度机制
             （6）同步/互斥机制
         '''
        elif num == 30:
            s = '''
            （1）任务调度算法
            （2）上下文切换时间
            （3）系统确定性
            （4）最小内存开销
            （5）最大中断禁止时间
         '''
        elif num == 31:
            s = '''
                 （1）处理器的C编译器能产生可重入代码。
                 （2）用C语言可打开和关闭中断。
                 （3）处理器支持中断并且能产生定时中断。
                 （4）处理器支持能够容纳一定量数据的硬件堆栈。
                 （5）处理器有将堆栈指针和其他CPU寄存器读出和存储到堆栈（或内存）的指令。
         '''
        elif num == 32:
            s = '''
                （1）用编译器把源代码编译成ELF（Executable and Linking Format）目标文件。
                （2）用链接器把目标文件链接成ELF格式的可执行映像文件。
                （3）用FROMELF工具把可执行的映像文件转化为二进制映像文件。
                （4）烧写二进制映像文件到目标板。
                 以上步骤是由IAR软件完成的。
         '''
        elif num == 33:
            s = '''
                Debug
                Release
            '''
        elif num == 34:
            s = '''
               入门容易、使用方便和代码紧凑
            '''
        elif num == 35:
            s = '''
               指令
               地址
            '''
        elif num == 36:
            s = '''
               32    16     32
            '''
        elif num == 37:
            s = '''
               线程模式
               处理模式
            '''
        elif num == 38:
            s = '''
               Thumb状态
               调试状态
            '''
        elif num == 39:
            s = '''
               （1）RS-485总线构成的网络只能以串行布线，不能构成星形等任意分支。
                串行布线给小区实际布线设计及施工带来很大困难，不遵循串行布线规则
                又将大大降低通信的稳定性。
               （2）RS-485总线自身的电气性能决定了其在实际工程应用中稳定性较差，
                在多结点、长距离场合需对网络进行阻抗匹配等调试，添加了工程复杂性。
               （3）RS-485总线通常不带隔离，网络上某一结点出现故障会导致系统整体
                或局部瘫痪，而且又难以判断其故障位置。
               （4）RS-485总线采用主机轮询方式，会造成一些弊端。
            '''
        elif num == 40:
            s = '''
                Rd,label 
                无条件跳转到由寄存器给出的地址
                比较结果为0则分支
                LDM
                空操作
                POP
                SDIV
                多个数据的存储
            '''

        return s

    # def insertContent(self, num):
    #         if num == 1:
    #             # self.text.append("你好")
    #             # self.text.pack()
    #             s = "你好"
    #         else:
    #             s = ""
    #         return s

    # def insertContent(self):
    #     # if num == 1:
    #         self.text.insert(END, "嗯哼")
    #         self.text.pack()
            # return {
            #     "1" : "EPC的特点",
            #     "2": "对标签天线的要求",
            # }[num]
                # def slow(self):
                #     num = 1
                #     t = self.question(num)
                #     for i in t:
                #         self.canvas.create_text(100, 100 + 20 * i, text=i, tags="text")
                #         sleep(0.5)

    # def info(self, num):
    #     if num == 1:
    #         s = "淘宝"
    #     else:
    #         s = "没有"
    #     return s
QuestionGenerator()
