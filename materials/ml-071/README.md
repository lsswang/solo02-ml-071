# 阅读题组工具起点

Python 3.11；生产起点只用标准库。可使用NumPy、SciPy或自动微分扩展。

运行：

`python demo.py`

`topic_model.py`实现当前完整计数的后验和无系数loss；`testlet_assembly.py`实现当前逐题独立覆盖。接口可重构，保留一个能直接查询主题和直接接受外部联合概率表选卷的入口。`example.json`是可运行的合成普通输入，目标合同以题面为准。

example.json的training为固定训练演示，默认max_iter=1000，ridge=0.2；初值与全部记录均显式列出。
