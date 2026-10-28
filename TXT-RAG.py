import os
import jieba #切割工具调用
import requests#发送llama.cpp端口
import time
import sys
#注意，默认配置千问ai，llama.cpp为部署框架。可根据更改。
jishu = 0
if os.path.exists('ai.jy/jy.txt'):
    pass
else:
    print("正在建立海马体")
    os.makedirs('ai.jy', exist_ok=True)
    with open('ai.jy/jy.txt', 'w', encoding="utf-8") as wu:
        pass
    print('TXT海马体建立成功！3秒后请重启......')
    time.sleep(3)
    sys.exit()
lishi = []
while True:#循环
    yonghu = input("请输入问题：")  # 盒子
    if yonghu == 'exit' or yonghu == '退出':
        print('结束进程中')
        time.sleep(2)
        break
    guanjianci = [w for w in jieba.cut(yonghu) if len(w) >= 2]  # 盒子
    memory_text = ""  # 盒子
    if os.path.exists("ai.jy"):
        print("正在查找文件")
        for liebiao in os.listdir('ai.jy'):  # 查找文件
            if liebiao.endswith(".txt"):
                with open(f"ai.jy/{liebiao}", "r", encoding="utf-8") as f:  # 只读取 #f是盒子
                    neirong = f.read()
                for ci in guanjianci:  # 套盒子
                    if ci in neirong:  # 套盒子
                        print(f'l2系统在{liebiao}里找到了{ci}！')
                        memory_text += neirong + "\n"
                        break  # 结束
    jieguo = (#提示词工程，要参照对应模型的提示词模板
        f'<|im_start|>system\n'
        f'你是一个本地的ai助手，必须结合记忆回答问题。禁止编造身份，不要输出思考过程。如果为记忆空或者没有信息，就忽略然后正常回答\n'
        f'<|im_end|>\n'
        f'<|im_start|>user\n'
        f'【搜索到的记忆】：{memory_text}\n'
        f'【用户回答】：{yonghu}\n'
        f'<|im_end|>\n'
        f'<|im_start|>assistant\n')
    payload = {'prompt': jieguo,
               'n_predict': 1024,
               'temperature':0.7,
               'stop':['<|im_end|>']}
    url = 'http://127.0.0.1:8080/completion'

    try:
        print('\n正在呼叫ai，请稍等...')
        responses = requests.post(url, json=payload)
        reply = responses.json()['content']
        print(f'\n回答{reply}')
        jishu += 1
        lishi.append(f'用户：{yonghu}\nai:{reply}')
    except Exception as e:
        print(f'\n连接失败：{e}')
    if jishu % 3 == 0:
        print('正在进行记忆储存，请勿操作')
        try:
            lishi_text = '\n'.join(lishi[-3:])
            chongzhi1 = (#记忆提示词工程，要参照对应模型的提示词模板。
                f'<|im_start|>system\n'
                f'你是一个记忆提炼助手。请提取用户对话中透露的个人信息、设定和关键事实。如果没有具体事实，直接输出“无”。绝对不要输出任何解释。\n'
                f'<|im_end|>\n'
                f'<|im_start|>user\n'
                f'以下是刚才的对话记录{lishi_text}\n'
                f'<|im_end|>\n'
                f'<|im_start|>assistant\n'
            )
            chongzhi = {
                'prompt': chongzhi1,
                'temperature':0.3,
                'stop':['<|im_end|>']
            }
            chzh = requests.post(url, json=chongzhi)
            cz = chzh.json()['content']
            if '</think>' in cz:
                cz = cz.split('</think>')[-1]
            cz = cz.strip()
            if cz in ['无', '', '.', '。'] or len(cz) < 2:#无记忆忽略检测
                print('模型认为:没有记忆的必要。')
            else:
                os.makedirs('ai.jy', exist_ok=True)#记忆
                with open('ai.jy/jy.txt', 'a', encoding="utf-8") as jy:
                    jy.write(cz + '\n')
                print('让我记一下')
            lishi.clear()

        except Exception as e:
            print(f'失败:{e}\n排查原因')
