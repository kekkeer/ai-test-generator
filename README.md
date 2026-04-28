# AI Test Generator

基于 LLM 的测试用例辅助生成工具，接入 DeepSeek API，通过结构化 Prompt 将需求描述转化为测试用例。

## 项目背景

日常开发中，测试用例编写存在重复性高、覆盖率难以保证的问题。本项目尝试用 LLM 辅助这一流程，将需求文本输入后自动输出测试用例，减少人工编写成本。

## 技术栈

- Python 3
- OpenAI SDK
- Rich（命令行交互）

## 本地运行

```bash
pip install openai rich
set OPENAI_API_KEY=your_key
python ai_test_gen.py
```

## 设计思路

- 直接调用 DeepSeek Chat 模型，通过 System Prompt 约束输出格式
- 当前为单轮生成，后续可扩展为多轮对话（补充边界条件、异常场景等）
- 支持通过替换 base_url 切换不同模型供应商

## 待改进

- 目前仅支持单文件、单轮生成，未接入测试框架
- 缺少输出结构化解析（JSON 格式）
- 未对 API 返回做校验和重试
