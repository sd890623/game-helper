# 导入模块
import multiprocessing
import time
import psutil

# 定义a_process的目标函数
def a_func():
    print("a_process开始运行")
    # 检查事件的状态，如果事件被设置，则继续执行，否则暂停等待
    while(True):
        print("继续运行")
        time.sleep(1)

# 定义b_process的目标函数
def b_func(event):
    print("b_process开始运行")
    # 模拟一些操作
    time.sleep(3)
    print("b_process运行完毕")
    # 设置事件，让a_process继续执行
    event.set()

if __name__ == '__main__':

  # 创建一个事件对象
#   event = multiprocessing.Event()

  # 创建两个进程对象，并指定目标函数和参数
  #   b_process = multiprocessing.Process(target=b_func, args=(event,))

  try:
    a_process = multiprocessing.Process(target=a_func)
    # 启动两个进程
    a_process.start()
    # time.sleep(60)

    # b_process.start()
  except Exception as e:
      print(e)


  proc = psutil.Process(a_process.pid)  #传入任意子进程的pid
  # time.sleep(5)

  proc.suspend()   #暂停子进程
  print('子进程暂停运行')
  time.sleep(5)
  proc.resume()  
  print('子进程继续运行')
  proc.wait()




