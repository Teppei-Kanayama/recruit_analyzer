import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import collections
import math

#データファイル名
filename = "./data/tsemi_recruit_data.xlsx"

#各シートの読み込み
applyment = pd.read_excel(filename, index_col=0, sheetname="applyment_sheet")
comment1 = pd.read_excel(filename, index_col=0, sheetname="comment_sheet1")
comment2 = pd.read_excel(filename, index_col=0, sheetname="comment_sheet2")
comment3 = pd.read_excel(filename, index_col=0, sheetname="comment_sheet3")
join = pd.read_excel(filename, index_col=0, sheetname="join_sheet")

#各人の属性
course =  applyment.ix[:, 7]
grade = applyment.ix[:, 8]
bunri = applyment.ix[:, 5]
univ = applyment.ix[:, 4]

def show_grade_and_bunri(sheet, title, output_path):
    #文系低学年・文系高学年・理系低学年・理系高学年・医療系低学年・医療系高学年のそれぞれの割合を調べる。
    bunri_list = np.array([0, 0, 0, 0, 0, 0])
    for i in list(sheet.index):
        if (course[i] == "B") and (grade[i] <= 3):
            ishigh = 0
        else:
            ishigh = 1

        if not math.isnan(bunri[i]):
            bunri_list[int(bunri[i] - 1) * 2 + ishigh] += 1

    print(bunri_list)

    data = bunri_list
    label = ["理系（医療系以外）低学年", "理系（医療系以外）高学年", "医療系低学年", "医療系高学年", "文系低学年", "文系高学年"]

    #plt.style.use('ggplot')
    plt.style.use('seaborn-pastel')
    plt.rcParams.update({'font.size':15})
    size=(9,5)

    ###pie###
    plt.figure(figsize=size,dpi=100)
    plt.pie(data,counterclock=False,startangle=90,autopct=lambda p:'{:.1f}%'.format(p) if p>=5 else '')
    plt.subplots_adjust(left=0,right=0.7)
    plt.legend(label,fancybox=True,loc='center left',bbox_to_anchor=(0.9,0.5))
    plt.axis('equal')
    plt.title(title)
    plt.savefig(output_path, bbox_inches='tight',pad_inches=0.05)

def show_univ(sheet, title, output_path):
    #各大学ごとの人数を調べる。
    univ_dict = {}
    for i in list(sheet.index):
        if type(univ[i]) is str:
            try:
                univ_dict[univ[i]] += 1
            except KeyError:
                univ_dict[univ[i]] = 1

    sorted_index = np.argsort(np.array(list(univ_dict.values())))

    sorted_values = []
    sorted_keys = []
    for ind in sorted_index:
        sorted_values.append(list(univ_dict.values())[ind])
        sorted_keys.append(list(univ_dict.keys())[ind])

    plt.figure(figsize=(15, 10))
    plt.title(title, fontsize=18)
    plt.bar(np.array(range(len(sorted_keys))) * 10, sorted_values[::-1], tick_label=sorted_keys[::-1], align="center", width=5)
    plt.savefig(output_path)

def show_grade(sheet, title, output_path):

    grade_list = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in list(sheet.index):
        try:
            if course[i] == "B":
                grade_list[int(grade[i]) - 1] += 1
            elif course[i] == "M":
                grade_list[int(grade[i]) + 5] += 1
            elif course[i] == "R" or course[i] == "S":
                grade_list[8] += 1
        except ValueError:
            pass
    print(grade_list)
    label = ["B1", "B2", "B3", "B4", "B5", "B6", "M1", "M2", "その他"]
    plt.title(title)
    plt.bar(np.array(range(9)), grade_list, tick_label=label, align="center")
    plt.savefig(output_path)

def main():
    #show_grade(comment1, "第一回説明会参加者の学年分布", "./figures/test.png")
    """
    show_grade_and_bunri(applyment, "説明会申込者の文理・学年", "./figures/applyment_bunri-grade.png")
    show_grade_and_bunri(comment1, "第一回説明会参加者の文理・学年", "./figures/comment1_bunri-grade.png")
    show_grade_and_bunri(comment2, "第二回説明会参加者の文理・学年", "./figures/comment2_bunri-grade.png")
    show_grade_and_bunri(comment3, "第三回説明会参加者の文理・学年", "./figures/comment3_bunri-grade.png")
    show_grade_and_bunri(join, "入ゼミ者の文理・学年", "./figures/join_bunri-grade.png")
    """
    show_univ(applyment, "説明会申込者の所属大学", "./figures/applyment_univ.png")
    show_univ(comment1, "第一回説明会参加者の所属大学", "./figures/comment1_univ.png")
    show_univ(comment2, "第二回説明会参加者の所属大学", "./figures/comment2_univ.png")
    show_univ(comment3, "第三回説明会参加者の所属大学", "./figures/comment3_univ.png")
    show_univ(join, "入ゼミ者の所属大学", "./figures/join_univ.png")

if __name__ == "__main__":
    main()
