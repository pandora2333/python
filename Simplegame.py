import easygui as g
import sys
class Simplegame:
    def run(self):
        while 1:
            g.msgbox("(｡･∀･)ﾉﾞ嗨，欢迎进入第一个界面小游戏")
            msg="请问在这里找到什么？"
            title="小游戏互动"
            choices=["谈恋爱","编程","找朋友","玩游戏"]
            choice=g.choicebox(msg,title,choices)
            g.msgbox("你的选择是："+str(choice),"结果")
            msg="你希望重新开始小游戏吗？"
            title="请选择"
            if g.ccbox(msg,title):
                pass
            else:
                sys.exit(0)
s=Simplegame()
s.run()
