# 测试数据

| 目录 | 内容及用途 |
|---|---|
| `acvp/` | 固定版本 NIST ACVP 原始 JSON、来源说明和 SHA-256 清单 |
| `fixtures/` | ML-KEM-1024 的 145 条 RTL 输入、参考输出及用例身份 |
| `cpu_baseline/` | RV32IM-fast 历史 RTL 逐例周期，供向量打包与 RTL 统计使用 |
| `call_profile/` | 完整 K4 测试集的 FIPS 202 调用记录，供预期硬件计数核对使用 |

板上直接使用的向量与运行包共同保存在 `../board/release/kat_vectors.json`；109 笔 HLS 局部差分事务使用 `../hls/tb/` 中的向量。实板 CPU-only/加速性能取自 `../evidence/board/` 的原始记录。
