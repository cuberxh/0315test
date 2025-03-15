# 数据字段列表
fnds = [
    "fnd17_oxlcxspebq", "fnd17_shsoutbs", "fnd28_value_05191q", "fnd28_value_05301q",
    "fnd28_value_05302q", "fnd17_pehigh", "fnd17_pelow", "fnd17_priceavg150day",
    "fnd17_priceavg200day", "fnd17_priceavg50day", "fnd17_pxedra", "fnd28_newa3_value_18191a",
    "fnd28_value_02300a", "mdl175_ebitda", "mdl175_pain"
]


ans = [] #结果集

#双重循环列举每一种可能，加入结果集
for i in range(len(fnds)):
    for j in range(i + 1, len(fnds)):
        A = fnds[i]
        B = fnds[j]
        str = f"ts_regression(ts_zscore({A}, 500), ts_zscore({B}, 500), 500)"
        ans.append(str)

#输出结果
for i in ans:
    print(i)

#计算总数，直接求结果集的长度即可
print(f"Total : {len(ans)}")
