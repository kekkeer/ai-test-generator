import os
from openai import OpenAI
from rich.console import Console

console = Console()

def generate_test_cases(requirement):
  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
  )

  with console.status("正在生成测试用例...", spinner="dots"):
    response = client.chat.completions.create(
      model="deepseek-chat",
      messages=[
        {"role": "system", "content": "你是一个软件测试工程师，请根据需求生成3条测试用例，用数字编号列出。"},
        {"role": "user", "content": requirement}
      ]
    )

  return response.choices[0].message.content


if __name__ == "__main__":
  req = input("请输入需求描述：")
  print("\n生成的测试用例：\n")
  print(generate_test_cases(req))
