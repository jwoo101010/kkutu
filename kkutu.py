# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:07:30 2024

@author: user
"""
# 처음 단어, 미션 글자 정하기
import random as r
# 입력시간, 제한 시간 측정
import time as tm

# 파일에서 데이터 불러와 데이터베이스 만들기
file=open("C:/Users/jwoo/Desktop/백업자료/20250311 백업/python/python/끄투 한글 모든 단어(어인정 포함).txt",'r',encoding='UTF-8')
text_all=file.read()
file.close()

data_base=list(text_all.split("\n"))

###############################################################################

# 가동시간: 45.6분
# 한방단어 포함 글자 찾기
# 조건: 이 글자로 끝나는 단어는 있되, 이 글자로 시작하는 것은 ㅇㅓㅄ다.
ifcheck=input("(start:program start->")
if ifcheck.lower()=='start':
    chr_li=range(ord('가'),ord('힣')+1)
    cl_sn=[0]*len(chr_li)
    cl_en=[0]*len(chr_li)
    st_ft=tm.time()
    print("start", st_ft)
    # 5,8/68,60/6,912개의 데이터 탐지(약 58억 7천만게)
    for k in range(len(chr_li)):
        # 11172개
        if k%100==0:
            print(chr(chr_li[k]),k, tm.time()-st_ft)
        # print(chr(chr_li[k]), "으로 시작하거나 끝나는 단어 탐색 시작")
        for s in data_base:
            # 525296개
            if s[0]==chr(chr_li[k]):
                # print(s)
                cl_sn[k]+=1
            if s[-1]==chr(chr_li[k]):
                # print(s)
                cl_en[k]+=1
        # print(chr(chr_li[k]),"으로 시작하거나 끝나는 단어 탐색 종료")
    et_ft=tm.time()
    print("end\n", et_ft-st_ft , "초 걸렸습니다.")
    for i in range(len(chr_li)):
        if cl_sn[i]==0 and cl_en[i]!=0:
            print(chr(chr_li[i]))
        
    for i in range(len(chr_li)):
        if cl_sn[i]>0 and cl_sn[i]<=10 and cl_en[i]!=0:
            print(chr(chr_li[i]))

kill=list("갏갗걋겇겊겿곻굠궃궝귐긑긶긿깆깥깸껸껼꼇꼍꾜꿑뀜끠냏냑냔냘넁넠녁녆녘뇰늄늉닺덟뎧뎬돓됵뒿듈듐듥듦듧듫땽뗌똣뜩뜹랋랒랓랖랗랸럿렁렇렫렷롫룀룅룔뤂뤠륨른릅릇릊릎릏릐맣먕묗묭뮴믁믏믐밇및밗벹볌볜봊봏봠붏붖붚븀븐븜빋뼌뿟쁜쁨샄샥섦섴솣숡숰숳슨싕싥싴싶쎔쑴씃앚앝얒얗얫얶얺엃엋엌엻옄옺왐욷웆웋웝웸윅읃읅읆읋읒읓읔읕읖읗읭잫졎죌즑짗쨔쨤쨩쭘쯕쯘쯤찱챱쳡촙촨춰췐츌츔츨칮칲컽켓켸콫쾃쿱쿽큅큠큭탉탸텋텝텹톹툑튬틋틤팹푄퓔퓸픈픔픠픳핥홣훕휵흿")
t_kill=list("갇갉값갬갭걍걔겜겝겯겻곗곬곶괌괵굄궈궨귄귿긧긱깅깟깩깰꺅꺌껀껏껙껨껭꼉꼿꽂꽐꽛꽤꽥꾐꾹꾼꿉꿋꿔꿜꿱뀀뀌뀨끅끗끙낀낌낏낑낢낵낸냅냬넛넣넨넴녈녑녓녜놉놔뇸뇽눔눕눙뉵늡늣늬닙닝닢댜덛뎀뎁뎃뎍뎜뎝뎡뎨돐돝돠돨됨됭둬뒈듁듕듭듯듸딍딤딧딮땍땐떤떰떳떵떽똔똠똴뙁뚤뚬뜽띔띨띰띵랏랙랠랫랴럴럽렐렘렙렝롄롭롶룹룻뤽륀륄를름릭릿맡몃몌몫몹묑뭄뮌뮨뮬믄믓믜밈밟뱍벰봅봐붑뷜뷩븨븩빰빱빳빽뺌뺙뺨뻑뻣뼉뼘뽁뽄뽐뽓뿅뿍뿐뿜뿡쁠삑삔삠삣삵샃샵샷섄섯셉셕션셤셥셧셩셴솝솨솰쇅쇡쇽숀숍숏숑숱숴쉑쉔쉭쉼슉슌슘슝슥슭슴슷싁쌕쌤쌰썹쎈쎌쏜쏨쏭쏴쏼쐬쑈쑨쑬쒜쒸쓱씁씸씹않앓앳얍얏얭엊엣옭왑왝왬왹욍욘욜욤욹웁웍웡웩윔윕윰윽읏읫잽쟉쟌쟘젝젹졀졈졉졋졍졔좃좆좍좔좡죔죡죤죵줅줘줴쥭쥴즘즛짭짯짹쨀쨈쩍쩐쩜쩝쩟쩡쫙쫠쭌쮸쯔쯜쯧쯩찟챵첵쳉쳑쳔쳠쳥촘쵹춍츈츤츩츰츱츳츼칫캅캑캭캴컁컥컹켐켜켠콱콸쾅쿄쿰퀄퀑큘킁킴킵탓탠탯텁텟텡텨톄툐툼툽퉤튕튝튠튱틔팁팎팟팰팸팻퍅펍펏펙펴펵폿푀푱퓽픗핌했햐헉헙헴홋홧홱횅훅훙훠훨휑휙휩휭흴힝")

"""
for i in kill:
    print("\n",i)
    for s in data_base:
        if s[-1]==i:
            print(s)
"""
##############################################################################        
def print_ans(l):
    for i in l:
        print(i)
###############################################################################
# 특정 글자로 시잣하는 단어(1글자), 특정 글자가 들어가는 단어(1글자)
print("시작하는 글자, 들어가는 단어나 글자를 줄바꿔서 입력")
print("이때, 두번째 단어나 글자를 안 넣으면 첫번째 글자로 시작하는 단어만 나열")
print("첫 글자는 시작단어, 두번째 글자는 끄투 점수글자")
st_txt=input()
mustin_txt=input()

ans_list=[]
for s in data_base:
    if s[0]==st_txt and mustin_txt=='':
        ans_list.append(s)
    elif s[0]==st_txt and mustin_txt in s:
        ans_list.append(s)
if ans_list==[]:
    print("[system]: 해당 조건에 맞는 단어가 존재하지 않습니다.")
else:
    print_ans(ans_list)

print()
###############################################################################
# 내가 입력한 단어를 이을 수 있는  단어를 모두 출력
# 만약 내가 입력한 단어가 없다면 이을 수 없다 판단
# 이을 단어가 없어도 이을 수 없다 판단
print("입력한 단어를 이을 수 있는 단어를 출력합니다.")
my_txt=input()

if my_txt in data_base:
    last_txt=my_txt[-1]
    
    ans_list=[]
    for s in data_base:
        if s[0]==last_txt:
            ans_list.append(s)
            
    if ans_list==[]:
        print("[system]: 해당 단어로 이을 수 있는 단어가 존재하지 않습니다.")
    else:
        print_ans(ans_list)

else:
    print("[system]: 입력한 단어가 존재하지 않습니다.")
    
print('#'*60)
###############################################################################
print("특정 글자로 끝나는 글자 입력")
inp=input()
le=len(inp)
ans_list=[]
for s in data_base:
    if s[-1]==inp:
        ans_list.append(s)
if ans_list==[]:
    print("[system]: 해당 조건에 맞는 단어가 존재하지 않습니다.")
else:
    print_ans(ans_list)

print()

###############################################################################
print("끄투 끝말잇기가 시작되었습니다. 엔터를 치면 시작됩니다.")
_=input()
# https://mengmota.blogspot.com/2020/04/blog-post.html
kill=list("갏갗걋겇겊겿곻굠궃궝귐긑긶긿깆깥깸껸껼꼇꼍꾜꿑뀜끠냏냑냔냘넁넠녁녆녘뇰늄늉닺덟뎧뎬돓됵뒿듈듐듥듦듧듫땽뗌똣뜩뜹랋랒랓랖랗랸럿렁렇렫렷롫룀룅룔뤂뤠륨른릅릇릊릎릏릐맣먕묗묭뮴믁믏믐밇및밗벹볌볜봊봏봠붏붖붚븀븐븜빋뼌뿟쁜쁨샄샥섦섴솣숡숰숳슨싕싥싴싶쎔쑴씃앚앝얒얗얫얶얺엃엋엌엻옄옺왐욷웆웋웝웸윅읃읅읆읋읒읓읔읕읖읗읭잫졎죌즑짗쨔쨤쨩쭘쯕쯘쯤찱챱쳡촙촨춰췐츌츔츨칮칲컽켓켸콫쾃쿱쿽큅큠큭탉탸텋텝텹톹툑튬틋틤팹푄퓔퓸픈픔픠픳핥홣훕휵흿")
t_kill=list("갇갉값갬갭걍걔겜겝겯겻곗곬곶괌괵굄궈궨귄귿긧긱깅깟깩깰꺅꺌껀껏껙껨껭꼉꼿꽂꽐꽛꽤꽥꾐꾹꾼꿉꿋꿔꿜꿱뀀뀌뀨끅끗끙낀낌낏낑낢낵낸냅냬넛넣넨넴녈녑녓녜놉놔뇸뇽눔눕눙뉵늡늣늬닙닝닢댜덛뎀뎁뎃뎍뎜뎝뎡뎨돐돝돠돨됨됭둬뒈듁듕듭듯듸딍딤딧딮땍땐떤떰떳떵떽똔똠똴뙁뚤뚬뜽띔띨띰띵랏랙랠랫랴럴럽렐렘렙렝롄롭롶룹룻뤽륀륄를름릭릿맡몃몌몫몹묑뭄뮌뮨뮬믄믓믜밈밟뱍벰봅봐붑뷜뷩븨븩빰빱빳빽뺌뺙뺨뻑뻣뼉뼘뽁뽄뽐뽓뿅뿍뿐뿜뿡쁠삑삔삠삣삵샃샵샷섄섯셉셕션셤셥셧셩셴솝솨솰쇅쇡쇽숀숍숏숑숱숴쉑쉔쉭쉼슉슌슘슝슥슭슴슷싁쌕쌤쌰썹쎈쎌쏜쏨쏭쏴쏼쐬쑈쑨쑬쒜쒸쓱씁씸씹않앓앳얍얏얭엊엣옭왑왝왬왹욍욘욜욤욹웁웍웡웩윔윕윰윽읏읫잽쟉쟌쟘젝젹졀졈졉졋졍졔좃좆좍좔좡죔죡죤죵줅줘줴쥭쥴즘즛짭짯짹쨀쨈쩍쩐쩜쩝쩟쩡쫙쫠쭌쮸쯔쯜쯧쯩찟챵첵쳉쳑쳔쳠쳥촘쵹춍츈츤츩츰츱츳츼칫캅캑캭캴컁컥컹켐켜켠콱콸쾅쿄쿰퀄퀑큘킁킴킵탓탠탯텁텟텡텨톄툐툼툽퉤튕튝튠튱틔팁팎팟팰팸팻퍅펍펏펙펴펵폿푀푱퓽픗핌했햐헉헙헴홋홧홱횅훅훙훠훨휑휙휩휭흴힝")

# l:단어의 길이, c:현재 턴 수, t:제한시간, d:소요시간, m:미션글자 포함수
# 2*((5+1*l)**0.74+0.88*c)*(1-(d/(2*t)))*(1+0.5*m)
pr_com=r.choice(data_base)
while pr_com[-1] in kill or pr_com[-1] in t_kill:
    pr_com=r.choice(data_base)

used_word=[]
t=60
c=0
score=0
use_mis=1
st_st=0

print(pr_com)
used_word.append(pr_com)
while 1:
    tr_t=20
    if use_mis==1:
        mis_txt=r.choice('가나다라마바사아자차카타파하까따짜빠싸')
        use_mis=0

    print(f"[system]: 미션 글자는 {mis_txt}입니다.",'-'*20)

    if st_st==0:
        st=tm.time()
    st_st=0
    inp_txt=input()
    if len(inp_txt)==1:
        print("[system]: 한글자입니다. 최소 두글자 이상을 입력해 주시기를 바라겠습니다.")
        continue
    en=tm.time()
    # 게임 포기
    if inp_txt=='gg' or inp_txt=='ㅈㅈ':
        print("\n[system]: 게임을 포기하였습니다.")
        break
    # 실제로 있는 단어인가?
    if inp_txt in data_base and inp_txt[0]==pr_com[-1]:
        #쓴단어 추가
        used_word.append(inp_txt)
        # 단어 길이
        l=len(inp_txt)
        # 턴수 증가
        c+=1
        # 입력시간
        d=en-st
        if d>=30:
            print("\n[system]: 입력 제한 시간 초과.")
            break
        # 제한시간
        t-=d
        #미션단어 개수
        m=0
        for txt in inp_txt:
            if mis_txt==txt:
                m+=1
                use_mis=1

        # 제한시간 넘기면 패배
        if t<=0:
            print("[system]: 제한시간 초과입니다. 당신의 패배입니다.")
            break
        
        pl_sc=int(int((2*((5+2*l)**0.74+0.88*c)*(1-(d/(2*t)))*(1+0.5*m))*100))/100
        score+=pl_sc
        print(f"[system]: {score}점({pl_sc}점 추가)\n당신의 남은 입력 제한 시간 : {int(t*100)/100} (입력 시간 : {int(d*100)/100}")
        # 컴퓨터 출력
        pr_kill=[]
        pr_coli=[]
        for s in data_base:
            # 데이터베이스의 첫번째 글자가 낸 글자의 마지막 글자와 같을때
            if s[0]==inp_txt[-1] and len(s)!=1 and not s in used_word:
                pr_coli.append(s)
                
        if pr_coli!=[]:
            rr=r.randint(0,10)
            if rr==0:
                for s in pr_coli:
                    if s[-1] in kill:
                        pr_kill.append(s)        
                pr_com=r.choice(pr_kill if len(pr_kill)!=0 else pr_coli)
            elif rr>=1 and rr<=6:
                for s in pr_coli:
                    if s[-1] in t_kill:
                        pr_kill.append(s)        
                pr_com=r.choice(pr_kill if len(pr_kill)!=0 else pr_coli)
            elif rr>=7 and rr<=9:
                if len(pr_coli)>=5:
                    pr_com=pr_coli[r.randint(0,5)]
                else:
                    pr_com=pr_coli[r.randint(0,len(pr_coli))]
            else:
                pr_com=r.choice(pr_coli)
            if pr_com in used_word:
                continue
            print(pr_com)
            used_word.append(pr_com)

        else:
            print("[system]: 더이상 이을 수 있는 단어가 존재하지 않습니다. 당신의 승리입니다.")
            break
    else:
        print(f"[system]: 존재하지 않거나 조건에 벗어난 단어입니다. 다시 입력해 주십시오.\n이을 글자:{pr_com[-1]}")
        st_st=1

print("GAMEOVER\n최고점수:",int(score))
if input(f"마지막 글자 {pr_com[-1]} 로 이을 수 있는 단어를 확인하시겠습니까?")=="ㅇ":
    for st in data_base:
            if pr_com[-1]==st[0]:
                print(st)

############################################################
# 컴퓨터간의 끝말잇기(점수 없음)
kill=list("갏갗걋겇겊겿곻굠궃궝귐긑긶긿깆깥깸껸껼꼇꼍꾜꿑뀜끠냏냑냔냘넁넠녁녆녘뇰늄늉닺덟뎧뎬돓됵뒿듈듐듥듦듧듫땽뗌똣뜩뜹랋랒랓랖랗랸럿렁렇렫렷롫룀룅룔뤂뤠륨른릅릇릊릎릏릐맣먕묗묭뮴믁믏믐밇및밗벹볌볜봊봏봠붏붖붚븀븐븜빋뼌뿟쁜쁨샄샥섦섴솣숡숰숳슨싕싥싴싶쎔쑴씃앚앝얒얗얫얶얺엃엋엌엻옄옺왐욷웆웋웝웸윅읃읅읆읋읒읓읔읕읖읗읭잫졎죌즑짗쨔쨤쨩쭘쯕쯘쯤찱챱쳡촙촨춰췐츌츔츨칮칲컽켓켸콫쾃쿱쿽큅큠큭탉탸텋텝텹톹툑튬틋틤팹푄퓔퓸픈픔픠픳핥홣훕휵흿")
t_kill=list("갇갉값갬갭걍걔겜겝겯겻곗곬곶괌괵굄궈궨귄귿긧긱깅깟깩깰꺅꺌껀껏껙껨껭꼉꼿꽂꽐꽛꽤꽥꾐꾹꾼꿉꿋꿔꿜꿱뀀뀌뀨끅끗끙낀낌낏낑낢낵낸냅냬넛넣넨넴녈녑녓녜놉놔뇸뇽눔눕눙뉵늡늣늬닙닝닢댜덛뎀뎁뎃뎍뎜뎝뎡뎨돐돝돠돨됨됭둬뒈듁듕듭듯듸딍딤딧딮땍땐떤떰떳떵떽똔똠똴뙁뚤뚬뜽띔띨띰띵랏랙랠랫랴럴럽렐렘렙렝롄롭롶룹룻뤽륀륄를름릭릿맡몃몌몫몹묑뭄뮌뮨뮬믄믓믜밈밟뱍벰봅봐붑뷜뷩븨븩빰빱빳빽뺌뺙뺨뻑뻣뼉뼘뽁뽄뽐뽓뿅뿍뿐뿜뿡쁠삑삔삠삣삵샃샵샷섄섯셉셕션셤셥셧셩셴솝솨솰쇅쇡쇽숀숍숏숑숱숴쉑쉔쉭쉼슉슌슘슝슥슭슴슷싁쌕쌤쌰썹쎈쎌쏜쏨쏭쏴쏼쐬쑈쑨쑬쒜쒸쓱씁씸씹않앓앳얍얏얭엊엣옭왑왝왬왹욍욘욜욤욹웁웍웡웩윔윕윰윽읏읫잽쟉쟌쟘젝젹졀졈졉졋졍졔좃좆좍좔좡죔죡죤죵줅줘줴쥭쥴즘즛짭짯짹쨀쨈쩍쩐쩜쩝쩟쩡쫙쫠쭌쮸쯔쯜쯧쯩찟챵첵쳉쳑쳔쳠쳥촘쵹춍츈츤츩츰츱츳츼칫캅캑캭캴컁컥컹켐켜켠콱콸쾅쿄쿰퀄퀑큘킁킴킵탓탠탯텁텟텡텨톄툐툼툽퉤튕튝튠튱틔팁팎팟팰팸팻퍅펍펏펙펴펵폿푀푱퓽픗핌했햐헉헙헴홋홧홱횅훅훙훠훨휑휙휩휭흴힝")

print("특정 글자로 시작할 글자를 입력")
inp_txt=input()
used_word=[]
c=0
pr_com=""

while 1:
    #컴
    pr_kill=[]
    pr_coli=[]
    for s in data_base:
        # 데이터베이스의 첫번째 글자가 낸 글자의 마지막 글자와 같을때
        if s[0]==inp_txt[-1] and len(s)!=1 and not s in used_word:
            pr_coli.append(s)
            
    if pr_coli!=[]:
        rr=r.randint(0,10)
        if rr==0:
            for s in pr_coli:
                if s[-1] in kill:
                    pr_kill.append(s)        
            pr_com=r.choice(pr_kill if len(pr_kill)!=0 else pr_coli)
        elif rr>=1 and rr<=6:
            for s in pr_coli:
                if s[-1] in t_kill:
                    pr_kill.append(s)        
            pr_com=r.choice(pr_kill if len(pr_kill)!=0 else pr_coli)
        elif rr>=7 and rr<=9:
            if len(pr_coli)>=5:
                pr_com=pr_coli[r.randint(0,5)]
            else:
                pr_com=pr_coli[r.randint(0,len(pr_coli))]
        else:
            pr_com=r.choice(pr_coli)
        if pr_com in used_word:
            continue
        print(pr_com)
        used_word.append(pr_com)

    else:
        print("[system]: 더이상 이을 수 있는 단어가 존재하지 않습니다.")
        break
    
    inp_txt=pr_com
    c+=1
    
print(c)
