# -*- coding:UTF-8 -*-
# @Time : 2022/1/30 10:29
# @Author : Palm
# @Remark :


URL_EX = {
    "params_dict":  {
        "base": {
            "name": "省份地区",
            "value_list": [
                ("北京", "bj"), ("天津", "tj"), ("河北", "heb"), ("山西省", "sx"),  ("内蒙古", "nmg"),
                ("辽宁", "ln"), ("吉林", "jl"), ("黑龙江", "hlj"), ("上海", "sh"),  ("江苏", "js"),
                ("浙江", "zj"), ("安徽", "ah"), ("福建", "fj"), ("江西", "jx"),  ("山东", "sd"),
                ("河南", "hen"), ("湖北", "hub"), ("湖南", "hun"), ("广东", "gd"),  ("广西", "gx"),
                ("海南", "han"), ("重庆", "cq"), ("四川", "sc"), ("贵州", "gz"),  ("云南", "yn"),
                ("西藏", "xz"), ("陕西", "snx"), ("甘肃", "gs"), ("青海", "qh"),  ("宁夏", "nx"),
                ("新疆", "xj"), ("香港", "hk"), ("澳门", "mo"), ("台湾", "tw")
            ]
        },
        "companyType": {
            "name": "企业描述",
            "value_list": [
                ("企业", "normal_company"), ("事业单位", "institution"), ("基金会", "npo_foundation"),
                ("社会团体", "npo"), ("律师事务所", "lawFirm"), ("中国香港企业", "hk"), ("中国台湾企业", "tw"),
                ("机关机构", "organization")
            ]
        }
    },
    "slash_dict": {
        "funds": {
            "name": "注册资本",
            "amount": ["or0100", "or100200", "or200500", "or5001000", "or1000"]
        },
        "establish": {
            "name": "成立时间",
            "time": ["oe01", "oe015", "oe510", "oe1015", "oe15"]
        },
        "industry": {
            "name": "行业分类",
            "classify": [
                "ocA", "ocB", "ocC", "ocD", "ocE", "ocF", "ocG", "ocH", "ocI",
                "ocJ", "ocK", "ocL", "ocM", "ocN", "ocO", "ocP", "ocQ", "ocR",
                "ocS", "ocT"
            ]
        },
        "currency": {
            "name": "资本类型",
            "classify": ["ot1", "ot2", "ot3"]
        },
        "enterprise": {
            "name": "企业类型",
            "classify": ["oot1", "oot2", "oot3", "oot4", "oot5", "oot6", "oot7", "oot8", "oot9", "oot10", "oot11"]
        },
        "Insured": {
            "name": "参保人数",
            "classify": ["oss050", "oss5099", "oss100499", "oss500999", "oss4999", "oss9999", "oss10000"]
        }
    }
}

SEARCH_URL = "https://www.tianyancha.com/search/"

DB_TABLE = 'company'