Q&A
===================

重写 get_access_token 函数来自定义 token 的存储
-------------------------------------------------

首先我们看 ``get_access_token()`` 的源码::

    def get_access_token(self) -> str:
        """
        判断现有的token是否过期。
        用户需要多进程或者多机部署可以手动重写这个函数
        来自定义token的存储，刷新策略。

        :return: 返回 ``token``
        """
        if self._token:
            now = time.time()
            if self.token_expires_at - now > 60:
                return self._token
        with LOCK:
            json_str = self.grant_token()
            self._token = json_str["access_token"]
            self.token_expires_at = int(time.time()) + json_str["expires_in"]
        return self._token

这其中包含了两个功能：

+ 通过时间戳对现有 ``token`` 判断是否过期；若未过期，则直接返回现有的 ``token``
+ 对现有 ``token`` 判断是否过期；若过期了，对进程进行上锁，并重新获取 ``token``

因此，在重写 ``get_access_token()`` 时，请务必保证这两个功能的实现，并在重新获取 ``token`` 和 ``token_expires_at`` 后，即可对其进行 \
自定义操作，例如::

    def get_access_token(self) -> str:
        if self._token:
            now = time.time()
            if self.token_expires_at - now > 60:
                return self._token
        with LOCK:
            json_str = self.grant_token()
            self._token = json_str["access_token"]
            self.token_expires_at = int(time.time()) + json_str["expires_in"]

        # 从这里开始即可进行自定义 ``token`` 的操作
        return self._token

