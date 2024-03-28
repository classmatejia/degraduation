<template>
  <div class="top-nav" id="nav" v-cloak>
    <div class="top-nav-content">
      <div class="l-nav">
        <ul>
          <li class="selected-city"><span></span>广州</li>
          <li class="change-city"><a href="#">切换城市</a></li>
          <li class="l-bra">[</li>
          <li class="city"><a href="#">佛山</a></li>
          <li class="city"><a href="#">顺德</a></li>
          <li class="city"><a href="#">南沙</a></li>
          <li class="r-bra">]</li>

        </ul>
      </div>

      <div class="r-nav">
        <ul>
          <li v-if="!isLoggedIn" class="login"><a href="/login">立即登录</a></li>
          <li v-else class="username">[[ username ]]</li>
          <li v-if="!isLoggedIn" class="register"><a href="/register">注册</a></li>

          <li class="account"><a href="#">个人中心</a></li>
          <li class="app"><a href="#">手机APP</a></li>
          <li class="merchant"><a href="#">商家中心</a></li>
          <li class="site-nav"><a href="#">网站导航</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default ({
  delimiters: ['[[', ']]'],
  data() {
    return {
      isLoggedIn: false,
      username: ''
    };
  },
  mounted() {
    // 检查 cookie 中是否存在用户名
    const username = this.getCookie('username');
    if (username) {
      this.isLoggedIn = true;
      // 将字符串转换为 Uint8Array
      const byteArray = new Uint8Array(username.match(/[\da-f]{2}/gi).map(function (h) {
        return parseInt(h, 16)
      }));
      // 使用 TextDecoder 解码
      const textDecoder = new TextDecoder('utf-8');
      const decodedString = textDecoder.decode(byteArray);
      console.log(decodedString); // 输出解码后的字符串
      this.username = decodedString;
      console.log(this.username);
    }
  },
  methods: {
    getCookie(name) {
      // 使用JavaScript函数获取cookie
      const cookieName = name + "=";
      const decodedCookie = decodeURIComponent(document.cookie);
      const cookieArray = decodedCookie.split(';');
      for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
          cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
          return cookie.substring(cookieName.length, cookie.length);
        }
      }
      return '';
    },

  }
});
</script>

<style scoped>
/*顶部导航条部分*/

.top-nav {
  height: 40px;
  padding: 0 36px;
  /*border: 1px solid red;*/
  /*width: 100%;*/

}

.top-nav .top-nav-content {
  /*display: block;*/
  margin: 0 auto;
  width: 1190px;
  /*border: 1px solid blue;*/
}

.top-nav ul li {
  font-size: 12px;
  line-height: 40px;

}

/*顶部导航条左边*/
.top-nav .l-nav {
  float: left;
  /*border: 1px solid #000;*/
}

.top-nav .l-nav ul li {
  float: left;
  padding: 0 3px;
  /*border: 0.1px solid red;*/
}

.top-nav .l-nav ul li a:hover {
  color: #31bbac;
}

.top-nav .l-nav .login a {
  color: #31bbac;
  padding: 0 2px 0 18px;
}

.top-nav .l-nav .selected-city {
  padding-left: 12px;
  position: relative;
  color: #666;
  /*border: 1px solid red; */
}

.top-nav .l-nav .selected-city span {
  display: inline-block;
  position: absolute;
  width: 12px;
  height: 12px;
  top: 50%;
  left: 0;
  margin-top: -6px;
  background-image: url("../img/icon/position.png");
  background-repeat: no-repeat;
  background-size: 100% 100%;
  /*border: 1px solid blue;*/
}

.top-nav .l-nav .change-city a {
  display: inline-block;
  width: 48px;
  height: 12px;
  line-height: 12px;
  border: 1px solid #e5e5e5;
  border-radius: 2px;
  padding: 2px;
  color: #666;
}

/*顶部导航条右边*/
.top-nav .r-nav {
  float: right;
  /*border: 1px solid #000;*/
}

.top-nav .r-nav ul li {
  float: left;
  padding: 0 15px;
  /*border: 1px solid red;*/
}

.top-nav .r-nav ul a:hover {
  color: #31bbac;
}

</style>