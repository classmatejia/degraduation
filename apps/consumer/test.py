import random

adj = {
    '休闲娱乐': ['舒适', '放松', '有趣', '欢乐', '悠闲', '刺激', '有氛围', '精彩', '快乐', "怡然自得", "愉快", "轻松",
                 "惬意", "神奇", "惊喜", "休闲"],
    '周边游': ['美丽', '愉快', '轻松', '惬意', '有趣', '神奇', '惊喜', '休闲', "舒适", "放松", "有氛围", "精彩", "快乐",
               "怡然自得", "多样"],
    '健身运动': ['健康', '锻炼', '有氧', '运动', '强身', '挑战性', '充满活力', "舒适", "放松", "有趣"],
    '丽人': ['美丽', '时尚', '护肤', '美好', '优雅', '自信', '迷人', "舒适", "放松", "有趣"],
    '购物': ['多样', '时尚', '便利', '优质', '物美价廉', '个性化', '潮流', "舒适", "放松", "有趣"],
    '生活服务': ['便捷', '专业', '周到', '贴心', '高效', '安全', '可靠', "舒适", "放松", "有趣"],
    '电影演出赛事': ['精彩', '惊艳', '震撼', '感人', '动人', '音乐', '精致', "舒适", "放松", "有趣"],
    '医疗健康': ['健康', '专业', '安全', '舒适', '医学', '全面', '便捷', "舒适", "放松", "有趣"]
}
merchant_data = {
    '休闲娱乐': ['足疗按摩', '洗浴/汗蒸', 'KTV', '酒吧', '茶馆', '网吧网咖', '棋牌室', '桌球馆'],
    '周边游': ['展馆展览', '采摘/农家乐', '温泉', '动植物园', '水上娱乐', '滑雪', '景点'],
    '健身运动': ['健身中心', '游泳馆', '羽毛球馆', '篮球场', '乒乓球馆', '足球场', '体育场馆'],
    '丽人': ['美发', '美甲美睫', '美容/SPA', '瑜伽', '纹身', '化妆品'],
    '购物': ['综合商场', '服饰鞋包', '运动户外', '珠宝饰品'],
    '生活服务': ['文印图文', '搬家运输', '生活配送', '家政服务', '成人用品', '家电数码维修', '居家维修'],
    '电影演出赛事': ['电影院', '剧场/影院', '音乐厅/礼堂', '热门演出'],
    '医疗健康': ['口腔齿科', '体检中心', '医院', '药店', '中医', '宠物医院', '整形']
}
qu = [
    "和平区",
    "河东区",
    "河西区",
    "南开区",
    "河北区",
    "红桥区",
    "塘沽区",
    "汉沽区",
    "大港区",
    "东丽区",
    "西青区",
    "津南区",
    "北辰区"
]
lu = ['幸福路', '和平路', '建国大街', '自由路', '兴盛街', '繁荣街', '共和路', '世纪大道', '光明路', '富民路', '解放路',
      "人民大街", "听安大道"]
num = 5000000


def random_lu():
    n = random.randint(0, 12)
    random_numbers = random.sample(range(0, 13), 10)
    return [lu[i] for i in random_numbers]


def random_qu():
    random_numbers = random.sample(range(0, 13), 10)
    return [qu[i] for i in random_numbers]


def random_adj(per):
    random_numbers = random.sample(range(0, len(adj[per])), 10)
    return [adj[per][n] for n in random_numbers]


# from apps.merchant.models import Merchant
#
# for category, subtypes in merchant_data.items():
#     for subtype in subtypes:
#         for i in range(1, 11):  # 生成10个商家数据
#             num += 1
#
#             address = f"地址：{random_qu()[i - 1]}区{random_lu()[i - 1]}{i}号"




merged_list = [f"{x}第{random.randint(1,13)}{y}{random.randint(2,30)}号" for x, y in zip(random_qu(), random_lu())]
