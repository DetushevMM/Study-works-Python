# Косольный доменный чат-бот
# Что делает код:
# Каждую итерацию:
# ИИ случайно «становится» экспертом в новой области.
# История чата ограничивается последними 10 сообщениями.
# Случайным образом выбирается одна из двух LLM моделей.
# Ответ ИИ печатается по частям (stream).
# Выход возможен по команде exit.
# !!!Для работы кода необходимо установить библиотеку Ollama на локальный компьютер или сервер. 
# Перейдите на официальный сайт: https://ollama.com. 
# После установки откройте терминал и запустите:  
# ollama serve
# ollama run llama3:3b
# ollama run llama3:8b
# ollama run llama2:7b


# pip install langchain langchain_community langchain-core

import random
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Список возможных областей экспертизы
domains = ["math", "history", "coding", "medicine", "philosophy"]

# Список моделей
models = ["llama3.2:3b", "llama2:7b"]

# Создаем две модели
llm1 = ChatOllama(model=models[0], temperature=0.7)
llm2 = ChatOllama(model=models[1], temperature=0.7)

# Шаблон для общения с ИИ
messages = [
    ("system", "You are an expert in {domain}. Keep answers short."),
    MessagesPlaceholder("history")
]
prompt_template = ChatPromptTemplate(messages)

# Хранилище истории
history = []

print("Введите 'exit' для завершения чата.")

while True:
    print()
    user_input = input("You: ")

    # Проверка на выход
    if user_input.strip().lower() == "exit":
        print("Выход из чата.")
        break

    # Добавляем сообщение пользователя
    history.append(HumanMessage(content=user_input))

    # Обрезаем историю до последних 10 сообщений
    history = history[-10:]

    # Случайно выбираем область и модель
    current_domain = random.choice(domains)
    current_llm = random.choice([llm1, llm2])

    # Создаем финальный промпт
    prompt = prompt_template.invoke({"domain": current_domain, "history": history})

    # Потоковая генерация ответа
    print(f"Bot ({current_domain}): ", end="")
    ai_response = ""
    for chunk in current_llm.stream(prompt.to_messages()):
        print(chunk.content, end="")
        ai_response += chunk.content
    print()

    # Добавляем ответ ИИ в историю
    history.append(AIMessage(content=ai_response))

