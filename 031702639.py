# -*- coding: UTF-8 -*-
import json
import re

class AddressChecker:
    def __init__(self):
        self.__phoneNumber = ''
        self.__name = ''
        self.__addr = ''
        self.ans = {}
    def setfunc(self,address):
        level = address[0]
        try:
            if level=='1':
                self.ans = self.func1(address)
            else:
                self.ans = self.func2(address)
            
        except AttributeError as e:
            print('Error input!:'+e+'请输入正确格式的地址！')
    def func1(self,address):
        address = address[2:]
        myles = re.split(r'[,。，.]',address)
        myles.remove('')
        answer = dict()
        # 分割姓名
        name = myles[0]
        answer['姓名'] = name
        address = address.replace(name,'',1)
        address = address.replace(',','')
        address = address.replace('.','')
        # 分割电话号码
        phoneNumber = re.search(r'\d{11}',address).group()
        answer['手机'] = phoneNumber
        address = address.replace(phoneNumber,'',1)
        # 分割行政区
        pattern = re.compile(r'(?P<province>[^0-9]+?省|.+?自治区)?(?P<city>.{1,3}?市|.{4,8}?自治州|.{2,4}?地区|.{2,4}?盟)?(?P<county>.{1,4}?区|[^0-9]{1,3}?县|.{1,3}?市|.{2,6}?旗)?(?P<town>.{1,4}?街道|.{1,4}?镇|.{1,4}?乡)?(?P<road>.{1,6}?弄|.{1,6}?路|.{1,6}?街|.{1,6}?巷|.{1,6}?道)?(?P<number>\d+?号|\d+.?道)?(?P<village>.*)')
        province=None
        city=None
        county=None
        town=None
        road=None
        number=None
        village=None
        m = pattern.search(address)
        jsArray = []

        list1 = ['北京市','天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '台湾省', '香港特别行政区', '澳门特别行政区']
        list2 = ['北京市','上海市','天津市','重庆市','石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市', '廊坊市', '衡水市', '太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市', '晋中市', '运城市', '忻州市', '临汾市', '吕梁市', '呼和浩特市', '包头市', '乌海市', '赤峰市', '通辽市', '鄂尔多斯市', '呼伦贝尔市', '巴彦淖尔市', '乌兰察布市', '兴安盟', '锡林郭勒盟', '阿拉善盟', '沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '盘锦市', '铁岭市', '朝阳市', '葫芦岛市', '长春市', '吉林市', '四平市', '辽源市', '通化市', '白山市', '松原市', '白城市', '延边朝鲜族自治州', '哈尔滨市', '齐齐哈尔市', '鸡西市', '鹤岗市', '双鸭山市', '大庆市', '伊春市', '佳木斯市', '七台河市', '牡丹江市', '黑河市', '绥化市', '大兴安岭地区', '南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市', '杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市', '合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市', '黄山市', '滁州市', '阜阳市', '宿州市', '六安市', '亳州市', '池州市', '宣城市', '福州市', '厦门市', '莆田市', '三明市', '泉州市', '漳州市', '南平市', '龙岩市', '宁德市', '南昌市', '景德镇市', '萍乡市', '九江市', '新余市', '鹰潭市', '赣州市', '吉安市', '宜春市', '抚州市', '上饶市', '济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市', '潍坊市', '济宁市', '泰安市', '威海市', '日照市', '临沂市', '德州市', '聊城市', '滨州市', '菏泽市', '郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市', '新乡市', '焦作市', '濮阳市', '许昌市', '漯河市', '三门峡市', '南阳市', '商丘市', '信阳市', '周口市', '驻马店市', '武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市', '荆门市', '孝感市', '荆州市', '黄冈市', '咸宁市', '随州市', '恩施土家族苗族自治州', '长沙市', '株洲市', '湘潭市', '衡阳市', '邵阳市', '岳阳市', '常德市', '张家界市', '益阳市', '郴州市', '永州市', '怀化市', '娄底市', '湘西土家族苗族自治州', '广州市', '韶关市', '深圳市', '珠海市', '汕头市', '佛山市', '江门市', '湛江市', '茂名市', '肇庆市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '南宁市', '柳州市', '桂林市', '梧州市', '北海市', '防城港市', '钦州市', '贵港市', '玉林市', '百色市', '贺州市', '河池市', '来宾市', '崇左市', '海口市', '三亚市', '三沙市', '儋州市', '成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '眉山市', '宜宾市', '广安市', '达州市', '雅安市', '巴中市', '资阳市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州', '贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '昆明市', '曲靖市', '玉溪市', '保山市', '昭通市', '丽江市', '普洱市', '临沧市', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州', '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州', '迪庆藏族自治州', '拉萨市', '日喀则市', '昌都市', '林芝市', '山南市', '那曲市', '阿里地区', '西安市', '铜川市', '宝鸡市', '咸阳市', '渭南市', '延安市', '汉中市', '榆林市', '安康市', '商洛市', '兰州市', '嘉峪关市', '金昌市', '白银市', '天水市', '武威市', '张掖市', '平凉市', '酒泉市', '庆阳市', '定西市', '陇南市', '临夏回族自治州', '甘南藏族自治州', '西宁市', '海东市', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '银川市', '石嘴山市', '吴忠市', '固原市', '中卫市', '乌鲁木齐市', '克拉玛依市', '吐鲁番市', '哈密市', '昌吉回族自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州', '喀什地区', '和田地区', '伊犁哈萨克自治州', '塔城地区', '阿勒泰地区']

        if m:
            city = m.group('city')
            # 直辖市判断
            if(city=='北京市' or city=='上海市' or city=='天津市' or city=='重庆市'):
                jsArray.append(city[:2])
                
            else:
                province = m.group('province')
                if(province):
                    jsArray.append(province)
                else:#与1级地址比对
                    for s in list1:
                        if s[:2]==address[:2]:
                            if(s=='北京市' or s=='上海市' or s=='天津市' or s=='重庆市'):
                                province = s[:2]
                                jsArray.append(s[:2])
                                break
                            province=s
                            jsArray.append(s)
                            if province[-1:]=='省':
                                address = address.replace(province[:-1],'',1)
                            if province[-3:]=='自治区' or province[-3:]=='行政区':
                                address = address.replace(province[:-3],'',1)
                            break
                    if not province:
                        
                        jsArray.append('')
            cityOne =None
            b = pattern.search(address)
            cityOne=b.group('city')
            
            if cityOne:
                
                jsArray.append(cityOne)
            else: #与二级地址比对
                
                for s in list2:
                    if s[:2]==address[:2]:
                        cityOne=s
                        jsArray.append(s)
                        if cityOne[-1:]=='市' or cityOne[-1:]=='盟':
                            address = address.replace(cityOne[:-1],'',1)
                        if cityOne[-3:]=='自治洲':
                            address = address.replace(cityOne[:-3],'',1)
                        break
                if not cityOne:
                        jsArray.append('')
            c = pattern.search(address)
            
            countyOne = c.group("county")
            if countyOne:
                jsArray.append(countyOne)
            else:
                jsArray.append('')

            town = c.group("town")
            if town:
                jsArray.append(town)
            else:
                jsArray.append('')
            
            village = c.group("village")
            if village:
                jsArray.append(village)
            else:
                jsArray.append('')
        answer['地址'] = jsArray
        return answer
    def func2(self,address):
        
        address = address[2:]
        myles = re.split(r'[,。，.]',address)
        myles.remove('')
        answer = dict()
        # 分割姓名
        name = myles[0]
        answer['姓名'] = name
        address = address.replace(name,'',1)
        address = address.replace(',','')
        address = address.replace('.','')
        # 分割电话号码
        phoneNumber = re.search(r'\d{11}',address).group()
        answer['手机'] = phoneNumber
        address = address.replace(phoneNumber,'',1)
       
        # 分割行政区
        pattern = re.compile(r'(?P<province>[^0-9]+?省|.+?自治区)?(?P<city>.{1,3}?市|.{4,8}?自治州|.{2,4}?地区|.{2,4}?盟)?(?P<county>.{1,4}?区|[^0-9]{1,3}?县|.{1,3}?市|.{2,6}?旗)?(?P<town>.{1,4}?街道|.{1,4}?镇|.{1,4}?乡)?(?P<road>.{1,6}?弄|.{1,6}?路|.{1,6}?街|.{1,6}?巷|.{1,6}?道)?(?P<number>\d+?号|\d+.?道)?(?P<village>.*)')
        province=None
        city=None
        county=None
        town=None
        road=None
        number=None
        village=None
        m = pattern.search(address)
        
        jsArray = []
        list1 = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '台湾省', '香港特别行政区', '澳门特别行政区']
        list2 = ['北京市','上海市','天津市','重庆市','石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市', '廊坊市', '衡水市', '太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市', '晋中市', '运城市', '忻州市', '临汾市', '吕梁市', '呼和浩特市', '包头市', '乌海市', '赤峰市', '通辽市', '鄂尔多斯市', '呼伦贝尔市', '巴彦淖尔市', '乌兰察布市', '兴安盟', '锡林郭勒盟', '阿拉善盟', '沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '盘锦市', '铁岭市', '朝阳市', '葫芦岛市', '长春市', '吉林市', '四平市', '辽源市', '通化市', '白山市', '松原市', '白城市', '延边朝鲜族自治州', '哈尔滨市', '齐齐哈尔市', '鸡西市', '鹤岗市', '双鸭山市', '大庆市', '伊春市', '佳木斯市', '七台河市', '牡丹江市', '黑河市', '绥化市', '大兴安岭地区', '南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市', '杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市', '合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市', '黄山市', '滁州市', '阜阳市', '宿州市', '六安市', '亳州市', '池州市', '宣城市', '福州市', '厦门市', '莆田市', '三明市', '泉州市', '漳州市', '南平市', '龙岩市', '宁德市', '南昌市', '景德镇市', '萍乡市', '九江市', '新余市', '鹰潭市', '赣州市', '吉安市', '宜春市', '抚州市', '上饶市', '济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市', '潍坊市', '济宁市', '泰安市', '威海市', '日照市', '临沂市', '德州市', '聊城市', '滨州市', '菏泽市', '郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市', '新乡市', '焦作市', '濮阳市', '许昌市', '漯河市', '三门峡市', '南阳市', '商丘市', '信阳市', '周口市', '驻马店市', '武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市', '荆门市', '孝感市', '荆州市', '黄冈市', '咸宁市', '随州市', '恩施土家族苗族自治州', '长沙市', '株洲市', '湘潭市', '衡阳市', '邵阳市', '岳阳市', '常德市', '张家界市', '益阳市', '郴州市', '永州市', '怀化市', '娄底市', '湘西土家族苗族自治州', '广州市', '韶关市', '深圳市', '珠海市', '汕头市', '佛山市', '江门市', '湛江市', '茂名市', '肇庆市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '南宁市', '柳州市', '桂林市', '梧州市', '北海市', '防城港市', '钦州市', '贵港市', '玉林市', '百色市', '贺州市', '河池市', '来宾市', '崇左市', '海口市', '三亚市', '三沙市', '儋州市', '成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '眉山市', '宜宾市', '广安市', '达州市', '雅安市', '巴中市', '资阳市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州', '贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '昆明市', '曲靖市', '玉溪市', '保山市', '昭通市', '丽江市', '普洱市', '临沧市', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州', '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州', '迪庆藏族自治州', '拉萨市', '日喀则市', '昌都市', '林芝市', '山南市', '那曲市', '阿里地区', '西安市', '铜川市', '宝鸡市', '咸阳市', '渭南市', '延安市', '汉中市', '榆林市', '安康市', '商洛市', '兰州市', '嘉峪关市', '金昌市', '白银市', '天水市', '武威市', '张掖市', '平凉市', '酒泉市', '庆阳市', '定西市', '陇南市', '临夏回族自治州', '甘南藏族自治州', '西宁市', '海东市', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '银川市', '石嘴山市', '吴忠市', '固原市', '中卫市', '乌鲁木齐市', '克拉玛依市', '吐鲁番市', '哈密市', '昌吉回族自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州', '喀什地区', '和田地区', '伊犁哈萨克自治州', '塔城地区', '阿勒泰地区']
        if m:
            city = m.group('city')
            # 直辖市判断
            if(city=='北京市' or city=='上海市' or city=='天津市' or city=='重庆市'):
                jsArray.append(city[:2])
            else:
                province = m.group('province')
                if(province):
                    jsArray.append(province)
                else:#与1级地址比对
                    for s in list1:
                        
                        if s[:2]==address[:2]:
                            if(s=='北京市' or s=='上海市' or s=='天津市' or s=='重庆市'):
                                province = s[:2]
                                jsArray.append(s[:2])
                                break
                            province=s
                            jsArray.append(s)
                            if province[-1:]=='省':
                                address = address.replace(province[:-1],'',1)
                            if province[-3:]=='自治区' or province[-3:]=='行政区':
                                address = address.replace(province[:-3],'',1)
                            break
                    if not province:
                        jsArray.append('')
            cityOne =None
            b = pattern.search(address)
            cityOne=b.group('city')
            if cityOne:
                jsArray.append(cityOne)
            else: #与二级地址比对
                for s in list2:                 
                    if s[:2]==address[:2]:
                        cityOne=s
                        jsArray.append(s)
                        if cityOne[-1:]=='市' or cityOne[-1:]=='盟':
                            address = address.replace(cityOne[:-1],'',1)
                        if cityOne[-3:]=='自治洲':
                            address = address.replace(cityOne[:-3],'',1)
                        break
                if not cityOne:
                        jsArray.append('')
            c = pattern.search(address)
            
            countyOne = c.group("county")
            if countyOne:
                jsArray.append(countyOne)
            else:
                jsArray.append('')

            town = c.group("town")
            if town:
                jsArray.append(town)
            else:
                jsArray.append('')
            
            road = c.group("road")
            if road:
                jsArray.append(road)
            else:
                jsArray.append('')
            
            number = c.group("number")
            if number:
                jsArray.append(number)
            else:
                jsArray.append('')
            
            village = c.group("village")
            if village:
                jsArray.append(village)
            else:
                jsArray.append('')
        answer['地址'] = jsArray
        # print(answer)
        return answer
address = input()
a =AddressChecker()
a.setfunc(address)
# print(a.ans)
js = json.dumps(a.ans,ensure_ascii=False)
print(js)