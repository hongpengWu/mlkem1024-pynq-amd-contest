# 实测与实现证据

| 目录 | 内容 |
|---|---|
| [board](board/summary.md) | 2026-10-23 同板双固件结果：两组各 145 条，60 次代表例重复，6 项恢复；原始 ZIP、JSON 与独立核验记录 |
| [implementation](implementation/result.json) | 发布 overlay 的 100 MHz 布局布线签核及资源报告；setup +0.302 ns、hold +0.026 ns |
| [hls](hls/) | base02、opt02、opt01_impl 的 C 仿真、RTL 协同仿真、综合及独立 IP 实现报告 |

原始归档保留运行时的路径、时间戳和哈希。`board/upload_snapshot/` 保存测量绑定的上传包，`board/release/` 位于仓库根的部署目录并保存相同制品。当前构建路径与步骤由根 README 定义。

离线重算并核验已有板上数据：

```powershell
python scripts/pynq_overlay.py collect-paired evidence/board --source board/release --check-existing
```

该命令读取已有文件，核验每条官方输出、返回码、固件及 RAM 哈希、硬件计数，并重算性能比值。
