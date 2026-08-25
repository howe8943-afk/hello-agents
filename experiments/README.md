# 日常实验

这里记录学习过程中的小实验、代码草稿和验证结果。

建议每个实验单独建立一个目录，例如：

```text
experiments/
  001-basic-agent/
    README.md
    main.py
  002-tool-calling/
    README.md
    main.py
```

每个实验的 README 可以记录：

- 实验目的
- 使用的模型或依赖
- 关键代码
- 运行命令
- 实验结果
- 遇到的问题与下一步

运行实验时，统一使用项目环境：

```powershell
uv run python experiments/<实验目录>/main.py
```
