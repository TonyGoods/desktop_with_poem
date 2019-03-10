# desktop_with_poem
一个每次开机都会有一个附带诗词的桌面

使用前，请先确定拥有 python 3.6 环境

操作步骤：
1. 首先按下 windows + R 键，输入 shell:startup，打开启动窗口
2. 将 src 目录下的 main.pyw - 快捷方式 复制到启动窗口

# setting.json

### shouldChangeImage: 是否需要更换背景图，值为 true 或者 false

### imagePath: 如果不需要更换背景图时，给定的背景图地址

### usingThisProgram: 是否在开机后运用本程序，值为 true 或者 false

### shouldChangePoem: 是否需要更换诗词，值为 true 或者 false

### shouldRemoveBeforeImage: 是否需要删除之前的桌面图，值为 true 或者 false