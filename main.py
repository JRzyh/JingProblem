import random
import fractions

times = input("How many times do you wan to try: ")
for i in range(int(times)):
    print("\n", i + 1, ":", end='')
    v = random.randint(1, 250)
    m = random.randint(1, 114514) * 100
    pMetal = random.randint(ceil(m/v), 200) * 100
    pTree = random.randint(5, floor(m/v)) * 100
    vMetal = fractions.Fraction(m - pTree * v, pMetal - pTree)
    vTree = v - vMetal
    # if vMetal <= 0 or vTree <= 0:
    #     print("FAILED")
    #     continue
    mMetal = pMetal * vMetal
    mTree = pTree * vTree
    vMetalValue = round(vMetal.numerator/vMetal.denominator, 2)
    vTreeValue = round(vTree.numerator/vTree.denominator, 2)
    mMetalValue = round(mMetal.numerator/mMetal.denominator, 2)
    mTreeValue = round(mTree.numerator/vTree.denominator, 2)
    print("一只鲸鱼总容积为 {} 立方米，所能承载的物质质量最大为 {} 千克，现在要用木头和金属放满整只鲸鱼。已知木头的密度为 {} 千克每立方米，金属的密度为 {} 千克每立方米，求应放质量为多少的木头和金属。"
          .format(v, m, pTree, pMetal))
    print("参考答案：木头质量为{}千克，金属质量为{}千克，木头体积为{}立方米，金属体积为{}立方米。".format(mTreeValue, mMetalValue, vTreeValue, vMetalValue))

print("Done.")
