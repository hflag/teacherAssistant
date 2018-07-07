第一次提交
需要注意的事项：
1. 因为在teacher应用中使用了django内置登录和退出，所以在项目settings.py
中的apps内，teacher一定要放置在admin前！
2. bootstrap中要想使用ajax那么要使用jquery取代bootstrap默认使用的jquery.slim.js,
改用jquery.min.js