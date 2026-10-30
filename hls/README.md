# Keccak/SHAKE HLS 核

本核实现 SHAKE128、SHAKE256、SHA3-256、SHA3-512，采用 25-lane 并行、单轮复用 24 轮的 Keccak-f[1600] 数据通路。32-bit 打包访存按 rate 块处理输入与输出，保持 FIPS 202 逐位结果。

| 接口 | 容量与语义 |
|---|---|
| input | 512 个 uint32，2048 B |
| output | 1024 个 uint32，4096 B/命令 |
| context | 26 个 uint64，含状态、模式和游标 |
| mode | 0 SHAKE128；1 SHAKE256；2 SHA3-256；3 SHA3-512 |
| command | 0 HASH；1 SQUEEZE；2 CLEAR |

HASH 完成初始化、吸收、填充与输出；SHAKE 通过 SQUEEZE 续取。SHA3 与 CLEAR 清除上下文。输入、输出与上下文使用独立缓冲区。

[根 README](../README.md)给出从 HLS 到 PS–PL overlay 的完整步骤；入口为 [flow.tcl](../flow.tcl)。独立测试包含 109 次事务，使用 Python hashlib 产生期望输出，覆盖边界长度、SHAKE 续取、交错上下文、错误调用与清除。测试细节见 [tb/README.md](tb/README.md)，既有报告见 [HLS 归档](../evidence/hls/)。

从仓库根目录检查固定测试输入：

```powershell
python hls/scripts/generate_vectors.py --check
```

HLS 运行产物写入 `build/hls/io1/<run_id>/`；`FLOW_HLS_RUN` 选择通过 C/RTL 协同仿真的运行，供 CPU 集成与 BD 构建使用。
