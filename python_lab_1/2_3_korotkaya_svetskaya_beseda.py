print("Привет! Как твое настроение?")
answer = input()
if ("хорошее" in answer or "прекрасное" in answer or "хорошо" in answer or "прекрасно" in answer or
    "отличное" in answer or "отлично" in answer or "нормально" in answer or "нормальное" in answer) and\
    "не" not in answer and "?" not in answer:
    print("Отлично, у меня тоже всё хорошо :)")
elif ("плохое" in answer or "ужасное" in answer or "отвратительное" in answer or
    "грустное" in answer or "плохо" in answer or "ужасно" in answer or
    "отвратительно" in answer or "грустно" in answer) and "не" not in answer and
    "?" not in answer:
    print("Ничего, скоро всё наладится")
else:
    print("Извини, я не могу разобрать твой ответ")

_______________