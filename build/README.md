# 构建目录

本目录保存本机生成的 HLS/Vivado 工程、固件、日志、报告和新部署包。入口为仓库根目录的 `flow.tcl` 与 `bd_axi.tcl`，具体阶段由文件顶部的 0/1 开关控制。

| 输出 | 内容 |
|---|---|
| `hls/io1/<run_id>/` | HLS 输入快照、报告和生成 RTL |
| `ps/`、`ps_cpu_only/` | PS mailbox 加速/软件固件 |
| `pynq/<run_id>/` | AXI 仿真、Block Design、Vivado 工程、bit/hwh |
| `results/` | 新运行的验证与实现报告 |
| `deployment/` | 新构建的加速系统板上运行包 |
| `paired_release/` | 新构建的双固件配对测量包 |

完整复现命令见[仓库说明](../README.md#路径-b从-hls-源码构建)。已实测发布包位于 `../board/release/`，每轮构建使用独立运行目录保存证据。
