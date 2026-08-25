# Hello-Agents

这是基于 [Hello-Agents](https://datawhalechina.github.io/hello-agents/#/) 的学习与实践项目，使用 `uv` 管理 Python 环境和依赖。

## 环境要求

- Python 3.12+
- uv 0.5+

## 开始使用

```powershell
uv sync
uv run hello-agent
```

运行测试：

```powershell
uv run pytest
```

## 项目结构

```text
src/hello_agent/   # 可复用代码
tests/             # 自动化测试
```

后续学习章节可以按主题在 `src/hello_agent/` 下拆分模块，并为每个模块补充 `tests/` 测试。

## GitHub

本地 Git 仓库已经初始化。创建 GitHub 空仓库后执行：

```powershell
git remote add origin https://github.com/<你的用户名>/hello-agent.git
git add .
git commit -m "chore: initialize uv project"
git branch -M main
git push -u origin main
```
