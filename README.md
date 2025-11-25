# SHICTHRS VT Checker

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

一个用于检查Windows系统虚拟化技术(VT)状态的Python库。

## 功能特性

- 检查系统虚拟化固件状态
- 检查数据执行保护(DEP)状态
- 获取系统依赖信息
- 检查二级地址转换扩展(SLAT)状态

## 安装

### 使用pip安装

```bash
pip install SHICTHRSVTChecker
```

### 从源码安装

```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_VTChecker.git
cd SHICTHRS_VTChecker
pip install -r requirement.txt
pip install .
```

## 使用方法

```python
from SHICTHRSVTChecker.SHICTHRSVTChecker import SHRVTChecker_get_vt_info

# 获取VT信息
vt_info = SHRVTChecker_get_vt_info()
print(vt_info)
```

输出示例:
```python
{
    'VirtualizationFirmware': {...},
    'DataExecutionPrevention_stu': {...},
    'DataExecutionPrevention_info': {...},
    'SecondLevelAddressTranslationExtensions_stu': {...}
}
```

## 依赖

- Python 3.6+
- colorama==0.4.6

## 许可证

本项目采用 GPL-3.0 许可证。详见 [LICENSE](LICENSE) 文件。

## 作者

SHICTHRS - https://github.com/JNTMTMTM/SHICTHRS_VTChecker

## 版权信息

Copyright © 2025-2026 SHICTHRS, Std. All rights reserved.

## 贡献

欢迎提交 Issue 和 Pull Request！
