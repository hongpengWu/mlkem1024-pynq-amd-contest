# PYNQ-Z2 配对发布包

`release/` 保存 2026-10-23 实板验证使用的完整发布包，含同一个 `.bit/.hwh`、两组 RISC-V 固件、145 条向量、驱动、Notebook、构建信息和 SHA-256 manifest。

将整个 `release/` 上传到板上 Jupyter 工作区，打开 `mlkem1024.ipynb`，点击 **Kernel → Restart & Run All**。默认依次执行两组各三例预检、两组各 145 条、60 次重复验证及 6 项恢复检查；全部代码已经写入 Notebook。

每次固件切换执行完整 128 KiB RAM 写入、读回和哈希核对。结果逐阶段写入板上 `evidence/<时间戳>/`，Notebook 最后一节提供结果下载。完整使用步骤见[仓库说明](../README.md#路径-a直接在-jupyter-复现)，归档数据见[实板证据](../evidence/board/)。

新 HLS/RTL 构建产物通过 `build/deployment/` 或 `build/paired_release/` 发布，现有 `release/` 保留实测输入原始字节。
