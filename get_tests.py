#Python3
puls = 0
print("Список доступного глобального пространства имён:", dir())
send_one = "Всё что вы введете будет проанализировано и добавлено в контекст безопасного тестирования"
while True:
  puls += 1
  inp = input(f"{send_one}\n|{puls}>>")
  # АНАЛИЗ ВВОДА АРХИТЕКТОРА по тестированию
  if inp:
    inp = "Архитектор промолчал, а это значит - молчание знак согласия."
    print(inp)
  elif inp.strip().lower() in ["exit","quit","выход", "стоп"]
    break
  else:
    print("Я прочитал, что Архитектор сказал:", inp)
  # ТЕСТ на основе результатов после согласования
  try:
    result = eval(inp, globals, locals)
  except BaseException as be:
    result = f"ОШИБКА тестирования: {be}"  # +f", при EVAL({inp})! Рекомендуется: `__import__(`"
