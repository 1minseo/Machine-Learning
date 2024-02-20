from konlpy.tag import Kkma
# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()
text = "아버지가 방에 들어갑니다."

# 형태소 추출 => 토크나이징된 형태소들은 리스트 형태로 반환
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리 => 복합 문장(2개 이상)이 있을 때 문장 단위로 토크나이징
sentences = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(sentences)
print(s)