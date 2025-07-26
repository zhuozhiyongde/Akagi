# Akagi

本项目是 [Akagi](https://github.com/shinkuan/Akagi) 的一个修改版，主要为了适配 [Majsoul Helper](https://github.com/zhuozhiyongde/MajsoulHelper) 项目的容器化部署。

原版 Akagi 是一个功能强大的雀魂 AI，提供了 TUI 界面。本版本进行了一些核心修改，使其能够作为后端服务运行。

为了 clone 本项目，你可能需要安装 [Git LFS](https://git-lfs.github.com/)。

## ✨ 核心修改

1.  **移除 TUI**：去除了原有的命令行终端用户界面。
2.  **集成数据服务器 (DataServer)**：增加了一个基于 WebSocket 的数据服务器，用于将 AI 的计算结果实时推送给前端。
3.  **增加 Vendor 依赖管理**：兼容与 MajsoulMax 共用环境。

## 📦 架构

在 Majsoul Helper 项目的 Docker 部署方案中，Akagi 扮演着核心的 AI 计算角色：

1.  **流量接收**：作为第二层 MITM 代理，从上游的 `MajsoulMax` 接收游戏流量（端口 `7880`）。
2.  **数据解析与 AI 计算**：拦截并解析游戏的核心数据，调用内置的 AI 模型进行计算，得出推荐操作。
3.  **结果推送**：将计算结果发送到内部的 `DataServer`。
4.  **前端通信**：`DataServer` 通过 WebSocket（端口 `8765`）将 AI 推荐结果实时推送给前端页面进行展示。

## 🚀 使用方式

本项目主要作为 `Majsoul Helper` 的一个组件，通过 `docker-compose` 统一启动和管理，亦可脱离 MajsoulMax，作为单一的 AI 计算后端使用。

```bash
pip install -r requirements.txt
python run_akagi.py
```

## 📜 许可证

本项目基于 [GNU General Public License v3.0](./LICENSE) 许可证开源。