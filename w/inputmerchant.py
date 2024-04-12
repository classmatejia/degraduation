
# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:8000/merchant/register")
file_path = "火锅67.txt"
name = ""
password = ""
qqemail = ""
phone = ""
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    for i in content.split("\n")[2:]:
        if i.startswith("商家名称："):
            name = i[5:]
            print(name)
        elif i.startswith("地址："):
            # print(i[3:])
            pass
        elif i.startswith("电话："):
            phone = i[3:]
            password = i[3:]
            qqemail = i[3:]+"@qq.com"
            print(qqemail)
            print(phone,password)
        else:
            continue
    Merchant.objects.create(merchantmen=merchant_name, email=email, password=password,
                            mobile=phone)