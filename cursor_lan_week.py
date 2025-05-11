# 定义四种语言的星期列表
days_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_it = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
days_es = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
days_fr = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print("English\t\tItaliano\tEspañol\t\tFrançais")
for en, it, es, fr in zip(days_en, days_it, days_es, days_fr):
    # 格式化输出是一种按照指定格式输出数据的方式，这里使用 f-string (格式化字符串)
    # 可以在字符串中使用 {} 插入变量，并指定对齐、宽度等格式要求
    # {en:<10} 表示左对齐，宽度为10个字符
    # \t 表示制表符，用于对齐不同语言的输出
    print(f"{en:<10}\t{it:<10}\t{es:<10}\t{fr}")