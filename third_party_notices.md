# 第三方来源与许可

| 组件 | 来源与许可 |
|---|---|
| [PicoRV32](rtl/picorv32.v) | YosysHQ/PicoRV32，文件内保留 Claire Xenia Wolf 的版权与 ISC 许可条款 |
| [mlkem-native](third_party/mlkem-native/) | pq-code-package/mlkem-native，提交 `b3ba7b32773e657dd37f6f87bce82528459ad8a4`；Apache-2.0 OR ISC OR MIT，完整条款见该目录 LICENSE |
| [公开测试向量](data/acvp/) | NIST ACVP-Server，提交 `975de31eb83d87039ec88934fdc47d8c312b892d`；固定来源与 SHA-256 清单随数据保存 |
| AMD 工具 IP 和 FPGA 原语 | Vivado/Vitis HLS 2024.2 安装环境提供，构建流程调用使用者的本地工具 |

`third_party/mlkem-native/SOURCE_MANIFEST.json` 保存上游路径和逐文件哈希，算法库保持原始字节。项目集成代码位于 `firmware/`、`rtl/` 和 `hls/`。第三方文件沿用各自许可；本项目自有代码的授权以作者授权为准。
